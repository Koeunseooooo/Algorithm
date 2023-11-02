print(1 << 6)
check = [False] * (1 << 6)
# print(check)

print(2 | 4)

# 177 183 178
print(bin(177))
print(bin(183))
print(bin(178))

print(bin(177 ^ 183))
# 6은 이진수로 표현하기 위해 몇 비트가 필요한지 어떻게 알 수 있을까

m = print(bin(177))

result = 0b11111110  # 2의 보수 표현으로 -2는 모든 비트가 1인 상태
print(result, 11)
