1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
def isPrime(N):
    LIMIT = int(N ** 0.5)
    for i in range(2, LIMIT+1):
        if N % i == 0:
            return False
    return True
N = int(input())
X = [None] * (1000000)
for i in range(2, N + 1):
    if isPrime(i) == True:
        print(i)
    else:
        continue