def fib_lite(n):
    if 1 >= n > -1:
        return n

    fib_sum = 0
    fib_next = 1

    while n > 0:
        n -= 1
        temp = fib_sum
        fib_sum = fib_next
        fib_next = fib_sum + temp

    return fib_sum
