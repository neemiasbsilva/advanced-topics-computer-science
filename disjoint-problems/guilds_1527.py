

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
    while True:
        n, m = list(map(int, input().split(' ')))
        if n == 0:
            break
        
        player_points = list(map(int, input().strip(' ').split(' ')))
        uf = UnionFind(n)
        number_wins = 0
        
        for i in range(m):
            q, a, b = list(map(int, input().split(' ')))
            a -= 1
            b -= 1
            if q == 1:
                p1, p2 = player_points[a], player_points[b]
                uf.union_set(a, b)
                player_points[uf.find_set(a)] = p1 + p2


            else:
                a_parent = uf.find_set(a)
                b_parent = uf.find_set(b)
                rafael_parent = uf.find_set(0)

                if rafael_parent == a_parent:
                    if player_points[a_parent] > player_points[b_parent]: number_wins+=1
                elif rafael_parent == b_parent:
                    if player_points[b_parent] > player_points[a_parent]: number_wins+=1

        print(number_wins)
