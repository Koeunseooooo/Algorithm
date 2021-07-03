if __name__=="__main__":
    belt_num,dishes,cont,coupon=map(int,input().split())
    belt=[]
    for _ in range(belt_num):
        belt.append(int(input()))
    left_pointer=0
    right_pointer=left_pointer+cont-1
    
    branch=1
    for i in range(belt_num):
        count=1
        temp_branch=[coupon,]
        for _ in range(cont):
            if belt[right_pointer%belt_num] not in temp_branch:
                temp_branch.append(belt[right_pointer%belt_num])
                count+=1

            right_pointer-=1

        branch = max(count, branch)
        left_pointer+=1
        right_pointer=left_pointer+cont-1

    print(branch)
            


        


    

