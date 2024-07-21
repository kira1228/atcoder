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
N = int(input())
h = [0] + list(map(int, input().split()))
dp = [0] * (N + 1)
dp[1] = 0
if N > 1:
    dp[2] = abs(h[2] - h[1])
for i in range(3, N + 1):
    dp[i] = min(dp[i-1] + abs(h[i-1] - h[i]), dp[i-2] + abs(h[i-2] - h[i]))
# restoration
Answer = []
Place = N
while True:
    Answer.append(Place)
    if Place == 1:
 