def solution(progresses, speeds):
    answer = []
    deploy_day = 0

    for progress, speed in zip(progresses, speeds):
        days = (100 - progress + speed - 1) // speed

        if days > deploy_day:

            deploy_day = days
            answer.append(1)
        else:

            answer[-1] += 1

    return answer
