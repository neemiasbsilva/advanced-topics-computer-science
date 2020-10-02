from sys import stdout, stdin


class UnionFind:

    def __init__(self, n):
        self.n = n
        self.pset = [i for i in range(n)]
        self.qtd = [1 for i in range(n)]

    
    def find_set(self, i):
        if self.pset[i] == i:
            return i
        self.pset[i] = self.find_set(self.pset[i])
        return self.pset[i]

    
    def union_set(self, i, j):
        m1, m2 = self.find_set(i), self.find_set(j)
        if m1 == m2: return self.qtd[m1] # same family
        
        p1, p2 = self.qtd[m1], self.qtd[m2] # query the number of people i and j are.

        self.pset[m1] = m2

        self.qtd[m2] = p1+p2

        return self.qtd[m2]



    def is_same_set(self, i, j):
        return self.find_set(i) == self.find_set(j)


if __name__ == "__main__":
    
    t = int(stdin.readline())
    for case in range(t):
        map_input = {}

        n = int(stdin.readline())
        n_people = 0
        relation = []
        for rel in range(n):
            s1, s2 = stdin.readline().strip().split()
            relation.append((s1, s2))
            if not (s1 in map_input):
                map_input[s1]= n_people
                n_people += 1
            if not (s2 in map_input):
                map_input[s2] = n_people
                n_people += 1

        uf = UnionFind(n_people)
        for s1, s2 in relation:
            
            stdout.write(str(uf.union_set(map_input[s1], map_input[s2]))+'\n')
