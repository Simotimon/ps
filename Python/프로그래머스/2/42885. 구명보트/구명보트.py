def solution(people, limit):
    answer = 0
    
    people = sorted(people)
    
    min_i = 0
    max_i = len(people) -1
    
    while min_i <= max_i:
        if people[min_i]+people[max_i]<=limit:
            min_i += 1
            
        max_i -= 1
        answer += 1
    return answer