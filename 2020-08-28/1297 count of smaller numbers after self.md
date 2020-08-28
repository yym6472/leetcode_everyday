## 简介

- 链接：[https://www.lintcode.com/problem/count-of-smaller-numbers-after-self/description](https://www.lintcode.com/problem/count-of-smaller-numbers-after-self/description)

这道题的题意是：给定一个整数数组`nums`，需要输出一个新的数组`counts`，其中`counts[i]`为`nums[i]`右侧比其小的数的个数。

## 解法

这道题和[求逆序数对](./../2020-08-26/532%20reverse-pairs.md)几乎一样，区别仅在于需要将每个元素的逆序数对分别记录输出。仅用来巩固树状数组的写法，不再细说。