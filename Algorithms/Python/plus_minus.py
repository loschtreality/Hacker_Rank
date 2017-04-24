def plus_minuses(array):
    pos = 0
    neg = 0
    zero = 0

    for num in array:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        else:
            zero += 1

    pos = create_fraction(pos, len(array))
    neg = create_fraction(neg, len(array))
    zero = create_fraction(zero, len(array))

    print(pos)
    print(neg)
    print(zero)


def create_fraction(num, length):
    if num == 0:
        return 0.00000

    return round(num / length, 5)
