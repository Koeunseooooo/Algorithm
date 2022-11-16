from itertools import permutations

def solution(numbers):
    answer = 0
    nums = [n for n in numbers] # numbers 하나씩 자른거
    per=[]
    
    # 소수 : 1보다 큰 자연수 중 1과 자기 자신만을 약수로 가지는 수
    for i in range(1,len(numbers)+1):
        per+= list(permutations(nums,i))
        # p.append(list(permutations(nums,i)))
        # append를 안 쓰면 []를 안쓰고 flat하게 일차원배열로 넘길 수 있음! (처음 암..)
    # print(per)
    new_nums=[int(''.join(p)) for p in per]
    set_nums=set(new_nums)
    print(set_nums)
    
    for s in set_nums:
        if s>=2:
            if isPrime(s):
                answer+=1
            
    return answer

def isPrime(a):
    check=True
    for i in range(2,a):
        if a%i==0:
            check=False
            break
    return check
            