student1 = {'학번' : 1000, '이름' : '홍길동', '학과' : '컴퓨터학과'}
print(student1)

student1['연락처'] = '010-4382-1020'

print(student1)

student1['학과'] = '영문학과'

print(student1)

del(student1['학과'])

print(student1)

print(student1['학번'])
print(student1['이름'])
print(student1['연락처'])

print(student1.get('이름'))

print(student1.get('주소'))

student1.key()