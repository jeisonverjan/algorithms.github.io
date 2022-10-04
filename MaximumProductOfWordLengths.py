words = ["a","aa","aaa","aaaa"]
max_pro = 0

def have_common_char(str1, str2):
    for char in str1:
        if char in str2:
            return True
    return False

for i in range(len(words)):
    for j in range(i+1, len(words)):
        if not have_common_char(words[i], words[j]):
            tem_prod = len(words[i]) * len(words[j])
            if tem_prod > max_pro:
                max_pro = tem_prod

print(max_pro)
