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
# aのb乗をmで割ったあまりを返す関数
def Power(a, b, m):
    p = a
    Answer = 1
    for i in range(30):
        wari = 2 ** i
        if (b // wari) % 2 == 1:
            Answer = (Answer * p) % m
        p = (p * p) % m
    return Answer 
# a÷bを m で割った余りを返す関数
def Division(a, b, m):
    return (a * Power(b, m-2, m)) % m
H, W = map(int, input().split())
m = 1000000007
a = 1
 