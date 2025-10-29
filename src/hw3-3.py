import importlib
from itertools import count

from mult_pub import lg_flr, mult

# hw3-2.py cannot be imported with a hyphen, so we use importlib
hw3_2 = importlib.import_module("hw3-2")


def init_counter():
    c = count()

    def incre(_=None, step=1):
        for _ in range(step):
            next(c)

    return c, incre


if __name__ == "__main__":
    test_bit_length = [2, 4, 8, 16, 32, 64, 128, 256]
    print("HW3-2 Recursive Multiply:")
    c_prev = None
    for bits in test_bit_length:
        x = (1 << bits) - 1
        y = (1 << bits) - 1
        counter, incre = init_counter()
        final = hw3_2.recursive_multiply(x, y, _out=incre)
        c = next(counter) - 1
        r = f"Ratio: {c / c_prev:.4f}" if c_prev is not None else ""
        print(f"Bits len: {bits} \tSteps: {c} \t{r}")
        c_prev = c

    print("\nHW3-3 mult:")
    c_prev = None
    for bits in test_bit_length:
        x = (1 << bits) - 1
        y = (1 << bits) - 1
        counter, incre = init_counter()
        final = mult(x, y, lg_flr(x), lg_flr(y), _out=incre)
        c = next(counter) - 1
        r = f"Ratio: {c / c_prev:.4f}" if c_prev is not None else ""
        print(f"Bits len: {bits} \tSteps: {c} \t{r}")
        c_prev = c
