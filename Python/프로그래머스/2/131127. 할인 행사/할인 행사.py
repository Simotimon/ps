from collections import Counter

def solution(want, number, discount):
    answer = 0

    target = dict(zip(want, number))


    for start in range(len(discount) - 9):
 
        items = discount[start:start + 10]


        counts = Counter(items)

       
        if counts == target:
            answer += 1

    return answer