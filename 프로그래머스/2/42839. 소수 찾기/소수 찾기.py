from itertools import permutations

def solution(numbers):
    candidates = set()

    for length in range(1, len(numbers) + 1):
        for pieces in permutations(numbers, length):
            number = int(''.join(pieces))
            candidates.add(number)

    answer = 0

    for number in candidates:
        if number < 2:
            continue

        is_prime = True

        divisor = 2
        while divisor * divisor <= number:
            if number % divisor == 0:
                is_prime = False
                break
            divisor += 1

        if is_prime:
            answer += 1

    return answer