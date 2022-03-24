# 하루는 24*60*60으로, 모든 경우의 수가 86400가지 밖에 존재하지 않음. 
# 즉, 경우의 수가 100000개도 되지 않으므로 파이썬에서의 문자열 연산을 이용해 확인해도 무방.
# 이러한 유형은 완전탐색 유형. 보통 데이터의 개수가 100만개 이하일 떄 유용하다.

n=int(input())
cnt=0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                cnt+=1

print(cnt)
