## 题意

- 链接：[https://www.lintcode.com/problem/minimum-window-substring/description](https://www.lintcode.com/problem/minimum-window-substring/description)

这道题的题意为，给定两个字符串`source`和`target`，求`source`中最短的包含`target`中每一个字符的子串。
例如，当`target`为`aabc`时，需要找到`source`中最短的包含两个`a`，一个`b`和一个`c`的子串。

## 题解

同向双指针题目，和[928 longest substring with at most two distinct characters](../2020-09-07/928%20longest%20substring%20with%20at%20most%20two%20distinct%20characters.md)的区别在于条件不同，做法类似。

这里条件的实现如下代码所示：
```python
class Condition(object):
    def __init__(self, target):
        self.char_dict = {}
        for ch in target:
            if ch not in self.char_dict:
                self.char_dict[ch] = 0
            self.char_dict[ch] += 1
        self.needed = len(self.char_dict)
    def add_char(self, ch):
        if ch in self.char_dict:
            self.char_dict[ch] -= 1
            if self.char_dict[ch] == 0:
                self.needed -= 1
    def remove_char(self, ch):
        if ch in self.char_dict:
            self.char_dict[ch] += 1
            if self.char_dict[ch] == 1:
                self.needed += 1
    def check(self):
        return self.needed == 0
```

分别在右指针移动和左指针移动的时候，使用`add_char`和`remove_char`来更新当前子串覆盖target的情况。

这里的`self.needed`类似一个信号量，记录**当前未被满足的target中的字符类型数目**。每当增加一个字符后，该字符剩余需要的个数等于零，说明该字符类型被满足，因此`self.needed -= 1`；
同理，每当减少一个字符后，该字符剩余需要的个数等于一，说明该字符类型在减少该字符后，重新不再满足覆盖`target`中该类型字符的条件，因此`self.needed += 1`。
当`self.needed == 0`时，表示target中的所有字符类型都被当前子串覆盖，因而当前子串`source[left_ptr:right_ptr+1]`就是满足条件的子串。