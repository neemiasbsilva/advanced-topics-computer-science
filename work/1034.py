from sys import stdout, stdin, maxsize

memory = [-1 for i in range(1000000+1)]
def ice_block(m, arr):

    if m == 0: return 0
    elif m < 0: return int(maxsize//2)

    result = int(maxsize//2)

    for i in range(len(arr)):
        result = min(result, ice_block(m - arr[i], arr))

    return 1 + result


def ice_block_dp(m, arr):
    
    if m == 0: return 0
    elif m < 0: return int(maxsize//2)
	
	#Se já computou retorna.
    if memory[m] != -1: return memory[m]
    result = int(maxsize)

    for i in range(len(arr)):
        result = min(result, ice_block_dp(m-arr[i], arr))

    memory[m] = 1 + result
    return 1 + result

if __name__ == "__main__":
   t = int(stdin.readline())
   for i in range(t):
    #    memory = [int(maxsize//2) for i in range(1000000+1)]
       memory = [-1 for i in range(m+1)]
       n, m =  stdin.readline().strip().split()
       n = int(n)
       m = int(m)
       arr = list(map(int, stdin.readline().strip().split()))
       stdout.write(str(ice_block_dp(m, arr))+'\n')
    #    print(ice_block_dp(m, arr))
        # print(ice_block(m, arr))
        # print(bloco(m, arr, 1))

       
