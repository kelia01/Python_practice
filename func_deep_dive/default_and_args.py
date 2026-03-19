from cmath import isnan


def product_calc(*args):
    product = 1

    if len(args) == 0:
        return product
    for x in args:
        if not isinstance(x, (int, float)):
            raise TypeError("All arguments must be numbers")
        product *= x
    return product

print(product_calc(2, 3, 4))