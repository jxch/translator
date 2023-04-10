from itertools import (takewhile, repeat)


def iter_count(file):
    buffer = 1024 * 1024
    buf_gen = takewhile(lambda x: x, (file.read(buffer) for _ in repeat(None)))
    return sum(buf.count("\n") for buf in buf_gen)
