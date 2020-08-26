class Solution:
    """
    @param A: an array
    @return: total of reverse pairs
    """
    def reversePairs(self, A):
        sorted_array = sorted(list(set(A)))
        value2idx = {value: idx for idx, value in enumerate(sorted_array)}
        bit = BinaryIndexTree(len(value2idx))

        count = 0
        A.reverse()
        for number in A:  # from the last number to the first number
            # count for numbers whose value is less than the current one but the index is larger
            count += bit.query(value2idx[number] - 1)
            # update the binary index tree
            bit.update(value2idx[number], 1)  # add the current number (count += 1) to BIT
        return count



class BinaryIndexTree(object):
    def __init__(self, size: int) -> None:
        self.size = size
        self.data = [0] * size
    
    def update(self, position: int, delta: int) -> None:
        """
        Update the array[position] by adding the delta. position is the 0-based index.
        """
        assert position >= 0 and position < self.size
        position += 1  # convert to the 1-based index
        while position <= self.size:
            self.data[position - 1] += delta
            position += lowbit(position)

    def query(self, position: int) -> int:
        """
        Query the sum from array[0] to array[position]. position is the 0-based index.
        """
        if position < 0:  # the position may be -1
            return 0
        assert position >= 0 and position < self.size
        position += 1  # convert to the 1-based index
        result = 0
        while position > 0:
            result += self.data[position - 1]
            position -= lowbit(position)
        return result


def lowbit(x: int) -> int:
    """
    Return the lowbit of x in binary.
    E.g., 6 (0110) -> 2 (0010)
          8 (1000) -> 8 (1000)
          13 (1101) -> 1 (0001)
    """
    return x & -x


if __name__ == "__main__":
    solution = Solution()
    solution.reversePairs([4,4,2])