from collections import deque

def solution(priorities, location):
    pr_q = deque(priorities)
    ind_q = deque(range(len(priorities)))
    answer = 0

    while pr_q:
        p = pr_q.popleft()
        i = ind_q.popleft()

        if any(p < other for other in pr_q):
            pr_q.append(p)
            ind_q.append(i)
        else:
            answer += 1
            if i == location:
                return answer
