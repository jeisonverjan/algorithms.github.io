class Solution:
    def isPalindrome(self, s: str) -> bool:

        result = ''
        if s == ' ':
            return True

        for char in s:
            if char.isalnum():
                result += char.lower()

        return result == result[::-1]
