def solution(brown, yellow):
    answer = []
    sum=brown+yellow
    for i in range(3,sum):
        if sum%i==0:
            x=sum//i
            y=i
            if x>=3 and y>=3:
                if x<y:
                    x, y = y, x
                center = (x - 2) * (y - 2);
                if center == yellow:
                    answer.append(x)
                    answer.append(y)
                    break
    return answer