import importlib
from itertools import count
from sys import argv

from mult_pub import add, lg_flr, mult

# hw3-2.py cannot be imported with a hyphen, so we use importlib
hw3_2 = importlib.import_module("hw3-2")


def noop(x=None, step=1):
    """Counter call signiture"""
    return x, step


def add_sp(x, y, _out=noop):
    m, n = 1 + 2 * lg_flr(x), 1 + 2 * lg_flr(y)
    return add(x, y, m, n, _out)


def mult_sp(x, y, _out=noop):
    m, n = 1 + 2 * lg_flr(x), 1 + 2 * lg_flr(y)
    return mult(x, y, m, n, _out)


def recursive_multiply(x: int, y: int, _out=noop) -> int:
    if x <= 1 or y <= 1:
        _out()
        return mult_sp(x, y, _out)
    _out(step=7)
    n = min(x.bit_length(), y.bit_length())
    m = n // 2
    xh = x >> m
    xl = x - (xh << m)
    yh = y >> m
    yl = y - (yh << m)
    zc = recursive_multiply(add_sp(xh, xl, _out), add_sp(yh, yl, _out), _out)
    zh = recursive_multiply(xh, yh, _out)
    zl = recursive_multiply(xl, yl, _out)

    _out([m, xh, xl, yh, yl, zh, zc, zl])
    return add_sp(
        add_sp(
            zh * (1 << (2 * m)),
            add_sp(add_sp(zc, -zh, _out), -zl, _out) * (1 << m),
            _out,
        ),
        zl,
        _out,
    )


def init_counter():
    c = count()

    def incre(_=None, step=1):
        for _ in range(step):
            next(c)

    return c, incre


if __name__ == "__main__":
    sample_domain = int(argv[1]) if len(argv) > 1 else 8
    test_bit_length = list(map(lambda x: 2**x, range(1, sample_domain + 1)))

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
        final = recursive_multiply(x, y, _out=incre)
        c = next(counter) - 1
        r = f"Ratio: {c / c_prev:.4f}" if c_prev is not None else ""
        print(f"Bits len: {bits} \tSteps: {c}\t{r}")
        c_prev = c
