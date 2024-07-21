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
M, D = map(int, input().split())
y, m, d = map(int, input().split())
d += 1
if d > D:
    d = 1
    m += 1
if m > M:
    m = 1
    y += 1
print(y, m, d)