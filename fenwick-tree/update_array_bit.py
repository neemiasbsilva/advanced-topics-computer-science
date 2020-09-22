from sys import stdin, stdout

LSOne = lambda b: b&(-b)

class FenwickTree:

    def __init__(self, n):
        self.ft = [0 for i in range(n+1)]

    def rsq_util(self, b):
        
        s = 0

        while b > 0:
            s += self.ft[b]
            b -= LSOne(b)
        return s

    def adjust(self, k, v):

        while k < len(self.ft):
            self.ft[k] += v
            k += LSOne(v)

if __name__ == "__main__":
    t = int(stdin.readline())
    for case in range(t):
        n, u = stdin.readline().split(' ')
        n = int(n)
        u = int(u)
        fenwick_tree = FenwickTree(n)
        for i in range(u):
            l, r, val = stdin.readline().split(' ')
            l = int(l)
            r = int(r)
            val = int(val)

            fenwick_tree.adjust(l, val)
            if r+1 <= n:
                fenwick_tree.adjust(r+1, -val)

        q  = int(stdin.readline())

        for i in range(q):
            out = fenwick_tree.rsq_util(int(stdin.readline()))
            stdout.write(str(out)+'\n')