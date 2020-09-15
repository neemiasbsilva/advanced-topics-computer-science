from sys import stdin, stdout

LSOne = lambda b: b&(-b)


class FenwickTree:

    def __init__ (self, n):
        self.ft = [0 for i in range(n+1)]

    def rsq_util(self, b): # return RSQ(1,b)
        s = 0
        while b > 0:
            s += 1 
            # self.ft[b]
            b -= LSOne(b)
        return s

    def rsq(self, a, b):
        return self.rsq_util(b) - (0 if a == 1 else self.rsq_util(a-1))

    def adjust(self, k, v):
        
        while k < len(self.ft):
            self.ft[k] += v
            k += LSOne(v)

if __name__ == "__main__":

    while True:
        ip, m = list(map(int, stdin.readline().strip().split()))
        if ip == '':
            break
        count = 0
        l_pc = []
        l_na = []
        for i in range(m):
            pc, na = list(map(int, stdin.readline().strip().split()))
            l_pc.append(pc)
            l_na.append(na)

        size = max(l_pc)
        
        fenwick_tree = FenwickTree(size)
        for pc, na in zip(l_pc, l_na):
            pcmax = size if pc+ip > size else pc+ip
            pcmin = 0 if pc-ip <= 0 else pc-ip
            if -1 < fenwick_tree.rsq(pcmin, pcmax) <= na:
                count += 1
                fenwick_tree.adjust(i+1, pc)
            # Brute force    
            # if len(l):
            #     length = 0
            #     for j in l:
            #         if pc-ip < j <= pc+ip:
            #             length += 1
            #     if length > 0 and length <= na:
            #         l.append(pc)
            # else:
            #     l.append(pc)
        stdout.write(str(count)+'\n')

