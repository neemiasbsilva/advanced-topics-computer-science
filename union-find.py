
class UnionFind:

    def __init__(self, pset):

        self.pset = [i for i in range(len(pset))]

    
    def findSet(self, i):
        if self.pset[i] == i: return i

        self.pset[i] = self.findSet(self.pset[i])
        
        return self.pset[i]

    def unionSet(self, i, j):
        self.pset[self.findSet(i)] = self.findSet(j)

    def issameSet(self, i, j):
        if self.findSet(i) == self.findSet(j):
            return True
        else:
            return False

if __name__ == '__main__':
    
    pset = [0, 1, 2, 3, 4]

    UN = UnionFind(pset)

    UN.unionSet(0, 1)
    UN.unionSet(1, 2)
    UN.unionSet(3, 1)   
    print(UN.findSet(0))
    print(UN.issameSet(0, 4))
    print(UN.pset)

    
    
