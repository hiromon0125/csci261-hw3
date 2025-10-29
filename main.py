def fl(value: float) -> int:
    """Returns the floor of a float value as an integer."""
    return int(value)


def main():
    n = 0  # Global variable to hold the maximum bit-length

    def recursive_multiply(x: int, y: int) -> int:
        """
        Multiplies two integers x and y using the recursive multiplication algorithm.
        xl and xh are the low and high bits of x, respectively.
        yl and yh are the low and high bits of y, respectively.
        n is the maximum bit-length of x and y.
        """
        nonlocal n
        xl, xh = x & ((1 << (n // 2)) - 1), x >> (n // 2)
        yl, yh = y & ((1 << (n // 2)) - 1), y >> (n // 2)

        x = 2 ^ fl(n / 2) * xh + xl
        y = 2 ^ fl(n / 2) * yh + yl
        cx = xh + xl
        cy = yh + yl
        zh = recursive_multiply(xh, yh)
        zc = recursive_multiply(cx, cy)
        zl = recursive_multiply(xl, yl)
        return 2 ^ (2 * fl(n / 2)) * zh + 2 ^ (fl(n / 2)) * (zc - zh - zl) + zl


if __name__ == "__main__":
    main()
