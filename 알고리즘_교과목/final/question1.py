X=['A','B','C','B','D','A','B']
Y=['B','D','C','A','B','A']

def lsc_length(X,Y):
    
    m=len(X)
    n=len(Y)

    b = [[0 for col in range(n)] for row in range(m)]
    c = [[0 for col in range(n+1)] for row in range(m+1)]
  
    for i in range(1,m+1):
        for j in range(1,n+1):
            if X[i-1]==Y[j-1]:
                c[i][j]=c[i-1][j-1]+1
                b[i-1][j-1]='↖' #대각선방향을 의미
            elif c[i-1][j]>=c[i][j-1]:
                c[i][j]=c[i-1][j]
                b[i-1][j-1]='↑'
            else:
                c[i][j]=c[i][j-1]
                b[i-1][j-1]='←'
    return b

def print_lcs(b,x,i,j):
    if i<0 or j<0:
        return
    if b[i][j]=='↖':
        print_lcs(b,x,i-1,j-1)
        print(x[i],end='')
    elif b[i][j]=='↑':
        print_lcs(b,x,i-1,j)
    else :
        print_lcs(b,x,i,j-1)


b=lsc_length(X,Y)
i=len(X)-1
j=len(Y)-1
print_lcs(b,X,i,j)