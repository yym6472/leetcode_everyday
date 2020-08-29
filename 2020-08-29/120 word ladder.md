## 题意

- 链接：[https://www.lintcode.com/problem/word-ladder/description](https://www.lintcode.com/problem/word-ladder/description)

这道题的题意为：给定两个单词`start`和`end`和一个词典`dict`，要求找出一条将`start`转换成`end`的最少步数，其中“一步”指变动单词中的任意一个字母，并且变动后的单词需要出现在`dict`中。

## 解法

将字典中的每一个单词认为是一个节点，单词与单词之间的边定义为“只有一个字母存在区别”，由此可以建立一张简单图。简单图求最短路径，一般可以采用BFS算法。

BFS的模板一般如下：
```python
from collections import deque

def bfs(start, end):
    q = deque()
    visited = set([start])
    q.append(start)
    level = 0
    while q:  # while queue is not empty
        level += 1  # the current level of the generated tree
        for _ in range(len(q)):
            current = q.popleft()
            if match(current, end):  # current is the end node
                return level  # return the minimum length of path
            for neighbor in current.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
    return -1  # unreachable
```

需要注意的是这道题里的建图策略，有几种方法：
- 预先处理所有字典中的单词节点，为每个单词节点记录`neighbors`，构建邻接表
- 在bfs中动态判断每个单词在字典中的邻居
- 在bfs中，根据当前单词节点，枚举每一个位置的字符（`a` - `z`），构建对当前字符所有可能的相邻单词节点，再根据字典进行筛选

实现时，字典、visited都使用HashSet，因此插入、查询、判断是否存在的复杂度都可以认为是`O(1)`。假设单词长度为n，字典大小为m，上面三种策略的复杂度分别为：
- O(m^2 * n)
- O(m^2 * n)
- O(m * n) （但是常数可能较大，因为有26的因子）

当m较大时，第三种策略应该是更优的。