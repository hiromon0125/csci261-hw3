import importlib
from itertools import count

# hw3-2.py cannot be imported with a hyphen, so we use importlib
hw3_2 = importlib.import_module("hw3-2")


def init_counter():
    c = count()

    def incre(_=None):
        return next(c)

    return c, incre


if __name__ == "__main__":
    counter, incre = init_counter()
    test_bit_length = [2, 4, 8, 16, 32, 64, 128, 256]
    c_prev = None
    for bits in test_bit_length:
        x = (1 << bits) - 1
        y = (1 << bits) - 1
        final = hw3_2.recursive_multiply(x, y, incre)
        c = next(counter) - 1
        r = f"Ratio: {c / c_prev:.2f}" if c_prev is not None else ""
        print(f"Bits len: {bits} \tSteps: {c} \t{r}")
        c_prev = c
