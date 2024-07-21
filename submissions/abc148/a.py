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
n, s, k = list(map(int, input().split()))
total = 0
for i in range(n):
    p, q = map(int, input().split())
    total += p*q
if (total < s):
    total += k
    print(total)
    else:
    print(total)