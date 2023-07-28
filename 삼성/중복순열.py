# n개 중 r개를 뽑는데, 순서 중요 
# Ex. permutation([1,2,3,4],3)


def permutation(arr,r):
    arr=sorted(arr)
    visited = [ False for _ in range(len(arr))]

    def generate(chosen, visited):
        if len(chosen)==r:
            print(chosen)
            return
        
        for i in range(len(arr)):
            # arr[i-1]!=arr[i]는 정렬되어있기 때문에 쓸 수 있음 <- 중복 순열까지 커버 완료
            if not visited[i] and (i==0 or arr[i-1]!=arr[i] or visited[i-1]):
                chosen.append(arr[i])
                visited[i] = True
                generate(chosen,visited)
                visited[i] = False
                chosen.pop()
    generate([],visited)



permutation([1,2,2,4],3)
