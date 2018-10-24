inStr = 'It CookBook 1234 파이썬'
outStr = ''

print("문자열 --> %s"%inStr)
print("숫자 제거--> ", end = '')
for i in range(0, len(inStr)):
    if  inStr[i].isalpha() :
        outStr += inStr[i]
    elif inStr[i].isspace() :
        outStr += ' '
    else :
        None
print(outStr)
    