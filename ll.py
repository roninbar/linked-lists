def ll_insert(x, xs: tuple) -> tuple:
    if xs != ():
        y, ys = xs
        return (x, xs) if x < y else (y, ll_insert(x, ys))
    else:
        return x, ()


def ll_sorted(xs: tuple) -> tuple:
    if xs != ():
        y, ys = xs
        return ll_insert(y, ll_sorted(ys))
    else:
        return ()


def ll_concat(xs: tuple, ys: tuple) -> tuple:
    if xs != ():
        z, zs = xs
        return z, ll_concat(zs, ys)
    else:
        return ys


def ll_reverse(xs: tuple) -> tuple:
    ys = ()
    while xs != ():
        x, xs = xs
        ys = x, ys
    else:
        return ys
