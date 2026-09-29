def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for i in range(len(prices)):
        while stack and prices[i] < prices[stack[-1]]:
            previous = stack.pop()
            answer[previous] = i - previous

        stack.append(i)

    for previous in stack:
        answer[previous] = len(prices) - 1 - previous

    return answer