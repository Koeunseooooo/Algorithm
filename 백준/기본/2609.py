#최대공약수
def gcd(x,y):
    if x%y==0:
        return y
    return gcd(y,x%y)

#최소공배수
def lcm(x,y):
    return x*y // gcd(x,y)


a,b = map(int,input().split())
print(gcd(a,b))
print(lcm(a,b))
