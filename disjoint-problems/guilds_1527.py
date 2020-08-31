

class UnionFind:

    def __init__(self, pset_length, player_points):
        self.pset = [i for i in range(pset_length)]
        self.player_points = player_points

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
        uf = UnionFind(n, player_points)
        number_wins = 0
        for i in range(m):
            q, a, b = list(map(int, input().split(' ')))
            a -= 1
            b -= 1
            if q == 1:
                uf.union_set(a, b)

            else:
                a_parent = uf.find_set(a)
                b_parent = uf.find_set(b)

                guilds_a = [i for i in range(len(uf.pset)) if uf.pset[i] == a_parent]
                guilds_b = [i for i in range(len(uf.pset)) if uf.pset[i] == b_parent]

                result_a = result_b = 0

                for i in range(len(guilds_a)):
                    result_a += player_points[guilds_a[i]]
                
                for i in range(len(guilds_b)):
                    result_b += player_points[guilds_b[i]]

                if guilds_a[0] == player_points[0]:
                    if result_a > result_b: number_wins += 1
                else:
                    if result_b > result_a: number_wins += 1

        print(number_wins)
