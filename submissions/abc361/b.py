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
a, b, c, d, e, f = map(int, input().split())
g, h, i, j, k, l = map(int, input().split())
def has_intersection(a, b, c, d, e, f, g, h, i, j, k, l):
    # 直方体の範囲を正規化
    x1, x2 = min(a, d), max(a, d)
    y1, y2 = min(b, e), max(b, e)
    z1, z2 = min(c, f), max(c, f)
        x3, x4 = min(g, j), max(g, j)
    y3, y4 = min(h, k), max(h, k)
    z3, z4 = min(i, l), max(i, l)
        # 共通部分の範囲を求める
    x_min, x_max = max(x1, x3), min(x2, x4)
    y_min, y_max = max(y1, y3), min(y2, y4)
    z_min, z_max = max(z1, z3), min(z2, z4)
        # 共通部分の存在を確認する
 