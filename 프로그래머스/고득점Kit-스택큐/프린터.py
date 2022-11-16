def solution(priorities, location):
    arr=[[i,p] for i,p in enumerate(priorities)]
    answer=0
    while True:
        tar=arr.pop(0)
        if all(tar[1]>=i[1] for i in arr): #가장 큰 수일 경우
            answer+=1
            if tar[0]==location:
                return answer
        else:
            arr.append(tar)
    