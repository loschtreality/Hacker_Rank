def lonely_integer(a, n):
    ex_or = a[0]

    for i in range(1, n):
        num = a[i]
        ex_or ^= num

    return ex_or
