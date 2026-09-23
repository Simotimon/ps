def solution(array):
    dic = {}
    for num in array:
        dic[num] = array.count(num)
        
    max_val = max(dic.values())
     
    max_keys = []
    for k, v in dic.items():
        if v == max_val:
            max_keys.append(k)
            
    if len(max_keys) >= 2:
        return -1
    else:
        return max_keys[0]
        
   