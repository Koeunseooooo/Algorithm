two_arr = [[False] * 2 for i in range(5)]
# two_arr = [[False] * 2] * 5

print(id(two_arr[0][0]))
print(id(two_arr[0][1]))
print(id(two_arr[0]))
print(id(two_arr[1]))
two_arr[0][0] = True
print(two_arr[0][0])
print(two_arr[0][1])


test = [1, 2, 3, 4, 5]
test[3] = 10
print(id(test[0]))
print(id(test[1]))
print(test[3])
print(test[4])

test1 = [1] * 5
test1[3] = 10
print(id(test1[0]))
print(id(test1[1]))
print(test1[3])
print(test1[4])
