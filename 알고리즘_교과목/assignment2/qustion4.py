# [Programming] Given an image represented by a 5 × 5 matrix, write a method to rotate the 
# image by 90 degrees (clockwise). You can generate a matrix randomly.

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
    print("Input 5*5 matrix's values : ")
    for _ in range(5):
        original.append(list(map(int, input().split())))
    
    print("90 degrees rotated matrix : ")
    rotated = rotate_90(original)
    for row in rotated:
        print(row)

