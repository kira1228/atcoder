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
17
18
19
n = int(input())
l = []
for i in range(n):
    A, B, C, D = map(int , input().split())
    l.append([A, B, C, D])
s = 0
for x in range(1, 101):
    for y in range(1, 101):
        for A, B, C, D in l:
            if (A < x - 0.5 < B and C < y - 0.5 < D):
                s += 1
                break
print(s)