from collections import deque

def solution(maps):
    rows, cols = len(maps), len(maps[0])
    dist = [[0] * cols for _ in range(rows)]
    dist[0][0] = 1

    q = deque([(0, 0)])
    while q:
        r, c = q.popleft()
        if (r, c) == (rows - 1, cols -1):
            return dist[r][c]
        for dr, dc in [(1, 0),(-1,0),(0,1),(0,-1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols :
                if maps[nr][nc] == 1 and dist[nr][nc] == 0:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
    
    return -1