import math

myData = [int(math.pow(2, num)) for num in range(0, 5) if num % 2 != 0]

print(myData)