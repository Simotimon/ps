import sys

def solution(tickets):
    n = len(tickets)
    sys.setrecursionlimit(max(sys.getrecursionlimit(), n + 100))

    tickets = sorted(tickets)  
    visited = [False] * n
    route = ["ICN"]

    def dfs(airport):
        
        if len(route) == n + 1:
            return True

        for j in range(n):
            
            if not visited[j] and tickets[j][0] == airport:
                visited[j] = True
                route.append(tickets[j][1])

                if dfs(tickets[j][1]):
                    return True

               
                visited[j] = False
                route.pop()

        return False

    dfs("ICN")
    return route