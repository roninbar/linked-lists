def insert(x, xs: tuple) -> tuple:
    if xs != ():
        y, ys = xs
        return (x, xs) if x < y else (y, insert(x, ys))
    else:
        return x, ()


def sorted(xs: tuple) -> tuple:
    if xs != ():
        y, ys = xs
        return insert(y, sorted(ys))
    else:
        return ()


def concat(xs: tuple, ys: tuple) -> tuple:
    if xs != ():
        z, zs = xs
        return z, concat(zs, ys)
    else:
        return ys


def reversed(xs: tuple) -> tuple:
    ys = ()
    while xs != ():
        x, xs = xs
        ys = x, ys
    else:
        return ys
