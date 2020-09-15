## 题意

- 链接：[https://www.lintcode.com/problem/cut-the-cake/description](https://www.lintcode.com/problem/cut-the-cake/description)

题意为：有一块`n * m`的蛋糕，有`k`个草莓分布在蛋糕上。现在要求将蛋糕切开使得每块蛋糕上恰有一个草莓，蛋糕只能水平或竖直切，求刀切的最短长度。

`n`和`m`均不超过`20`。

## 题解

使用记忆化DFS，状态定义为蛋糕矩形的两个坐标。每次搜索，分别横向和纵向枚举切分线即可。