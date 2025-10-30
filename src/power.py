def power(x: int, y: int):
    # x^((yh)*(2^n)) * x^yl
    print(x, y)
    if y <= 2:
        return x**y
    if y % 2 == 0:
        return power(x, y // 2) * power(x, y // 2)
    n = int((y.bit_length() + 0.5) // 2)
    yh = y >> n
    yl = y - (yh << n)
    temp = power(2, n)
    return power(x, yh * temp) * power(x, yl)


if __name__ == "__main__":
    print("result:", power(2, 0))  # 1024
    print("result:", power(2, 10))  # 1024
    print("result:", power(3, 20))  # 3486784401
    print("result:", power(6, 15))  # 470184984576
