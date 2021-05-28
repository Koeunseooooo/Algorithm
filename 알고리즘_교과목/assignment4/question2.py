import random
import numpy as np
import math

def create_random_array(row,col):
    return np.array([[random.randint(0,100) for col in range(col)] for row in range(row)])

def matrix_chain_order(p, n):
    # m 행렬을 먼저 0으로 초기화 한다
    m = [ [0 for i in range(n)] for i in range (n)]
    
    for len in range (2, n + 1):
        for i in range (n - len + 1):
            j = i + len - 1
            # dp 점화식을 그대로 코드화한다.
            m[i][j] = math.inf
            for k in range (i, j):
                q = (m[i][k] + m[k + 1][j] + (p[i] * p[k + 1] * p[j + 1]));
                if (q < m[i][j]): # min(q,min[i][j])
                    m[i][j] = q
                    # 저장은 인덱스를 바꾸어 마무리 한다!
                    m[j][i] = k + 1
    return m;

def optimal_chain_order(m, j, i ):
    # 이어져서 출력되어야 하므로 출력문 옵션에 end="" 모두 달아줌
    if j == i:
        # optimal한 chain order를 직관적으로 나타내기 위해 아스키코드 사용하려 행렬의 이름을 붙여준다.
        print(chr(65 + j), end = "")
        return;
    else:
        print("(", end = "")
        # (를 기준으로 쪼개진 각각의 수식을 다시 재쉬적으로 optimal_chain_order를 호출한다.
        optimal_chain_order(m, m[j][i] - 1, i)
        optimal_chain_order(m, j, m[j][i])
        print (")", end = "" )
 
if __name__ == '__main__':
    dim = [5,3,7,10]
    n = len(dim) - 1
    # 5×3행렬(A), 3×7행렬(B), 7x10행렬(C) 랜덤 생성
    A=create_random_array(5,3)
    print(A)
    B=create_random_array(3,7)
    print(B)
    C=create_random_array(7,10)
    print(C)

    print("output matrix is : ")
    output_matrix = (A.dot(B)).dot(C)
    print(output_matrix)
    print("output matrix of size is :",np.shape(output_matrix))

    m = matrix_chain_order(dim, n) # m행렬 저장
    
    print("Optimal chain order is : ", end = "")

    optimal_chain_order(m, n - 1, 0) # 계산해야 하는 순서대로 optimal_chain_order 나타내기
    
    print("\nMinimum number of computations is :", m[0][n - 1]) #최적의 계산은 m[0][n-1] 에 담겨져있다.
    