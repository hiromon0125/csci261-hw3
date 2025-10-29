from sys import argv


def add_decimal(a, b):
    return str(int(a) + int(b))


def subtract_decimal(a, b):
    return str(int(a) - int(b))


def shift_left_decimal(a, n):
    return a + "0" * n


def main(input_file: str = "input.txt", output_file: str = "output.txt") -> None:
    with open(input_file, "r") as infile:
        x, y = infile.read().strip().split("\n")

    with open(output_file, "w") as outfile:

        def recursive_multiply(X, Y):
            n = max(len(X), len(Y))
            X = X.zfill(n)
            Y = Y.zfill(n)
            if len(X) == 1 and len(Y) == 1:
                return str(int(X) * int(Y))
            m = n // 2
            xh, xl = X[:m] or "0", X[m:] or "0"
            yh, yl = Y[:m] or "0", Y[m:] or "0"

            zc = recursive_multiply(add_decimal(xh, xl), add_decimal(yh, yl))
            zl = recursive_multiply(xl, yl)
            zh = recursive_multiply(xh, yh)
            outfile.write(",".join(map(str, [m, xh, xl, yh, yl, zh, zc, zl])) + "\n")

            temp1 = shift_left_decimal(zh, 2 * (n - m))
            temp2 = shift_left_decimal(subtract_decimal(zc, add_decimal(zh, zl)), n - m)
            result = add_decimal(add_decimal(temp1, temp2), zl)
            return result.lstrip("0") or "0"

        # compute result and (optionally) write final result
        final = recursive_multiply(x, y)
        print(int(final))


if __name__ == "__main__":
    main(argv[1])
