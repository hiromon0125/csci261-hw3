from sys import argv


def add_binary(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]


def subtract_binary(a, b):
    return bin(int(a, 2) - int(b, 2))[2:]


def shift_left(a, n):
    return a + "0" * n


def main(input_file: str = "input.txt", output_file: str = "output.txt") -> None:
    with open(input_file, "r") as infile:
        f = infile.read().strip().split("\n")
        X = int(f[0])
        Y = int(f[1])

    with open(output_file, "w") as outfile:

        def recursive_multiply(x: int, y: int) -> int:
            print(x, y)
            if x <= 1 or y <= 1:
                return x * y
            n = min(x.bit_length(), y.bit_length())
            m = n // 2
            xh = x >> m
            xl = x - (xh << m)
            yh = y >> m
            yl = y - (yh << m)
            zc = recursive_multiply(xh + xl, yh + yl)
            zh = recursive_multiply(xh, yh)
            zl = recursive_multiply(xl, yl)
            outfile.write(",".join(map(str, [m, xh, xl, yh, yl, zh, zc, zl])) + "\n")

            return zh * (1 << (2 * m)) + (zc - zh - zl) * (1 << m) + zl

        final = recursive_multiply(X, Y)
        print("fin: " + str(final))


if __name__ == "__main__":
    main(argv[1])
