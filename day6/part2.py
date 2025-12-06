with open('./inputday6.txt') as file:
    input_text = file.read()

lines = input_text.strip().split('\n')
if not lines:
    grand_total = 0
else:
    max_len = max(len(line) for line in lines)
    padded_lines = [line.ljust(max_len) for line in lines]
    num_rows = len(padded_lines)

    columns = [''.join(padded_lines[r][c] for r in range(num_rows)) for c in range(max_len)]

    problems = []
    current_problem_cols = []
    for col in columns:
        if col.isspace():
            if current_problem_cols:
                problems.append(current_problem_cols)
            current_problem_cols = []
        else:
            current_problem_cols.append(col)
    if current_problem_cols:
        problems.append(current_problem_cols)

    grand_total = 0
    problems_part2 = problems[::-1]

    for problem_cols in problems_part2:
        operator_char = None
        for col in problem_cols:
            if col[-1] in ('+', '*'):
                operator_char = col[-1]
                break
                
        problem_numbers = []
        for col in problem_cols:
            number_digits = col[:-1]  
            cleaned_num_str = ''.join(digit for digit in number_digits if not digit.isspace())
            if cleaned_num_str:
                problem_numbers.append(int(cleaned_num_str))
                
        result = 0
        if operator_char == '+':
            result = sum(problem_numbers)
        elif operator_char == '*':
            result = 1
            for n in problem_numbers:
                result *= n
                
        grand_total += result

        print(grand_total)
