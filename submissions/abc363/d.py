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
def nth_palindrome(n):
    # 1桁の回文数（1から9まで）
    if n < 10:
        return n
        # 2桁以上の回文数
    count = 9
    length = 1
        # 桁数を増やしながらn番目の回文数を探す
    while True:
        length += 1
        half_length = (length + 1) // 2
        palindromes_in_length = 9 * (10 ** (half_length - 1))
                if n <= count + palindromes_in_length:
            break
                count += palindromes_in_length
     