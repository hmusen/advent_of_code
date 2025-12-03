with open('./inputday3.txt') as file:
    banks = file.read().split('\n')

def largest_12_digits(bank):
    digits_needed = 12
    result = []
    for i, d in enumerate(bank):
        # Remove smaller digits if we have enough digits left to reach 12
        while result and len(result) + (len(bank) - i) > digits_needed and result[-1] < d:
            result.pop()
        if len(result) < digits_needed:
            result.append(d)
    return int(''.join(result))

total = sum(largest_12_digits(bank) for bank in banks)
print(total)  # Output: 3121910778619
