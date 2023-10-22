a = [[1, 2], [3, 4]]
b = a[:]
print(id(a))  # 4396179528 (다름)
print(id(b))  # 4393788808 (다름)
print(id(a[0]))  # 4396116040 (같음)
print(id(b[0]))  # 4396116040 (같음)
b[0][1] = 0
# a의 내부 객체 변경 시 b의 내부 객체도 변경됨
print(a)  # [[1,2], [3, 4, 5]]
print(b)  # [[1, 2], [3, 4, 5]]
