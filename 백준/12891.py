from collections import Counter, deque

# 9 8
# CCTGGATTG
# 2 0 1 1

n, s = map(int, input().strip().split())
dna = list(input())
# DNA 문자열은 모든 문자열에 등장하는 문자가 {‘A’, ‘C’, ‘G’, ‘T’} 인 문자열
A, C, G, T = map(int, input().strip().split())
dic = {"A": 0, "C": 0, "G": 0, "T": 0}
left = 0
right = s - 1
init = dna[left:right]
for a in init:
    if a in dic.keys():
        dic[a] += 1

answer = 0
while right < n:
    dic[dna[right]] += 1  # 오른쪽 원소 추가 -> 부분 문자열 길이만큼 완성
    if dic["A"] >= A and dic["C"] >= C and dic["G"] >= G and dic["T"] >= T:
        answer += 1
    dic[dna[left]] -= 1
    left += 1
    right += 1
print(answer)

# 코드 작성의 편의를 위해 슬라이딩 윈도우 기법에서도 투 포인터 개념이 활용될 수 있음을 유의하자
# 내가 제대로 슬라이딩 윈도우 기법을 활용하고 있는지 짚어보자
