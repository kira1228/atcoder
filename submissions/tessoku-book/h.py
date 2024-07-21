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
H, W = map(int, input().split())
X = [ None ] * (H)
Z = [ [ 0 ] * (W + 1) for i in range(H + 1) ]
for i in range(H):
  X[i] = list(map(int, input().split()))
# 入力（後半）
Q = int(input())
A = [ None ] * Q
B = [ None ] * Q
C = [ None ] * Q
D = [ None ] * Q
for i in range(Q):
  A[i], B[i], C[i], D[i] = map(int, input().split())
# 配列 Z は既に初期化済み
# 横方向に累積和をとる
# X[i-1][j-1] などになっているのは、配列が 0 番目から始まるため
for i in range(1, H+1):
  for j in range(1, W+1):
 