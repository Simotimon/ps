def solution(K, dungeons):
    answer = -1
    dungeons.sort(key=lambda x: x[1])
    visited = [False] * len(dungeons)
    def dfs(current_k, count):
        nonlocal answer
        answer = max(answer, count)
        for i in range(len(dungeons)):
            if not visited[i] and current_k >= dungeons[i][0]:
                visited[i] = True
                dfs(current_k - dungeons[i][1], count + 1)
                visited[i] = False
    dfs(K, 0)
    return answer