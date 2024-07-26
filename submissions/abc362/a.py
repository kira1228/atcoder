1
2
3
4
5
6
7
8
9
R, G, B = map(int, input().split())
C = str(input())
if C == "Red":
    print(min(G, B))
elif C == "Green":
    print(min(R, B))
else:
    print(min(R, G))