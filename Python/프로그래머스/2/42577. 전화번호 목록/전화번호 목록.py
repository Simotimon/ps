def solution(phone_book):
    hash_map = {}

    for number in phone_book:
        hash_map[number] = 1 

    for number in phone_book:
        temp = ""
        for char in number[:-1]:
            temp += char
            if temp in hash_map:
                return False
    return True
