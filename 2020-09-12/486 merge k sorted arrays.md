## 题意

- 链接：[https://www.lintcode.com/problem/merge-k-sorted-arrays/description](https://www.lintcode.com/problem/merge-k-sorted-arrays/description)

题意为，给定`k`个有序数组（长度可以不一样），要求将他们合并为一个大的排序数组。

## 题解

对每个有序数组维护一个指针，将指针所指位置的元素放入小顶堆中。每次从小顶堆中弹出一个元素，append到新的数组中，并且将对应列表的指针向后移一位，将下一个元素加入小顶堆（当指针到达末尾时，则不再添加）。这样做直到小顶堆中没有额外元素，返回新的序列即可。

堆的最大大小为`k`，每次入堆、出堆的时间复杂度为`O(logk)`，因此总的时间复杂度为`O(nlogk)`，其中`n`为所有数组的总长度。