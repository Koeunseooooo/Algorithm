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
        else :
            letters.append(element)
    

    #