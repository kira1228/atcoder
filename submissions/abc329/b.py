1
2
3
4
5
6
n = int(input())
s = set(map(int, input().split()))
s.remove(max(s))
print(max(s))