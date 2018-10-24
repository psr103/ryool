## 입력받을 문자열과 출력할 문자열 함수는 선언해준다. ##
inStr = " 한글 Python 프로그래밍 "
outStr= ""

## len을 사용하여 inStr 문자열의 자릿수를 추출하고, if를 사용해 해당 자릿수가 공백이 ##
## 아닐시에, outStr의 빈 문자열에 차곡차곡 기록되도록 한다. ## 
for i in range(0, len(inStr)) :
    if inStr[i] != ' ' :
        outStr += inStr[i]

## inStr[0], inStr[3], inStr[10], inStr[16] 은 공백이므로 outStr 문자열에 추가되지 않았다. ##
## 그러므로 outStr을 출력하면 '[한글python프로그래밍]'이 출력될 것이다.##
print("원래 문자열 ==> "+'[' + inStr + ']')
print("공백 삭제 문자열 ==> " + '[' + outStr + ']')