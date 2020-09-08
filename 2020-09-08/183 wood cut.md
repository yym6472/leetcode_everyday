## 题意

- 链接：[https://www.lintcode.com/problem/wood-cut/description](https://www.lintcode.com/problem/wood-cut/description)

这道题的题意为：有`n`条给定长度的原木，现在需要将它们加工处理成`k`条长度相同的小段木头，求小段木头的最大长度。

## 题解

使用二分查找，目标是**最后一个使得条件成立的位置**。判断条件为：所有原木能否切成`k`段指定长度的小段。

查找最后一个使得条件成立的位置的模板（“OOOOXXX”类型）如下：
```python
def binary_search(start, end, check):
    left, right = start, end
    while left + 1 < right:
        mid = left + (right - left) / 2
        if check(mid):
            left = mid
        else:
            right = mid
    if check(right):
        return right
    if check(left):
        return left
    return -1
```