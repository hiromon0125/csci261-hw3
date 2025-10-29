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

        n = max(len(str(x)), len(str(y)))
        m = n // 2
        high_x, low_x = divmod(x, 10**m)
        high_y, low_y = divmod(y, 10**m)
        zh = recursive_multiply(high_x, high_y)
        zc = recursive_multiply(low_x, low_y)
        zl = recursive_multiply(high_x + low_x, high_y + low_y)
        return zh * 10 ** (2 * m) + (zl - zh - zc) * 10**m + zc

    # compute result and write to output file
    result = recursive_multiply(x, y)
    with open(output_file, "w") as outfile:
        outfile.write(str(result) + "\n")


if __name__ == "__main__":
    main(argv[1])
