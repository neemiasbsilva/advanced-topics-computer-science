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
            k += LSOne(k)

if __name__ == "__main__":
    t = int(stdin.readline())
    for case in range(t):
        n, u = stdin.readline().split(' ')
        n = int(n)
        u = int(u)
        fenwick_tree = FenwickTree(n)

        # print()
        # print("0: {}".format(fenwick_tree.ft))
        for i in range(u):
            l, r, val = stdin.readline().split(' ')
            l = int(l)
            r = int(r)
            val = int(val)

            fenwick_tree.adjust(l+1, val)
            fenwick_tree.adjust(r+2, -val)

            # print("{}: {}".format(i+1, fenwick_tree.ft))

        q  = int(stdin.readline())

        for i in range(q):
            val = int(stdin.readline())+1
            out = fenwick_tree.rsq_util(val)
            stdout.write(str(out)+'\n')
