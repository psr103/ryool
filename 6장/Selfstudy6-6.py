i, hap = 0, 0

while i < 101:
    i = i + 1
    hap = hap +i

    if hap >= 1000:
        break

print("1~100의 합계를 최초로 1000이 넘게 하는 숫자: %d" %i)