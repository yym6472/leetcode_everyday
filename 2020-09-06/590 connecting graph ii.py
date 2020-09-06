class ConnectingGraph2:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        self.father = list(range(n))
        self.count = [1 for _ in range(n)]

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def connect(self, a, b):
        a, b = a - 1, b - 1
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = self.father[root_b]
            self.count[root_b] += self.count[root_a]

    """
    @param: a: An integer
    @return: An integer
    """
    def query(self, a):
        a = a - 1
        root_a = self.find(a)
        return self.count[root_a]

    def find(self, x):
        if self.father[x] == x:
            return x
        else:
            root = self.find(self.father[x])
            self.father[x] = root            
            return root