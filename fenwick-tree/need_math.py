from sys import stdin, stdout

if __name__ == "__main__":
    
    n = int(stdin.readline())
    n_buggys = list(map(int, stdin.readline().strip().split()))

    for line in stdin:
        action, i = line.strip().split()
        i = int(i)

        if action == 'a':
            n_buggys[i-1] = 0
        else:
            stdout.write(str(sum(n_buggys[:i-1]))+'\n')

