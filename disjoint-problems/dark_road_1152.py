import heapq

class UnionFind:

    def __init__(self, pset_length):
        self.pset = [i for i in range(pset_length)]

    def find_set(self, i):
        if self.pset[i] == i: return i

        self.pset[i] = self.find_set(self.pset[i])
        return self.pset[i]

    def union_set(self, i, j):
        self.pset[self.find_set(i)] = self.find_set(j)

    def issame_set(self, i, j):
        if self.find_set(i) == self.find_set(j):
            return True
        else:
            return False

class Graph:

    def __init__(self):
        self.edge_list = []

    def add_edge(self, u, v, w):
        heapq.heappush(self.edge_list,(w, [u, v]))


if __name__ == "__main__":

    g = Graph()
    m, n = list(map(int, input().split(' ')))

    while(n != 0):

        for i in range(n):
            x, y, z = list(map(int,input().split(' ')))
            g.add_edge(x, y, z)

        m, n = list(map(int,input().split(' ')))
        print(g.edge_list)

    
