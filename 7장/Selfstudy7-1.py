aa = []
hap = 0

for i in range(0,10):
    aa.append(i)

for i in range(0,10):
    aa[i] = int(input(str(i+1)+"번 째 숫자 : "))

for i in range(0,10):
    hap += aa[i]

print("합계 => %d" %hap)
    