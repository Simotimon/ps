def solution(array, commands):
    answer = []

    for cm in commands:
        [i,j,k] =cm
        arr= array[i-1 : j]
        arr = sorted(arr)
        answer.append(arr[k-1])
    return answer