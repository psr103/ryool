## 문자열을 입력받는다. ##
ss = input("입력 문자열 ==> ")
print("출력 문자열 ==> ", end= '')

## if 조건문으로 문자열이 (로 시작하지 않을시 (를 출력하도록 한다. ##
if ss.startswith('(') == False :
    print("(", end = '')

## 지정된 문자열을 출력한다. ##
print(ss, end = '')


## if 조건문으로 문자열이 )로 끝나지 않을시 )를 출력하도록 한다. ##
if ss.endswith(')') == False :
    print(")", end = '')