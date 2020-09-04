## 题意

- 链接：[https://www.lintcode.com/problem/number-of-islands-ii/description](https://www.lintcode.com/problem/number-of-islands-ii/description)

在`n * m`的数组中，初始所有地块（元素）都为`0`，表示都是海洋。给定一个坐标数组`A`，每一个坐标表示将对应地块由海洋变为陆地，要求每次数组变动后，都返回岛屿的数量。

这道题相比[433 number of islands](../2020-08-30/433%20number%20of%20islands.md)的不同在于其地块是动态的变化的，题目要求每一次变动后返回新的岛屿的个数。


## 解法

若直接套用[433 number of islands](../2020-08-30/433%20number%20of%20islands.md)的解法（BFS/DFS），则每次计算岛屿个数的复杂度为`O(n*m)`，总的时间复杂度为`O(n*m*len(A))`。当`A`较大时，复杂度很高。

直观的想法是，维护一个当前岛屿的列表，若新生成的陆地与任意一个岛屿相邻，则将其并入该岛屿；否则，新生成一个岛屿。

这里使用并查集的数据结构，能够高效的合并陆地到岛屿，以及查询每块陆地是否属于相同的岛屿。每次新生成一块陆地时，将其认为是独立的一个岛屿（当前岛屿数+1），随后检查它四个方向是否存在相邻的陆地。
若存在陆地，则**判断它们是否已经属于同一个岛屿**，若不属于：**合并两个岛屿**，并将岛屿数-1；否则，不做任何处理。

这里存在两个操作：判断两块陆地是否属于同一个岛屿，以及合并两个岛屿。这也正是并查集支持的两个操作，且在实现恰当的时候，它们的平均复杂度都接近常数。

并查集的`find`一般可以使用一行代码快速实现：
```C++
int find(int x) {
    return father[x] == x ? x : father[x] = find(father[x]);
}
```
展开后的逻辑是：
```C++
int find(int x) {
    if (father[x] == x) {
        return x;
    } else {
        super_father = find(father[x]);
        father[x] = super_father;
        return super_father;
    }
}
```

这是一个递归查找父节点的过程，同时`father[x] = super_father;`这行代码又将递归过程一路上的节点直接与根节点相连，称为**路径压缩**。经过这一步后，整棵树将变得非常扁平，也就保证了其常数级别的复杂度。

可以看到并查集实现简单、又非常高效，是相当优美的数据结构。