from operator import itemgetter
import importlib.util
import heapq

spec = importlib.util.spec_from_file_location(
    "module.name", "union-find.py")
union_find = importlib.util.module_from_spec(spec)
spec.loader.exec_module(union_find)

class Graph:

    def __init__(self, V):
        self.V = V
        self.graph = [[] for i in range(V)]
        self.edge_list = []

    def addEdge(self, e1, e2, weight=None):
        self.graph[e1].append((e2, weight))
        self.graph[e2].append((e1, weight))

        heapq.heappush(self.edge_list, (weight, [e1, e2]))


    def get(self):
        print(self.graph)


    def kruskal_algorithm(self):
        # sorte my priority queue
        edge_list = sorted(self.edge_list)

        # initially all vertex are disjoint
        UF = union_find.UnionFind(self.V)
        cost = 0
        for edge in edge_list:
            if not UF.issameSet(edge[1][0], edge[1][1]):
                cost += edge[0]
                UF.unionSet(edge[1][0], edge[1][1])
            
        return cost


# if __name__ == '__main__':
    
#     g = Graph(6)
#     g.addEdge(0, 1, 5)
#     g.addEdge(0, 4, 15)
#     g.addEdge(0, 5, 2)
#     g.addEdge(1, 3, 9)
#     g.addEdge(1, 4, 22)
#     g.addEdge(1, 5, 4)
#     g.addEdge(2, 3, 12)
#     g.addEdge(2, 4, 1)
#     g.addEdge(3, 5, 6)

#     g.get()
    
