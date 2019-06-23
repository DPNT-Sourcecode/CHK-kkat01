# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):

    if not isinstance(x, int):
        return
    if not isinstance(y, int):
        return

    if x < 0 or x > 100:
        return
    if y < 0 or y > 100:
        return

    return (x + y)
