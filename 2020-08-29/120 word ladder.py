class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        dict.add(end)
        from collections import deque
        q = deque()
        q.append(start)
        visited = set([start])
        level = 0
        while q:
            level += 1
            for i in range(len(q)):
                current = q.popleft()
                count.append(current)
                if current == end:
                    return level
                for neighbor in get_neighbors(current, dict):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
        return -1

def get_neighbors(word, dict):
    all_results = set()
    for pos in range(len(word)):
        for off in range(26):
            char = chr(97 + off)
            if word[pos] == char:
                continue
            new_word = word[:pos] + char + word[pos+1:]
            if new_word in dict:
                all_results.add(new_word)
    return all_results