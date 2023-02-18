a, b, n = input().split()
n = int(n)

# banana apple 3
a = a+b
print(a)
b = list(b)

if len(b) >= n:
    for i in range(n):
        b[i] = a[i]
    print(''.join(b))
else:
    print(a[:n])
