## 题意

- 链接：[https://www.lintcode.com/problem/course-schedule-ii/description](https://www.lintcode.com/problem/course-schedule-ii/description)

有`n`门课程，编号为`0`到`n - 1`。给定某些课程的前后置关系`(i, j)`（表示完成课程`i`必须先完成课程`j`），求任意完成课程的顺序。

## 解法

这道题是拓扑排序，可以使用类似BFS的方法。首先将所有入度为`0`的节点加入队列；在每一次循环中，弹出队列的第一个元素，将其连接的所有节点的入度减一；如果某节点入度达到零，则将其加入队列即可。

这里记录一个需要注意的点，在我处理每个课程的依赖课程时，在初始化时写了：
```python
neighbors = [[]] * numCourses
```

这样就会发现添加完依赖课程后，每个子列表的元素都是相同的。是因为外层列表中存放的元素都是**指向同一个列表对象的指针**。
而正确的写法应该是：
```python
neighbors = [[] for _ in range(numCourses)]
```
这样才会每一次单独创建一个子列表。