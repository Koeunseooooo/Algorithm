def solution(a, b, n):
    answer = 0
    remain = 0
    while n>=a : # 단, 보유 중인 빈 병이 2개 미만이면 콜라를 받을 수 없음
        remain_bottle=n%a # 반환되지 못하는, 남아있는 콜라의 수 
        n=(n//a)*b # 마트에서 받을 수 있는 콜라의 수 & n값 업데이트
        answer+=n # answer에 누적
        n+=remain_bottle # 남아있는 병은 n에 더해줘서 다음 마트갈 때 다시 이용
    return answer