# bubble sort. insertion sort, merge sort, quick sort, radix sort, bucket sort 6개 구현 작성하기 ( 함수 작성 )
# 입력크기 랜덤으로 해서 넣기
# 실행시간 알려주는 함수 찾기 -> 테이블 형태로 출력하기

import datetime
def bubble_sort(a):
    n=len(a)
    for i in range(n-1):
        for j in range(n-1,i,-1):
            if a[j-1]>a[j]:
                a[j-1], a[j] = a[j], a[j-1]
    return a


def insertion_sort(a):
    n=len(a)
    for i in range(1,n):
        j=i
        origin_index = a[i]
        while j>0 and a[j-1] > origin_index:
            a[j]=a[j-1]
            j = j -1 
        a[j]=origin_index
    return a


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

    return a

def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    leftList = a[:mid]
    rightList = a[mid:]
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)
    return merge(leftList, rightList)


def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result


def counting_sort(arr, digit):
    n = len(arr)
  
    # 배열의 크기에 맞는 output 배열을 생성하고 10개의 0을 가진 count란 배열을 생성한다. 
    output = [0] * (n)
    count = [0] * (10)
    
    #digit, 자릿수에 맞는 count에 += 1을 한다. 
    for i in range(0, n):
        index = int(arr[i]/digit) 
        count[ (index)%10 ] += 1
 
    # count 배열을 수정해 digit으로 잡은 포지션을 설정한다.  
    for i in range(1,10):
        count[i] += count[i-1]  
    # 결과 배열, output을 설정한다. 설정된 count 배열에 맞는 부분에 arr원소를 담는다.   
    i = n - 1
    while i >= 0:
        index = int(arr[i]/digit)
        output[ count[ (index)%10 ] - 1] = arr[i]
        count[ (index)%10 ] -= 1
        i -= 1

    #arr를 결과물에 다시 재할당한다.  
    for i in range(0,len(arr)): 
        arr[i] = output[i]
 

def radix_sort(a):
    # arr 배열중에서 maxValue를 잡아서 어느 digit, 자릿수까지 반복하면 될지를 정한다. 
    maxValue = max(a)  
    #자릿수마다 countingSorting을 시작한다. 
    digit = 1
    while int(maxValue/digit) > 0: 
        counting_sort(a,digit)
        digit *= 10
    return a

def bucket_sort(array, num_buckets):
    if type(array) != list or type(num_buckets) != int:
        return "Input to sort must be list, and number of buckets must be list"
    if len(array) < 2:
        return array

    buckets = []
    for i in range(num_buckets):
        buckets.append([])
    #buckets will be a list of lists. The number of elements in buckets will
    #be the number of buckets the user specified
    bucketnum = 0
    for i in array:
        buckets[bucketnum].append(i)
        bucketnum += 1
        if bucketnum == num_buckets:
            bucketnum = 0

    for i in range(len(buckets)):
        buckets[i] = insertion_sort(buckets[i])

    combined_array = []
    for i in range(num_buckets):
        for element in buckets[i]:
            combined_array.append(element)

    combined_array = insertion_sort(combined_array)

    return combined_array

def inputN(input_size):
    input_list=[]
    for i in range(input_size,0,-1):
        input_list.append(i)
    return input_list


if __name__ == "__main__" :

    print(" Executing Time")
    print("                | bubble sort | insertion sort | quick sort | merge sort | radix sort | bucket sort |")
    print(" n = 100        | ")
    print(" n = 1000       | ")
    print(" n = 10000      | ")

    # N = 100 
    print("N=100")
    start_time = datetime.datetime.now()
    bubble_sort(inputN(100))
    end_time = datetime.datetime.now()
    bubble_exe_time =( end_time - start_time ).microseconds
    print(bubble_exe_time)

    start_time = datetime.datetime.now()
    insertion_sort(inputN(100))
    end_time = datetime.datetime.now()
    insertion_exe_time =( end_time - start_time ).microseconds
    print(insertion_exe_time)


    start_time = datetime.datetime.now()
    quick_sort(inputN(100),0,len(inputN(100))-1)
    end_time = datetime.datetime.now()
    quick_exe_time =( end_time - start_time ).microseconds
    print(quick_exe_time)
    
    start_time = datetime.datetime.now()
    merge_sort(inputN(100))
    end_time = datetime.datetime.now()
    merge_exe_time =( end_time - start_time ).microseconds
    print(merge_exe_time)

    start_time = datetime.datetime.now()
    radix_sort(inputN(100))
    end_time = datetime.datetime.now()
    radix_exe_time =( end_time - start_time ).microseconds
    print(radix_exe_time)
    
    start_time = datetime.datetime.now()
    bucket_sort(inputN(100),10)
    end_time = datetime.datetime.now()
    bucket_exe_time =( end_time - start_time ).microseconds
    print(bucket_exe_time)

    # N = 1000
    print("N=1000")
    start_time = datetime.datetime.now()
    bubble_sort(inputN(1000))
    end_time = datetime.datetime.now()
    bubble_exe_time =( end_time - start_time ).microseconds
    print(bubble_exe_time)

    start_time = datetime.datetime.now()
    insertion_sort(inputN(1000))
    end_time = datetime.datetime.now()
    insertion_exe_time =( end_time - start_time ).microseconds
    print(insertion_exe_time)


    start_time = datetime.datetime.now()
    quick_sort(inputN(1000),0,len(inputN(1000))-1)
    end_time = datetime.datetime.now()
    quick_exe_time =( end_time - start_time ).microseconds
    print(quick_exe_time)
    
    start_time = datetime.datetime.now()
    merge_sort(inputN(1000))
    end_time = datetime.datetime.now()
    merge_exe_time =( end_time - start_time ).microseconds
    print(merge_exe_time)

    start_time = datetime.datetime.now()
    radix_sort(inputN(1000))
    end_time = datetime.datetime.now()
    radix_exe_time =( end_time - start_time ).microseconds
    print(radix_exe_time)
    
    start_time = datetime.datetime.now()
    bucket_sort(inputN(1000),20)
    end_time = datetime.datetime.now()
    bucket_exe_time =( end_time - start_time ).microseconds
    print(bucket_exe_time)

    # N = 10000
    print("N=10000")
    start_time = datetime.datetime.now()
    bubble_sort(inputN(10000))
    end_time = datetime.datetime.now()
    bubble_exe_time =( end_time - start_time ).microseconds
    print(bubble_exe_time)

    start_time = datetime.datetime.now()
    insertion_sort(inputN(10000))
    end_time = datetime.datetime.now()
    insertion_exe_time =( end_time - start_time ).microseconds
    print(insertion_exe_time)


    start_time = datetime.datetime.now()
    quick_sort(inputN(10000),0,len(inputN(10000))-1)
    end_time = datetime.datetime.now()
    quick_exe_time =( end_time - start_time ).microseconds
    print(quick_exe_time)
    
    start_time = datetime.datetime.now()
    merge_sort(inputN(10000))
    end_time = datetime.datetime.now()
    merge_exe_time =( end_time - start_time ).microseconds
    print(merge_exe_time)

    start_time = datetime.datetime.now()
    radix_sort(inputN(10000))
    end_time = datetime.datetime.now()
    radix_exe_time =( end_time - start_time ).microseconds
    print(radix_exe_time)
    
    start_time = datetime.datetime.now()
    bucket_sort(inputN(10000),50)
    end_time = datetime.datetime.now()
    bucket_exe_time =( end_time - start_time ).microseconds
    print(bucket_exe_time)