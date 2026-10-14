def solution(sizes):
    max_width = 0
    max_height = 0

    for width, height in sizes:
        long_side = max(width, height)
        short_side = min(width, height)

        max_width = max(max_width, long_side)
        max_height = max(max_height, short_side)

    return max_width * max_height