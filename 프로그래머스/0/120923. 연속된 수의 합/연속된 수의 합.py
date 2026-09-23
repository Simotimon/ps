def solution(num, total):
    answer = []
    x = (num*(num-1)//2)
    y = total - x
    
    if y % num == 0:
        x = y // num
        answer = list(range(x, x+num))
    
    return answer