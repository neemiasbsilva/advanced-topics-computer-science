from sys import stdout, stdin


class UnionFind:

    def __init__(self, n):
        self.n = n
        self.pset = [i for i in range(n)]

    
    def find_set(self, i):
        if self.pset[i] == i:
            return i
        self.pset[i] = self.find_set(self.pset[i])
        return self.pset[i]

    
    def union_set(self, i, j):
        self.pset[self.find_set(i)] = self.find_set(j)

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
            
            uf.union_set(map_input[s1], map_input[s2])
            people = 0
            for i in range(len(uf.pset)):
                if uf.is_same_set(map_input[s1], uf.pset[i]): people += 1

            stdout.write(str(people)+'\n')
