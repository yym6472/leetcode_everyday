'''
Definition for a Connection
class Connection:

    def __init__(self, city1, city2, cost):
        self.city1, self.city2, self.cost = city1, city2, cost
'''
class Solution:
    # @param {Connection[]} connections given a list of connections
    # include two cities and cost
    # @return {Connection[]} a list of connections from results
    def lowestCost(self, connections):
        # Write your code here
        connections = sorted(connections, key=lambda x: (x.cost, x.city1, x.city2))
        city_set = set()
        for connection in connections:
            city_set.add(connection.city1)
            city_set.add(connection.city2)
        cities = list(city_set)
        city2idx = {city: idx for idx, city in enumerate(cities)}
        union_find_set = UnionFindSet(len(cities))
        results = []
        for connection in connections:
            if union_find_set.union(city2idx[connection.city1], city2idx[connection.city2]):
                results.append(connection)
        if len(results) == len(cities) - 1:
            results = sorted(results, key=lambda x: (x.cost, x.city1, x.city2))
            return results
        else:
            return []

class UnionFindSet(object):
    def __init__(self, size):
        self.size = size
        self.father = list(range(size))
    def find(self, x):
        if x == self.father[x]:
            return x
        else:
            root = self.find(self.father[x])
            self.father[x] = root
            return root
    def union(self, a, b):
        fa = self.find(a)
        fb = self.find(b)
        if fa != fb:
            self.father[fa] = fb
            return True
        else:
            return False
