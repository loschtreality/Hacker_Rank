bracket_map = {
    ")": "(",
    "}": "{",
    "]": "["
}


def bracket_matcher(brackets):
    stack = []
    is_matching = True
    for bracket in brackets:
        try:
            if bracket_map[bracket]:
                try:
                    item = stack.pop()
                    if bracket_map[bracket] != item:
                        is_matching = False
                except IndexError:
                    is_matching = False
        except KeyError:
            stack.append(bracket)

    if is_matching:
        print("YES")
    else:
        print("NO")
