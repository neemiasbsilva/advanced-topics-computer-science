from sys import stdin, stdout

LSOne = lambda b: b&(-b)

class FenwickTree:

    def __init__(self, n):
        self.ft = [0 for i in range(n+1)]

    def rsq_util(self, b): # return RSQ(1, b)
        s = 0
        while b > 0:
            s += self.ft[b]
            b -= LSOne(b)
        return s
    def rsq(self, a, b):
        return self.rsq_util(b) - (0 if a == 1 else self.rsq_util(a-1))

    def adjust(self, k, v):
        
        while k < len(self.ft):
            self.ft[k] += v
            k += LSOne(k)



if __name__ == "__main__":

    n = int(stdin.readline())

    fenwick_tree = FenwickTree(n)

    n_buggys = list(map(int, stdin.readline().strip().split()))
    for i, buggys in enumerate(n_buggys):
        fenwick_tree.adjust(i+1, buggys)

    for line in stdin:
        action, i = line.strip().split()
        i = int(i)
        if action == 'a':
            fenwick_tree.adjust(i, -n_buggys[i-1])
            n_buggys[i-1] = 0
        else:
            stdout.write(str(fenwick_tree.rsq(1, i-1))+'\n')
