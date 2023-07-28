# n개 중 r개를 뽑는데, 순서 중요X 
# Ex. combination([1,2,3,4],3)


def combination(arr,r):
    arr=sorted(arr)
    used = [0 for _ in range(len(arr))]

    def generate(chosen):
        if len(chosen)==r:
            print(chosen)
            return
        
        start=arr.index(chosen[-1])+1 if chosen else 0
        for i in range(start,len(arr)):
            # arr[i-1]!=arr[i]는 정렬되어있기 때문에 쓸 수 있음 <- 중복 순열까지 커버 완료
            if used[i]==0 and (i==0 or arr[i-1]!=arr[i] or used[i-1]):
                chosen.append(arr[i])
                used[i]=1
                generate(chosen)
                chosen.pop()
                used[i] = 0
    generate([])



combination([1,2,2,4],3)
