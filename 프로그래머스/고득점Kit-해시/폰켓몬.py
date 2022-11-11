def solution(nums):
    c_num=len(nums)//2
    answer = 0
    result={}
    for i in nums: #초기화
        result[i]=0
    
    for i in nums: #키 값 별 개수 누적
        result[i]+=1
    
    while(True):
        for k in result:
            if c_num == answer:
                break
            if result[k]!=0:
                result[k]-=1
                answer+=1
                print(result[k])
        break
    return answer