## 介绍

- 链接: [https://www.lintcode.com/problem/reverse-pairs/description](https://www.lintcode.com/problem/reverse-pairs/description)

这道题求一个数组的逆序对数，应该有多种时间复杂度为O(nlogn)的解法，这里使用树状数组（Binary Indexed Tree）来做。

## 树状数组

### 结构

树状数组的结构图如下：

![image.png](https://i.loli.net/2020/08/26/QXu8eAjwz36qlTc.png)

其中`A`数组为逻辑或概念上的数据，是有实际意义的、我们真正想维护的数组；而`C`数组则是实际上保存在树状数组这一数据结构中的数组。他们之间满足下面的关系：
```
00001	C[1]：	A[1]
00010	C[2]：	A[1] + A[2]
00011	C[3]：	A[3]
00100	C[4]：	A[1] + A[2] + A[3] + A[4]
00101	C[5]：	A[5]
00110	C[6]：	A[5] + A[6]
00111	C[7]：	A[7]
01000	C[8]：	A[1] + A[2] + A[3] + A[4] + A[5] + A[6] + A[7] + A[8]
01001	C[9]：	A[9]
01010	C[10]：	A[9] + A[10]
01011	C[11]：	A[11]
..... .....    .....
```
通过这种关系，使得对数组A的单点更新和区间查询操作都能在log(n)时间复杂度内完成。

先引入一个函数操作叫作`lowbit`，他的作用是取`x`在二进制表示下的最低一位`1`。例如，对于数字`6`，其二进制表示为`0110`，那么最低位为第二位`0010`，即`2`；
而对于数字`13`，其二进制表示`1101`，最低位为第一位`0001`，即`1`；对于数字`8`，二进制表示`1000`，其最低位为第四位`1000`，即`8`。

通过观察上面的结构图，以及`A`和`C`之间的关系，可以得出一些结论：
- 结构图中，`C[x]`的父节点为`C[x + lowbit(x)]`
- `A`和`C`满足的关系为：`C[x] = A[x - lowbit(x) + 1] + ... + A[x]`

### 操作

1. 查询
    为了查询`A[1]`到`A[x]`的区间和，从`x`开始，每次将`x`减去`lowbit(x)`，然后将`C[x]`累加即可，例如：
    ```
    S[13] = A[1] + ... + A[13]
          = (A[1] + ... + A[8]) + (A[9] + ... + A[12]) + (A[13])
          = C[8] + C[12] + C[13]
          = C[12 - lowbit(12)] + C[13 - lowbit(13)] + C[13]
    ```
    python实现如下（这里为了不浪费空间，进行了一个坐标映射，将从1开始的index变换为从0开始的index）：
    ```python
    def query(self, position: int) -> int:
        """
        Query the sum from array[0] to array[position]. position is the 0-based index.
        """
        assert position >= 0 and position < self.size
        position += 1  # convert to the 1-based index
        result = 0
        while position > 0:
            result += self.data[position - 1]
            position -= lowbit(position)
        return result
    ```
2. 更新
    为了更新`A[x]`的值，需要从`A[x]`开始，依次更新包含`A[x]`的所有`C`数组中的元素，而`C`的哪些位置包含`A[x]`，其实就是从`C[x]`开始不断找父节点，即`C[x + lowbit(x)]`，直到`x`超出数组最大长度。
    python代码如下：
    ```python
    def update(self, position: int, delta: int) -> None:
        """
        Update the array[position] by adding the delta. position is the 0-based index.
        """
        assert position >= 0 and position < self.size
        position += 1  # convert to the 1-based index
        while position <= self.size:
            self.data[position - 1] += delta
            position += lowbit(position)
    ```

## 求逆序对个数

为了求逆序对个数，只需要倒序遍历原始数组，同时维护的目标（即`A`数组）是**当前数字之后（因为是倒叙遍历的）不同的数字出现的次数**。例如数字`2`在当前数字之后出现了5次，那么此时应该有`A[2] = 5`。

这样，在计算当前数字的逆序数时，就可以将它转化为求区间和。例如当前数字是`20`，如果我要求小于`20`出现过的次数，我只要求`A[1] + A[2] + ... + A[19]`就可以了（因为保存的是每一个数字出现的个数）。
此时使用一个查询操作即可。

但这里还有个问题，就是数字可能很大，比如`100000000`，这样的话`A`数组也要开得很大，比如`A[100000000]`。这里可以用离散化的方式解决，因为在求逆序数问题里，我们并不关心数字的具体大小，而
只关心数字的相对大小，因此只要先对数组排一个序（注意去重），然后建立每个数值到index的映射就可以了。这样能保证index较小的数必然数值上也较小，这样只需要使用index来代替数值进行上述操作即可。
