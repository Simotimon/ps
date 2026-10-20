def solution(arr):
    biggest =max(arr)
    answer = biggest
    
    while True:
        flag = True
        for num in arr:
            if answer % num !=0:
                flag = False
                break
        if flag:
            return answer
        answer += biggest