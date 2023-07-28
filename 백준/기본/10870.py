n = int(input())

arr=[]
for i in range(n+1):
    if i ==0 or i ==1:
        arr.append(i)
    else :
        arr.append(arr[i-1]+arr[i-2])
print(arr[-1])

# 피보나치 다르게 푸는 법?