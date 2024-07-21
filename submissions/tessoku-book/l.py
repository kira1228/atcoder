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
# 入力
T = int(input())
N = int(input())
L = [ None ] * N
R = [ None ] * N
for i in range(N):
  L[i], R[i] = map(int, input().split())
# "前の時刻との差" に加算
B = [ 0 ] * (T + 1)
for i in range(N):
  B[L[i]] += 1
  B[R[i]] -= 1
# 累積和をとる
Answer = [ None ] * (T + 1)
Answer[0] = B[0]
for d in range(1, T):
  Answer[d] = Answer[d-1] + B[d]
 