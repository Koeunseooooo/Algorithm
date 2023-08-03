'''arr = []
for _ in range(9):
    f=int(input())
    arr.append(f)
arr.sort()


sum_ = sum(arr)
fake=[]
# 7번 반복 대신 반대로 생각 9명 합에서 2명을 뺐을때 100 이하인 경우 찾기
for i in range(9):
    for j in range(i+1,9):
        if(len(fake)==2):
            continue
        if sum_-arr[i]-arr[j] ==100:
            fake.append(arr[i])
            fake.append(arr[j])
            #list del method은 코테 풀이할때 가급적 쓰지 말자!

for i in arr:
    if i in fake:
        continue
    print(i)'''


'''2번째 풀이(combination 이용)
# combinations
def combinations(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in combinations(array[i+1:], r-1): # 현재 target 원소 이후만 인덱싱하여 배열 재구성
                yield [array[i]] + next

for i in combinations(arr,7):
    if sum(i) == 100:  # 그합이 100이라면
        for j in sorted(i):  # 그 7명을 오름차순으로 정렬후 출력한다.
            print(j)
        break #그 후 반복문 탈출
'''

#3번째 풀이(dfs)
short_men = [int(input()) for _ in range(9)]
seven_short_temp = []  # 7명을 뽑아 합을 조사할 새로운 리스트 선언


def dfs(depth, start):
    print(seven_short_temp,depth,start)
    if depth == 7:  # 만약 7번 재귀를 돌았다면
        if sum(seven_short_temp) == 100:  # 현재 저장된 일곱난쟁이들의 합이 100이라면
            for j in sorted(seven_short_temp):  # 오름차순으로 정렬 후 출력
                print(j)
            exit()  # 그 후 코드 종료
        else:  # 만약 7명을 뽑았는데 합이 100이 아니라면
            return  # 해당 재귀를 더이상 실행하지 않고 종료

    for i in range(start, len(short_men)):  # 시작인덱스와 9명의 난쟁이가 있으므로 9번을 돈다.
        seven_short_temp.append(short_men[i])  # 난쟁이 한명을 추가한다.
        dfs(depth + 1, i + 1)  # dfs를 돈다(다음번 깊이는 +1로 해주고 인덱스는 중복되지 않게 하기위해서 다음 인덱스를 넣어준다.)
        seven_short_temp.pop()  # dfs를 돌다 7명이 다 찼으나 합이 100이 아니어서 return 되었으면 넣었던 난쟁이 한명을 다시 빼준다.


dfs(0, 0)  # dfs를 돈다.
#'''


