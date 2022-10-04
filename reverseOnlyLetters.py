#https://leetcode.com/problems/reverse-only-letters/

s = "ab-cd-dh"
reverse = []
for i, v in enumerate(s):
    if v.isalpha():
        reverse.insert(-i, v)
for i, v in enumerate(s):
    if not v.isalpha():
        reverse.insert(i, v)

result = ''.join(reverse)
print(result)