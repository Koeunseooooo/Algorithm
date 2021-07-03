if __name__=="__main__":
    belt_num,dishes,cont,coupon=map(int,input().split())
    belt=[]
    for _ in range(belt_num):
        belt.append(int(input()))
    left_pointer=0
    right_pointer=left_pointer+cont-1
    
    branch=[]
    
    while(left_pointer<=len(belt)-1):
        temp_branch=[coupon,]
        for i in range(cont):
            if right_pointer < 0:
                right_pointer=len(belt)-1

            if(right_pointer>len(belt)-1):
                right_pointer=right_pointer%8

            if belt[right_pointer] not in temp_branch:
                temp_branch.append(belt[right_pointer])

            right_pointer-=1

        branch.append(len(temp_branch))
        left_pointer+=1
        right_pointer=left_pointer+cont-1

    print(max(branch))
            


        


    

