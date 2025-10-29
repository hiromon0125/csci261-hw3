from sys import argv


def fl(value: float) -> int:
    """Returns the floor of a float value as an integer."""
    return int(value)


def add_binary(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]


def subtract_binary(a, b):
    return bin(int(a, 2) - int(b, 2))[2:]


def shift_left(a, n):
    return a + "0" * n


def main(input_file: str = "input.txt", output_file: str = "output.txt") -> None:
    with open(input_file, "r") as infile:
        x, y = map(int, infile.readline().strip().split())

    with open(output_file, "w") as outfile:

        def recursive_multiply(X, Y):
            n = max(len(X), len(Y))
            # Pad the shorter string with zeros
            X = X.zfill(n)
            Y = Y.zfill(n)
            if n == 1:
                return str(int(X) * int(Y))
            m = n // 2
            xh, xl = X[:m], X[m:]
            yh, yl = Y[:m], Y[m:]
            zh = recursive_multiply(xh, yh)
            zc = recursive_multiply(add_binary(xh, xl), add_binary(yh, yl))
            zl = recursive_multiply(xl, yl)
            outfile.write(",".join([X, Y, zh, zc, zl]) + "\n")

            temp1 = shift_left(zh, 2 * (n - m))
            temp2 = shift_left(subtract_binary(zc, add_binary(zh, zl)), n - m)
            result = add_binary(add_binary(temp1, temp2), zl)
            return result.lstrip("0") or "0"

        # compute result and write to output file
        recursive_multiply(x, y)


if __name__ == "__main__":
    main(argv[1])
