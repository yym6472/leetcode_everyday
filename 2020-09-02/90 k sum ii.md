## 题意

- 链接：[https://www.lintcode.com/problem/k-sum-ii/description](https://www.lintcode.com/problem/k-sum-ii/description)

题意为：给定`n`个**不同**的**正整数**，需要找到其中的`k`个数，加起来正好等于`target`。需要给出所有的方案。

## 解法

深度优先搜索，搜索的状态定义为**当前的选取列表、当前考虑选取的下标**。每一次dfs中的邻居为：
1. 将当前考虑选取的下标的元素加入选取列表，将下标加一
2. 不将当前考虑选取的下标的元素加入选取列表，下标加一

需要剪枝的地方：
- 当选取的元素个数超出`k`
- 当元素之和超过`target`
- 当下标超出数组边界