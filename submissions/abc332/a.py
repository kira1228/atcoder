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
n, m = map(int, input().split())
s = str(input())
t = str(input())
if (str(t[:n]) == s and str(t[-n:]) == s):
    print(0)
elif (str(t[:n]) == s and str(t[-n:]) != s):
    print(1)
elif (str(t[:n]) != s and str(t[-n:]) == s):
    print(2)
else:
    print(3)