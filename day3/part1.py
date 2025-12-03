with open('./inputday3.txt') as file:
    input_text = file.read().split('\n')

total_joltage = 0

for bank in input_text:
    max_joltage = 0
    for i in range(len(bank)):
        for j in range(i+1, len(bank)):
            joltage = int(bank[i] + bank[j])
            if joltage > max_joltage:
                max_joltage = joltage
    total_joltage += max_joltage

print(total_joltage)

        