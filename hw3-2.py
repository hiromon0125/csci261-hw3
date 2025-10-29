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
        x = bin(int(f[0]))[2:]
        y = bin(int(f[1]))[2:]

    with open(output_file, "w") as outfile:

        def recursive_multiply(X, Y):
            n = min(len(X), len(Y))
            m = n // 2
            # X = X.zfill(n)
            # Y = Y.zfill(n)
            if m <= 2:
                return bin(int(X, 2) * int(Y, 2))[2:]
            xh, xl = X[:m], X[m:]
            yh, yl = Y[:m], Y[m:]
            zl = recursive_multiply(xl, yl)
            zc = recursive_multiply(add_binary(xh, xl), add_binary(yh, yl))
            zh = recursive_multiply(xh, yh)
            outfile.write(
                ",".join(
                    map(
                        str,
                        [
                            m,
                            int(xh, 2),
                            int(xl, 2),
                            int(yh, 2),
                            int(yl, 2),
                            int(zh, 2),
                            int(zc, 2),
                            int(zl, 2),
                        ],
                    )
                )
                + "\n"
            )

            temp1 = shift_left(zh, 2 * (n - m))
            temp2 = shift_left(subtract_binary(zc, add_binary(zh, zl)), n - m)
            result = add_binary(add_binary(temp1, temp2), zl)
            return result.lstrip("0") or "0"

        # compute result and (optionally) write final result
        final = recursive_multiply(x, y)
        print(int(final, 2))


if __name__ == "__main__":
    main(argv[1])
