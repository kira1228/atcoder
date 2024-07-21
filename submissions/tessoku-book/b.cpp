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
def f(x):
    return x*x*x + x
N = int(input())
L = 0
R = 100
for i in range(20):
    Mid = (L + R) / 2
    val = f(Mid)
    if val > N:
        R = Mid
    else:
        L = Mid
print(Mid)