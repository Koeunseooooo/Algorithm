def reverseStr(s) :
    print(s.reverse())  #None
    # print문을 찍어도 None이 나오는 이유 : 역순으로 정렬해주는 '기능'만 제공, 반환값을 제공하지 않음
    # 출력해보고 싶다면 아래와 같이 써야함
    print(s) #["o","l","l","e","h"]
 
if __name__=="__main__" :
    a=input("문자열을 입력하세요")
    b=list(a)
    print(b)
    reverseStr(b)
