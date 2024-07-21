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
# 入力（前半）
N = int(input())
X = [ None ] * N
Y = [ None ] * N
for i in range(N):
  X[i], Y[i] = map(int, input().split())
# 入力（後半）
Q = int(input())
A = [ None ] * Q
B = [ None ] * Q
C = [ None ] * Q
D = [ None ] * Q
for i in range(Q):
  A[i], B[i], C[i], D[i] = map(int, input().split())
# 各座標にある点の数を数える
S = [ [ 0 ] * 1501 for i in range(1501) ]
for i in range(N):
  S[X[i]][Y[i]] += 1
 