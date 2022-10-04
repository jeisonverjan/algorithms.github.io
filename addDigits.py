#https://leetcode.com/problems/add-digits/
num = 23456

# basic case
if num < 10:
    print(num)

while num > 9:
    total = 0
    for digit in str(num):
        total += int(digit)
    num = total
print(num)




