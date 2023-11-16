n = int(input())

result = []
for i in range(1, n + 1):
    if "3" in str(i) or "6" in str(i) or "9" in str(i):
        cnt = 0
        for j in str(i):
            if j == "3" or j == "6" or j == "9":
                cnt += 1
        result.append("-" * cnt)
    else:
        result.append(str(i))

ans = " ".join(result)
print("{0}".format(ans))
