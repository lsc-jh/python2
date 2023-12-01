
def basicOp():
    print(2 ** 2 ** 3)  # 2 ^ 8
    print(3 // 2)

# basicOp()


def bitwiseOp():
    print(bin(14))
    print(bin(6))
    print(14 & 6)
    print(14 | 5)
    print(14 >> 2)  # 1110 ->
    print(bin(14 >> 2))  # 1110 -> 0011
    print(14 << 2)
    print(bin(14 << 2))

bitwiseOp()