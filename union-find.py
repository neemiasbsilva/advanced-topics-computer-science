
class UnionFind:

    def __init__(self, pset_length):

        self.pset = [i for i in range(pset_length)]
        self.rank = [0 for i in range(pset_length)]

    
    def findSet(self, i):
        if self.pset[i] == i: return i

        self.pset[i] = self.findSet(self.pset[i])
        
        return self.pset[i]

    def unionSet(self, i, j):
        self.pset[self.findSet(i)] = self.findSet(j)

    def unionSetRank(self, i, j):
        if not self.issameSet(i, j):
            x, y = self.findSet(i), self.findSet(j)
            if self.rank[x] > self.rank[y]:
                self.rank[y] = x
            else:
                self.rank[x] = y

                if self.rank[x] == self.rank[y]:
                    self.rank[y] += 1
            

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

    
    
