#https://leetcode.com/problems/next-greater-element-i/

nums1 = [1,3,5,2,4]
nums2 = [6,5,4,3,2,1,7]
result = []
stack = {}

for i, v in enumerate(nums2):
    stack[v] = i + 1
print(stack)

for v in nums1:
    flag = True
    for j in nums2[stack[v]:]:
        if j > v:
            result.append(j)
            flag = False
            break
    if flag:
        result.append(-1)

print(result)