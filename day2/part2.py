def has_repeating_pattern(s):
    n = len(s)
    for i in range(1, n):
        if n % i == 0 and s == s[:i] * (n // i):
            return True
    return False


def sum_invalid_ids(text):
    total = 0

    for r in text.split(','):
        try:
            start, end = map(int, r.split('-'))
        except ValueError:
            continue

        for x in range(start, end + 1):
            if has_repeating_pattern(str(x)):
                total += x

    return total


with open('./input_day2.txt') as file:
    input_text = file.read()

print(sum_invalid_ids(input_text))
