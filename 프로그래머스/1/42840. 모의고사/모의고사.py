from math import ceil

def solution(answers):
    scores = []
    persons = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    for p in persons:
        temp = ceil(len(answers) / len(p)) * p
        scores.append(sum(a == t for a, t in zip(answers, temp)))

    max_score = max(scores)
    return [i + 1 for i, score in enumerate(scores) if score == max_score]