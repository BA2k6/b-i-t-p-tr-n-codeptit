import time
start = time.time()
import math
def sieve(n):
    a = [True] * (n + 1)
    a[0] = a[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if a[i]:
            for j in range(i * i, n + 1, i):
                a[j] = False
    return [i for i in range(2, n + 1) if a[i]]
def ck(N):
    n = int(math.sqrt(N))
    primes = sieve(n)
    count = 0
    for p in primes:
        if p ** 8 <= N:
            count += 1

    t= len(primes)
    for i in range(t):
        for j in range(i + 1, t):
            if primes[i] ** 2 * primes[j] ** 2 <= N:
                count += 1
            else:
                break
    return count
v= int(input())
print(ck(v))
print (time.time()-start)

