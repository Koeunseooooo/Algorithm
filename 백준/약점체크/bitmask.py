def bitCount(x):
    if x == 0:
        return 0
    return x % 2 + bitCount(x // 2)


print(bitCount(0b01110101011))

S = 0b01010
print(bin(S & (1 << 3)) if S & (1 << 3) != 0 else 0)
