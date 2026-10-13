def solution(s):
    digit_words = [
        "zero", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine"
    ]

    for digit, word in enumerate(digit_words):
        s = s.replace(word, str(digit))

    return int(s)