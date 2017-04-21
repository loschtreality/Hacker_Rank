from functools import reduce
import math

n = int(input())


def max_element(loops):
    maximum = -math.inf
    stack = []

    for i in range(loops):
        query = list(map(int, input().strip().split()))
        query_type = query[0]

        if query_type == 1:
            maximum = max(query[-1], maximum)
            stack.append(query[-1])
        elif query_type == 2:
            item = stack.pop()
            if item == maximum and len(stack) > 0:
                maximum = reduce(lambda a, b: max(a, b), stack)
            elif len(stack) == 0:
                maximum = -math.inf
        else:
            print(maximum)


max_element(n)
