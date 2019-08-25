import time
start = time.time()

def steps(k,cache):
    if k <=1:
        return 1
    if cache[k]!=0:
        return cache[k]
    ways = steps(k-1,cache)+steps(k-2,cache)
    cache[k]= ways
    print(cache)
    return ways

def main():

    N = int(input())
    cache=[0 for i in range(N+1)]
    print (steps(N,cache))

main()

end = time.time()
print(end - start)