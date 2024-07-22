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
N, K = map(int, input().split())
S = str(input())
ON = 0
for i in range(len(S)):
    if S[i] == "1":
        ON += 1
if abs(ON - K) % 2 == 0:
    print("Yes")
else:
    print("No")