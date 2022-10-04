# https://leetcode.com/problems/reverse-integer/

x = -460
neg = False
x = str(x)
if x[0] == '-':
    neg = True
    x = x[1:]
x = x[::-1]
x = int(x)
if neg:
    x = -x
print(x)

