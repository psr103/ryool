## 입력받을 문자열과 출력할 문자열 함수를 선언해준다. ##
inStr = '<<파<<이>>썬>>'
outStr= ''

## len을 사용하여 inStr 문자열의 자릿수를 추출하고, if를 사용해 해당 자릿수가 '<'나, '>'가 ##
## 아닐시에, outStr의 빈 문자열에 차곡차곡 기록되도록 한다. ## 
for i in range(0, len(inStr)) :
    if inStr[i] != '<' and  inStr[i] != '>' :
        outStr += inStr[i]

## inStr[0], inStr[1], inStr[3], inStr[4], inStr[7], inStr[8], inStr[10], inStr[11] ##
## 는 '<' 또는 '>'이므로 outStr 문자열에 추가되지 않았다. ##
## 그러므로 outStr을 출력하면 '파이썬'이 출력될 것이다.##
print("원래 문자열 ==>" + inStr)
print("특수문자 삭제 문자열 ==> " + outStr)