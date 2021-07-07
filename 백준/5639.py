#이진검색트리 백준 문제
# 자꾸 오류가 떠서 한시간뒤에 답지를 봤지만
# 답지의 의도와 완전히 같았다!!
# for문을 써서 오류가 났던것이다.. 여기선 꼭 while문을 써야한다
# 시간날때 내 방식으로 살짝 수정하기

import sys

# default 값이 1000이다
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def post_order(start, end):
    # 역전시 리턴
    if start > end:
        return

    # 루트 노드
    root = pre_order[start]
    idx = start + 1

    # root보다 커지는 지점을 찾는 과정  
    # for문으로 찾으면 안된다. 아래서 설명  
    while idx <= end:
        if pre_order[idx] > root:
            break
        idx += 1

    # 왼쪽 서브트리
    post_order(start + 1, idx - 1)

    # 오른쪽 서브트리
    post_order(idx, end)

    # 후위순회이므로 제일 마지막에 찍으면 된다
    print(root)


pre_order = []
while 1:
    try:
        pre_order.append(int(input()))
    # try에서 예외 발생시 break 실행 (한번더 enter키를 누르는 경우도 예외에 해당된다고 함)
    except:
        break

post_order(0, len(pre_order) - 1)

