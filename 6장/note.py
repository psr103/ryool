cCnt, lCnt, nCnt, hCnt, eCnt = 0,0,0,0,0


for c in input("문자열을 입력하세요 :"):
    if c.isupper():
        cCnt += 1
    elif c.islower():
        lCnt += 1
    elif c.isdigit():
        nCnt += 1
    elif c >= '가' and c <= '힣':
        hCnt += 1
    else :
        eCnt += 1

print("대문자: %d 소문자: %d 숫자: %d 한글: %d 기타:%d" % (cCnt, lCnt, nCnt, hCnt, eCnt))
