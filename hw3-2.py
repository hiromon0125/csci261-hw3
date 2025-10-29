from sys import argv


def fl(value: float) -> int:
    """Returns the floor of a float value as an integer."""
    return int(value)


def main(input_file: str = "input.txt", output_file: str = "output.txt") -> None:
    with open(input_file, "r") as infile:
        x, y = map(int, infile.readline().strip().split())

    def recursive_multiply(x: int, y: int) -> int:
        """
        Multiplies two integers x and y using the Karatsuba recursive multiplication.
        This implementation works on bit lengths and uses shifts instead of powers/XOR.
        """
        # base cases
        if x == 0 or y == 0:
            return 0
        m = max(x.bit_length(), y.bit_length())
        if m == 1:
            return x * y

        m2 = m // 2

        xl = x & ((1 << m2) - 1)
        xh = x >> m2
        yl = y & ((1 << m2) - 1)
        yh = y >> m2

        z2 = recursive_multiply(xh, yh)
        z0 = recursive_multiply(xl, yl)
        z1 = recursive_multiply(xh + xl, yh + yl) - z2 - z0

        return (z2 << (2 * m2)) + (z1 << m2) + z0

    # compute result and write to output file
    result = recursive_multiply(x, y)
    with open(output_file, "w") as outfile:
        outfile.write(str(result) + "\n")


if __name__ == "__main__":
    main(argv[1])
