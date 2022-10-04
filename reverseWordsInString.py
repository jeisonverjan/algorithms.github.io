#https://leetcode.com/problems/reverse-words-in-a-string-iii/

s = "hola sebastian puede ir a jugar?"

r = ''
for word in s.split():
    r += word[::-1] + ' '

print(r.strip())
"""
for i in range(len(s)-1, -1, -1):
    r += s[i]
print(r)
"""
