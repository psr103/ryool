hap = 0

num1 = int(input("시작값을 입력하세요: "))
num2 = int(input("끝값을 입력하세요: "))
num3 = int(input("증가값을 입력하세요 "))

i= num1



while i < num2 + 1 :
    hap = hap + i
    i = i + num3

print("%d부터 %d까지의 합계: %d" %(num1, num2, hap))
