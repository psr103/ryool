## 전역 변수 선언 부분##
i, k = 0, 0

## 메인 코드 부분##
i = 0
for i in range(0,10,1)  :
    if i < 5 :
        k = 0
        for k in range(k, 4 - i, 1) :
            print(' ', end='')
            
        
        k = 0
        for k in range(k, i * 2 + 1, 1) :
            print('\u2665', end = '')
            
    else:
        k = 0
        for k in range(k, i - 4, 1) :
            print(' ', end = '')
            
        k = 0
        for k in range(k, (9 - i) * 2 - 1, 1) :
            print('\u2665', end = '')
        
    print()
    i += 1