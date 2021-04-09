# [Programming] Given an image represented by a 5 × 5 matrix, write a method to rotate the 
# image by 90 degrees (clockwise). You can generate a matrix randomly.

import random
def rotate_90(m):
    n = len(m)
    ret = [[0] * n for x in range(n)]
    # 왜 'ret = [[0] * N] * N'과 같이 하지 않는지 헷갈리시면 연락주세요.

    for r in range(n):
        for c in range(n):
            ret[c][n-1-r] = m[r][c]
    return ret

if __name__=='__main__':
    original = []
    row =[]
    for x in range(5):
        for y in range(5):
            row.append(random.randint(1,25))
        original.append(row)
        row=[]

    print("randomly generated matrix(5*5) : ")
    for row in original:
        print(row)
    
    print("\n")
    
    print("90 degrees rotated matrix : ")
    rotated = rotate_90(original)
    for row in rotated:
        print(row)

