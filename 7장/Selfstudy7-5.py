animal = {"닭" : "병아리",
          "개" : "강아지",
          "곰" : "능소니",
          "고등어" : "고등어새끼",
          "명태" : "노가리",
          "호랑이" : "개호주"};

while (True):
    animalbabe = input(str(list(animal.keys()))+ "중 새끼 이름을 알고 싶은 동물은?")
    if animalbabe in animal :
        print("<%s>의 새끼 이름은 <%s> 입니다." %(animalbabe,animal.get(animalbabe)))
    elif animalbabe == "끝":
        break
    else :
        print("그런 동물이 없습니다. 확인해 보세요.")