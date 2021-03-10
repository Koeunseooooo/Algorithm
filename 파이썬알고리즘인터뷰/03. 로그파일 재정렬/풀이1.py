# 리트코드 937번 문제 

# 로그 재정렬의 기준
# 1. 로그의 가장 앞 부분은 식별자다
# 2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다. => letters+digits 순
# 3. 식별자는 순서에 영향을 끼치지 않지만 문자가 동일할 경우 식별자 순으로 한다. # 정렬 로직 새로 짜야함 !
# 4. 숫자 로그는 입력 순서대로 한다 => digit에 넣고 그대로 별도의 정렬없이 return해주면 된다는 소리

def sortLogFile(a : list) :
    digits=[]
    letters=[]
    for element in a :
        if element.split()[1].isdigit():
            digits.append(element)
        else : # 문자로 구성된 로그
            letters.append(element)

    # 3번 조건은 단순 오름,내림차가 아닌 특정한 조건이다.
    # 특정조건에 대하여 sort()의 파라미터에 원하는 정렬 조건을 key로 정의하면 됨
    letters.sort(key=lambda x:(x.split()[1:], x.split()[0]))
    # x.split()[1:]의 의미는 식별자를 제외한 문자들을 다 붙여서 생각했을때 정렬을 해!
    # 모두모두 문자가 동일한 경우에는! x.split()[0] 즉, 식별자 순으로 한당
    print(letters+digits)
    return letters + digits # 조건 2에 맞게 문자 -> 숫자 순으로 정렬 

if __name__=="__main__":
    logs=[]
    logs=input("로그를 여러개 입력해보세요~로그는 콤마로 구분된답니당").split(",")
    sortLogFile(logs)

    # 완-벽