# -*- coding: utf-8 -*-

'''
Input example:
3 5
C 1 2
F 1 2
C 1 2
F 1 3
C 1 3

Output example:
N
S
S
'''


class UnionFind:

    def __init__(self, pset_length):
        self.pset = [i for i in range(pset_length)]


    def findSet(self, i):
        if self.pset[i] == i:
            return i

        self.pset[i] = self.findSet(self.pset[i])
        return self.pset[i]

    def unionSet(self, i, j):
        self.pset[self.findSet(i)] = self.findSet(j)

    def issameSet(self, i, j):
        if self.findSet(i) == self.findSet(j):
            return True

        return False


if __name__ == "__main__":

    N, K = list(input().split(' '))
    N, K = int(N), int(K)

    UF = UnionFind(N)

    for i in range(K):
        # example: C 1 2
        ope = input().split(' ')

        if ope[0] == 'C':
            if UF.issameSet(int(ope[1])-1, int(ope[2])-1):
                print('S')
            else:
                print('N')
        else:
            UF.unionSet(int(ope[1])-1, int(ope[2])-1)
