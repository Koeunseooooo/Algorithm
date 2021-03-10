#조건 : 입력값은 문자 배열이며, 리턴 "없이" 리스트 내부를 직접 조작하라.

def reverseStr(s) :
    left, right = 0, len(s)-1

    while left < right :
        s[left]=s[right]
        s[right]=s[left]
        left+=1
        right-=1
    print(s)

if __name__=="__main__" :
    a = input("문자열을 입력하세요")
    print(a)
    str = list(a)
    print(str)
    # strToList = []
    # for char in a :
    #     strToList.append(char)
    # print(strToList)
    print("아래는 함수실행 결과 ")
    # reverseStr(strToList)
    reverseStr(str)

