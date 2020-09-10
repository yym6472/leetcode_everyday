## 题意

- 链接：[https://www.lintcode.com/problem/k-closest-points/description](https://www.lintcode.com/problem/k-closest-points/description)

题意为：给定若干个平面上的点`points`，以及一个目标点`origin`，要求找到`points`中离`origin`最近的`k`个点，并且按从近到远的顺序返回。

## 题解

在`Point`上定义大小比较关系，然后使用一个大顶堆，保存最近的`k`个点，最后依次弹出，就得到有序的列表了。