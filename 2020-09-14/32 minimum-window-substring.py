class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def minWindow(self, source, target):
        if not source or not target:
            return ""
        
        n = len(source)
        left_ptr, right_ptr = 0, 0
        condition = Condition(target)
        condition.add_char(source[0])
        result = None

        while right_ptr < n:
            if condition.check():
                if result is None or right_ptr - left_ptr + 1 < len(result):
                    result = source[left_ptr:right_ptr+1]
                condition.remove_char(source[left_ptr])
                left_ptr += 1
            else:
                right_ptr += 1
                if right_ptr < n:
                    condition.add_char(source[right_ptr])
        return result or ""


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


solution = Solution()
print(solution.minWindow("adobecodebanc", "abc"))