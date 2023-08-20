# permutations
array = [1, 2, 3]
k = 2
used = [False for i in range(len(array))]


def permutations(arr):
    if len(arr) == k:
        print(arr, end="")
        return arr
    for i in range(len(array)):
        if used[i] == False:
            used[i] = True
            permutations(arr + [array[i]])
            used[i] = False


permutations([])
print()

# product
array = [1, 2, 3]
k = 2
used = [False for i in range(len(array))]


def product(arr):
    if len(arr) == k:
        print(arr, end="")
        return arr
    for i in range(len(array)):
        product(arr + [array[i]])


product([])
print()

# combination
array = [1, 2, 3]
k = 2
used = [False for i in range(len(array))]


def combination(arr, i):
    if len(arr) == k:
        print(arr, end="")
        return arr
    for i in range(i, len(array)):
        combination(arr + [array[i]], i + 1)


combination([], 0)
print()

# combination_with_replacement
array = [1, 2, 2, 3]
k = 2
used = [False for i in range(len(array))]


def combination_with_replacement(arr, i):
    if len(arr) == k:
        print(arr, end="")
        return arr
    for i in range(i, len(array)):
        combination_with_replacement(arr + [array[i]], i)


combination_with_replacement([], 0)
print()
