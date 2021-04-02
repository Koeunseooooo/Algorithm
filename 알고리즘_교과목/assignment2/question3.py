# [Programming] Write a program that search for the integer 120 in the following list of integers
# using the binary search algorithm.

def BSearch(a, target, low, high) :
    if low > high :
        return -1
    mid= (low+high)//2
    # 나눗셈 몫만 알고싶다면 /가 아니라 //까지 붙이기 
    if a[mid]==target:
        return mid
    elif a[mid] > target:
        return BSearch(a,target,low,mid-1)
    else :
        return BSearch(a,target,mid+1,high)
 
if __name__=='__main__':
    a=[12,34,37,45,57,82,99,120,134]
    low=0
    high=len(a)-1
    result = BSearch(a,120,low,high)
    print("Index stored 120 is",result)
