def compute_inverse_count(puzzle_1d,n):
    inverse_count = 0
    for i in range(n*n-1):
        for j in range(i+1,n*n):
            if puzzle_1d[j] and puzzle_1d[i] and (puzzle_1d[i] > puzzle_1d[j]):
                inverse_count = inverse_count +1
    return inverse_count 

def find_empty_space(puzzle):
    for i in range(4-1,0,-1):
        for j in range(4-1,0,-1):
            if (puzzle[i][j]==0):
                return 4-i
 
def isvalid(puzzle):
    n=len(puzzle)
    inverse_count = compute_inverse_count(puzzle_15_1d,n);
    
    if (n & 1):
        return not(inverse_count & 1);
 
    else:
        pos = find_empty_space(puzzle)
        if (pos & 1):
            return not(inverse_count & 1)
        else:
            return inverse_count & 1

puzzle_15 =[[10,7,3,4],[5,9,0,11],[6,1,2,8,],[13,14,15,12]]
puzzle_15_1d = [10,7,3,4,5,9,0,11,6,1,2,8,13,14,15,12]

print(isvalid(puzzle_15))
