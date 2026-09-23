def solution(array):
    counts = {}
    for num in set(array):
        counts[num] = array.count(num)
    
    max_count = max(counts.values())
    
    if list(counts.values()).count(max_count) > 1:
        return -1
    else:
        for num, cnt in counts.items():
            if cnt == max_count:
                return num