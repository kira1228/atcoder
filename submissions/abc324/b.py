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
n = int(input())
s = set()
for i in range(1, 10):
    for j in range(1, 10):
        k = i*j
        s.add(k)
if n in s:
    print('Yes')
else:
    print('No')
    