# bubble sort. insertion sort, merge sort, quick sort, radix sort, bucket sort 6개 구현 작성하기 ( 함수 작성 )
# 입력크기 랜덤으로 해서 넣기
# 실행시간 알려주는 함수 찾기 -> 테이블 형태로 출력하기

def bubble_sort(a):
    n=len(a)
    for i in range(n-1):
        for j in range(n-1,i,-1):
            if a[j-1]>a[j]:
                a[j-1], a[j] = a[j], a[j-1]

def insertion_sort(a):
    n=len(a)
    for i in range(1,n):
        j=i
        origin_index = a[i]
        while j>0 and a[j-1] > origin_index:
            a[j]=a[j-1]
            j = j -1 
        a[j]=origin_index

def quick_sort(a, left, right ):
    pl = left
    pr = len(a)-1
    pv = a[(left+right)//2]

    while pl<=pr:
        while a[pl] < pv : pl +=1
        while a[pr] > pv : pr -=1
        if pl <= pr :
            a[pl],a[pr]=a[pr],a[pl]
            pl+=1
            pr-=1
    
    if left < pr :
        quick_sort(a,left,pr)
        quick_sort(a,pl,right)



def merge_sort(a):
    pass

def radix_sort(a):
    pass

def bucket_sort(a):
    pass

if __name__ == "__main__" :
    a=[6,4,3,7,1,9,8]
    bubble_sort(a)
    print(1,a)

    b=[6,4,3,7,1,9,8]
    insertion_sort(b)
    print(2,b)

    c=[6,4,3,7,1,9,8]
    quick_sort(c,0,len(c)-1)
    print(3,c)