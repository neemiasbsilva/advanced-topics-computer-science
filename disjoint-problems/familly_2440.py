
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



if __name__ == "__main__":
    n, m = list(map(int, input().split(' ')))

    uf = UnionFind(n)

    for i in range(m):

        ele1, ele2 = list(map(int, input().split(' ')))
        ele1 -= 1
        ele2 -= 1
        uf.union_set(ele1, ele2)
    
    family_set = []

    for i in range(len(uf.pset)):
        family_set.append(uf.find_set(uf.pset[i]))
    
    print(len(set(family_set)))