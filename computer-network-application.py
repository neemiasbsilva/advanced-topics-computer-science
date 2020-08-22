import importlib.util
from graph import Graph

spec = importlib.util.spec_from_file_location(
    "module.name", "union-find.py")
union_find = importlib.util.module_from_spec(spec)
spec.loader.exec_module(union_find)

def kruskal(G, E):

    
        UF = union_find.UnionFind(pset)

if __name__ == '__main__':
    G = Graph(6)
    G.addEdge(0, 1, 5)
    G.addEdge(0, 4, 15)
    G.addEdge(0, 5, 2)
    G.addEdge(1, 3, 9)
    G.addEdge(1, 4, 22)
    G.addEdge(1, 5, 4)
    G.addEdge(2, 3, 12)
    G.addEdge(2, 4, 1)
    G.addEdge(3, 5, 6)

    print(G.kruskal_algorithm())


