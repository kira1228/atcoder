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
20
import sys
N, S = map(int, input().split())
A = list(map(int, input().split()))
dp = [[None] * (S+1) for i in range(N+1)]
dp[0][0] = True
for i in range(1, S+1):
    dp[0][i] = False
for i in range(1, N+1):
    for j in range(0, S+1):
        if j < A[i-1]:
            if dp[i-1][j] == True:
                dp[i][j] = True
            else:
                dp[i][j] = False
                    if j >= A[i-1]:
 