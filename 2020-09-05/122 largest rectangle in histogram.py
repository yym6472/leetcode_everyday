class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, height):
        # write your code here
        from collections import deque
        height = [-1] + height + [-1]  # 两边添加-1避免特殊处理
        stack = deque([])
        max_area = 0
        for idx, num in enumerate(height):
            if not stack:
                stack.append((num, idx, idx))
                continue
            while stack and peak(stack)[0] > num:
                # 栈中元素存储的依次是：该元素的height、该元素的左边界index、该元素的index
                value, left_idx, cur_idx = stack.pop()
                max_area = max(max_area, value * (idx - left_idx))
            value, left_idx, cur_idx = peak(stack)
            if value == num:
                stack.append((num, left_idx, idx))
            else:
                stack.append((num, cur_idx + 1, idx))
        return max_area

def peak(stack):
    item = stack.pop()
    stack.append(item)
    return item


solution = Solution()
print(solution.largestRectangleArea([2,1,5,6,2,3]))