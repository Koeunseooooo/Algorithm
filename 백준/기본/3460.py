t=int(input())

n_arr=[]
for _ in range(t):
    n_arr.append(int(input()))

# 2진수 리스트 - binary list (b)
# print() 공부하기
for n in n_arr:
    b = []
    while(n>1):
        r=n%2
        n=n//2
        b.append(r)
    b.append(1)
    for i in range(len(b)):
        if b[i]==1:
            print(i, end=' ')
    print()
