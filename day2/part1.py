with open('./input_day2.txt') as file:
    input_text = file.read()

def is_invalid_part_two(id_str):
    n = len(id_str)
    
    for l in range(1, n):
        if n % l == 0:
            pattern = id_str[:l]
            
            reconstructed_id = pattern * (n // l)
            
            if reconstructed_id == id_str:
                return True
                
    return False

def calculate_sum_of_invalid_ids(input_text):
    working_ranges = list(input_text.split(','))
    total_sum = 0
    
    for range_str in working_ranges:
        parts = range_str.split('-')
        if len(parts) != 2:
             continue 

        front = parts[0].strip()
        rear = parts[1].strip()

        try:
            start_id = int(front)
            end_id = int(rear)
        except ValueError:
            continue
        
        for x in range(start_id, end_id + 1):
            string_x = str(x)
            
            if is_invalid_part_two(string_x):
                total_sum += x
        
    return total_sum

result = calculate_sum_of_invalid_ids(input_text)
print(result)