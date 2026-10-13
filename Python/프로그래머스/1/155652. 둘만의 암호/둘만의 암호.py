def solution(s, skip, index):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    skip_set = set(skip)


    allowed = [char for char in alphabet if char not in skip_set]


    positions = {char: i for i, char in enumerate(allowed)}

    result = []

    for char in s:
        next_position = (positions[char] + index) % len(allowed)
        result.append(allowed[next_position])

    return "".join(result)