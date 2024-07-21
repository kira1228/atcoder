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
def GCD(A, B):
    while A >= 1 and B >=1:
        if A >= B:
            A = A % B
        else:
            B = B % A
    if A >= 1:
        return A
    return B
            A, B = map(int, input().split())
LCM = int((A*B) // GCD(A, B))
print(LCM)