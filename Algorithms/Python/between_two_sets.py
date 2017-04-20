def is_factor(num, fac):
    return num % fac == 0


def is_elements_factor(array, factor):
    mapped = map(lambda num: is_factor(num, factor), array)
    return all(mapped)


def is_factor_of_elements(array, fac):
    mapped = map(lambda num: is_factor(num, fac), array)
    return all(mapped)


def between_sets(alpha, beta):
    fac_count = 0
    minimum = alpha[-1]
    maximum = beta[0]

    for i in range(minimum, maximum + 1):
        if is_elements_factor(alpha, i) and is_factor_of_elements(beta, i):
            fac_count += 1

    return fac_count
