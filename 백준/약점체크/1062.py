from itertools import combinations
import sys

input = sys.stdin.readline 
n, k = map(int, input().strip().split())

def solve(n, k):
    required={'a','n','t','i','c'}
    uniqueList=[]
    # 빈 집합을 만들 때엔 {}대신 set()을 사용. {} 사용 시 딕셔너리가 생성됨 주의
    uniqueSet=set()
    cnt=0
    for _ in range (n):
        cur = input().strip()
        curSet =set(cur)
        curSetLen =len(curSet)
        # print(curSetLen)s
        # 절대 읽을 수 없는 경우는 아예 배제
        if curSetLen > k:
            continue
        # 무조건 읽는 경우
        if curSetLen == 5:
            cnt += 1
            continue
        # 단어를 구성하는 unique한 글자(중복x) 뽑기 (set활용)
        curUnique = curSet-required
        uniqueList.append(curUnique)
        # update와 unique 차이 잘 알고 쓸 것 (..)
        uniqueSet.update(curUnique)


    # required 글자는 단어 내에 필수로 들어가므로 최소 5개의 글자를 배워야 하는데 k 자체가 5 미만이라면 그 자리에서 종료
    if k<5:
        return 0


    # K는 5보다 크거나 같은데, 주어진 words는 모두 a,n,t,i,c 5개 알파벳으로만 이루어진 경우 아래 과정 반복할 필요 없으므로 그 자리에서 종료
    if len(uniqueList) == 0:
        return cnt
            

    # antic 외에 K-5개 이하로 알파벳을 사용해도 모든 단어를 다 읽을 수 있는 경우 아래 과정 반복할 필요 없으므로 그 자리에서 종료
    if len(uniqueSet) <= k-5 :
       print(1)
       return cnt + len(uniqueList)

    maxCnt=0

    # {'a','n','t','i','c'}를 제외한 단어 속 unique한 글자들 중 k-5개의 글자를 고를 것임.
    # 이 때, 어떤 조합으로 골라야 가장 많은 단어를 읽을 수 있는지 combinations를 통해 brute-force 진행
    for c in combinations(uniqueSet,k-5):
        caseSet = set(c)
        tmpAns = 0
        for uniqueWord in uniqueList:
            if caseSet.issuperset(uniqueWord): # 또는 uniqueWord.issubset(caseSet)
                tmpAns+=1
        maxCnt=max(maxCnt,tmpAns)

    cnt += maxCnt
    return cnt

print(solve(n,k))


