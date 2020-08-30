## 题意

- 链接：[https://www.lintcode.com/problem/number-of-islands/description](https://www.lintcode.com/problem/number-of-islands/description)

题意为：给定一个二维数组，其中1表示陆地，0表示海洋，相邻的陆地相互连接。要求输出其中“岛屿”的个数，即其中“1的连通块”的个数。

## 解法

这道题使用BFS和DFS均可以解决。其中BFS/DFS的作用就是遍历整张图，在遍历过程中将其中陆地的元素从1改为0。最后bfs/dfs的次数就是岛屿的个数。

使用bfs做这道题需要注意，应该在元素入队列前将其置为0，而不是在出队列才做这一步。否则将会导致同一个元素重复入队，造成TLE。或者也可以使用一个单独的visited集合。