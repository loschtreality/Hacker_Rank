def compare(left, right):
    if left > right:
        return -1
    elif left == right:
        return 0
    else:
        return 1


def tally(a_list, b_list):
    alpha = 0
    beta = 0
    for index in range(len(a_list)):
        result = compare(a_list[index], b_list[index])

        if result == -1:
            alpha += 1
        elif result == 1:
            beta += 1

    print(alpha, beta)


# tally([a0, a1, a2], [b0, b1, b2])
