with open('./inputday7.txt') as file:
    input_data = file.read()

def solve_part2(input_data):
    grid = [list(line) for line in input_data.strip().split('\n')]
    
    if not grid:
        return 0
        
    R = len(grid)
    C = len(grid[0])
    
    start_col = -1
    if 'S' in grid[0]:
        start_col = grid[0].index('S')
    else:
        return 0

    current_counts = {start_col: 1}

    for r in range(1, R):
        if not current_counts:
            break
            
        next_counts = {}
        
        for c, count in current_counts.items():
            
            if not (0 <= c < C):
                continue 
            
            cell = grid[r][c]
            
            if cell == '^':
                
                left_col = c - 1
                if 0 <= left_col < C:
                    next_counts[left_col] = next_counts.get(left_col, 0) + count
                
                right_col = c + 1
                if 0 <= right_col < C:
                    next_counts[right_col] = next_counts.get(right_col, 0) + count
            
            else:
                next_counts[c] = next_counts.get(c, 0) + count
                    
        current_counts = next_counts

    total_timelines = sum(current_counts.values())
    
    print(total_timelines)

solve_part2(input_data)