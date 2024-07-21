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
N = int(input())
A3 = N // 3
A5 = N // 5
A7 = N // 7
A15 = N // 15
A35 = N // 35
A21 = N // 21
A105 = N // 105
nums = A3 + A5 + A7 - A15 - A35 - A21 + A105
print(nums)