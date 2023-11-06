n, m = 3, 4
a = [1, 3, 5]
b = [2, 4, 6, 8]
c = []
i, j = 0, 0

while i < n and j < m:
    if a[i] <= b[j]:
        c.append(a[i])
        i += 1
        if i == n:
            c += b[j:]
    else:
        c.append(b[j])
        j += 1
        if j == m:
            c += a[i:]

print(c)
