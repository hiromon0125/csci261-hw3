from sys import argv


def noop(x=None, step=1):
    """Counter call signiture"""
    return x, step


def recursive_multiply(x: int, y: int, _out=noop) -> int:
    if x <= 1 or y <= 1:
        _out()
        return x * y
    _out(step=7)
    n = min(x.bit_length(), y.bit_length())
    m = n // 2
    xh = x >> m
    xl = x - (xh << m)
    yh = y >> m
    yl = y - (yh << m)
    zc = recursive_multiply(xh + xl, yh + yl, _out)
    zh = recursive_multiply(xh, yh, _out)
    zl = recursive_multiply(xl, yl, _out)

    _out([m, xh, xl, yh, yl, zh, zc, zl])
    return zh * (1 << (2 * m)) + (zc - zh - zl) * (1 << m) + zl


def main(input_file: str = "input.txt", output_file: str = "output.txt") -> None:
    with open(input_file, "r") as infile:
        f = infile.read().strip().split("\n")
        X = int(f[0])
        Y = int(f[1])

    with open(output_file, "w") as outfile:

        def out_write(ls: list[int] | None = None, step=1):
            if ls is None:
                return
            outfile.write(",".join(map(str, ls)) + "\n")

        final = recursive_multiply(X, Y, out_write)
        print("fin: " + str(final))


if __name__ == "__main__":
    main(argv[1])
