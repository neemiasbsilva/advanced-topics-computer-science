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
        
        return False

class Graph:

    def __init__(self, V):
        self.V = V
        self.edge_list = []

    def add_edge(self, u, v, w):
        heapq.heappush(self.edge_list,[w, (u, v)])

    def krukals_algorithm(self):
        
        s_edge_list = sorted(self.edge_list, key= lambda ele: ele[0])
        # s_edge_list = self.edge_list.copy()

        # print(s_edge_list)
        uf  = UnionFind(self.V)
        cost = 0
        for edge in s_edge_list:
            if not uf.issame_set(edge[1][0], edge[1][1]):
                cost += edge[0]
                uf.union_set(edge[1][0], edge[1][1])

        return cost
if __name__ == "__main__":

    m, n = list(map(int, input().split(' ')))
    g = Graph(m)
    while(n != 0):

        for i in range(n):
            x, y, z = list(map(int,input().split(' ')))
            g.add_edge(x, y, z)
        print(g.krukals_algorithm())
        m, n = list(map(int,input().split(' ')))
        g = Graph(m)

    
