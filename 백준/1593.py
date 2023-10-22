g,s = map(int,input().split())
w=list(input())
s=list(input())

# possible=[]
# for p in permutations(w):
#     possible.append(p) -> 이렇게 하면 메모리 초과가 뜬다.
# 알파벳 개수는 26개이다.. 이것도 모르는 나 .. 님 . .

wl=[0]*52
for i in range(len(w)):
    if ord(w[i]) >=97: # 소문자
        wl[ord(w[i])-97+26]+=1
    elif ord(w[i]) >= 65:  # 대문자
        wl[ord(w[i])-65]+=1



cnt=0
start=0
length=0
sl=[0]*52
for i in range(len(s)):
    if ord(s[i]) >=97: # 소문자
        sl[ord(s[i])-97+26]+=1
    elif ord(s[i]) >= 65:  # 대문자
        sl[ord(s[i])-65]+=1
    length+=1
    if length==g:
        if wl==sl:
            cnt+=1
        if ord(s[start]) >= 97:  # 소문자
            sl[ord(s[start]) - 97 + 26] -= 1
        elif ord(s[start]) >= 65:  # 대문자
            sl[ord(s[start]) - 65] -= 1
        start+=1
        length-=1
print(cnt)
