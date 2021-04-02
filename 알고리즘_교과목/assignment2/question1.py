# [Programming] Write a program that takes a number 𝑛 and displays the largest positive 
# integer 𝑘 satisfying the following equations: 2
# k ≤ 𝑛. Display the results for three different 𝑛’s: 10, 
# 50, and 1025


def power_2(i):
    if i==1 :
        return 2
    return 2*power_2(i-1)

if __name__=='__main__':
    num=int(input('Enter a number : '))
    
    for i in range(1,num): 
        # range를 num으로 범위두는게 유의미하지 않음.. 근데 while문을 쓰기엔 흐음..?
        result = power_2(i)
        if result > num :
            k= i-1
            break
    print("the largerst positive integer k: ",k)
    