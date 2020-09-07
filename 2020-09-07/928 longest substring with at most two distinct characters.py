class Solution:
    """
    @param s: a string
    @return: the length of the longest substring T that contains at most 2 distinct characters
    """
    def lengthOfLongestSubstringTwoDistinct(self, s):
        if not s:
            return 0
        left_ptr, right_ptr = 0, 0
        counter = CharCounter()
        counter.add(s[0])
        max_length = 0
        while right_ptr < len(s):
            if counter.num_char_types <= 2:  # move the right pointer
                max_length = max(max_length, right_ptr - left_ptr + 1)
                right_ptr += 1
                if right_ptr < len(s):
                    counter.add(s[right_ptr])
            else:  # move the left pointer
                counter.remove(s[left_ptr])
                left_ptr += 1
        return max_length


class CharCounter:
    def __init__(self):
        self.counter = {}
        self.num_char_types = 0
    def add(self, ch):
        if ch not in self.counter:
            self.counter[ch] = 0
            self.num_char_types += 1
        self.counter[ch] += 1
    def remove(self, ch):
        assert ch in self.counter
        if self.counter[ch] == 1:
            self.num_char_types -= 1
            del self.counter[ch]
        else:
            self.counter[ch] -= 1