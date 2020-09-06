## 题意

- 链接：[https://www.lintcode.com/problem/connecting-graph-ii/description](https://www.lintcode.com/problem/connecting-graph-ii/description)

题意为：给定图中的`n`个节点，一开始图中没有边，需要完成下面两个方法：
1. `connect(a, b)`：在节点`a`和`b`之间连接一条边；
2. `query(a)`：返回图中包含`a`的联通区域的节点个数。

## 解法

标准的并查集模板题。只需要额外记录并查集中，每棵树（即连通块）所包含的节点个数即可。在合并时，将根节点的联通节点数加一。