def solution(routes):
    routes.sort(key=lambda x: x[1])
    answer = 0
    cam = -30001   # 여기만 바꾸면 됨

    for start, end in routes:
        if start > cam:
            answer += 1
            cam = end
    return answer