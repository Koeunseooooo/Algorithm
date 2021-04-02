# [Programming] Write a function to find all pairs of an integer array whose sum is equal to a 
# given number.
# Function: pairSum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7)
# Output: [‘2+5’, ‘4+3’, ‘3+4’, ‘-2+9’]

def pairSum(num_list,num):
    list_len=len(num_list)
    output_list=[]
    for i in range(0,list_len) :
        for j in range(i+1,list_len) :
            if num_list[i]+num_list[j]==7 :
                output_list.append(str(num_list[i])+'+'+str(num_list[j]))
    return output_list



if __name__ == "__main__" :
    num_list = list(map(int, input("Enter a list: ").split()))
    num = int(input("Enter a number: "))
    print("Output :" ,pairSum(num_list,num))