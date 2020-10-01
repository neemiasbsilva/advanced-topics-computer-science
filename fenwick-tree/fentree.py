from sys import stdout, stdin

LSOne = lambda b: b&(-b)

class FenwickTree:

    def __init__(self, n):
        self.n = n+1
        self.ft = [0 for i in range(n+1)]

    def rsq_util(self, b):
        s = 0

        while b > 0:
            s += self.ft[b]
            b -= LSOne(b)

        return s

    def rsq(self, a, b):
        return self.rsq_util(b) - (0 if a == 1 else self.rsq_util(a-1))

    def adjust(self, k, v):

        while k < self.n:
            self.ft[k] += v
            k += LSOne(k)

if __name__ == "__main__":
    
    n = int(stdin.readline())

    values = list(map(int, stdin.readline().strip().split()))
    
    fenwick_tree = FenwickTree(n)

    for k, v in enumerate(values):
        fenwick_tree.adjust(k+1, v)

        
    q = int(stdin.readline())

    for i in range(q):
        q_u, l_i, r_x = list(map(str, stdin.readline().strip().split()))
        l_i = int(l_i)
        r_x = int(r_x)
        if q_u == 'q':
            stdout.write(str(fenwick_tree.rsq(l_i, r_x))+'\n')
        else:
            fenwick_tree.adjust(l_i, r_x)
