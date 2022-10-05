dict = {"0": 0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7,"8":8, "9":9}
num1 = "1"
num = dict["2"]*10+dict["2"]
result = dict[num1[0]]
for i in range(1, len(num1)):
    temp = result*10+dict[num1[i]]
    result = temp

print(result)
