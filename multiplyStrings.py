#https://leetcode.com/problems/multiply-strings/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if num1 == "0" or num2 == "0":
            return "0"

        dict = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

        def convert_to_int(string):
            result = dict[string[0]]
            for i in range(1, len(string)):
                temp = result * 10 + dict[string[i]]
                result = temp
            return result

        return str(convert_to_int(num1) * convert_to_int(num2))