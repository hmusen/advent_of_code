with open('./inputday7.txt') as file:
    input_data = file.read()

def part1(input_data):
    grid = [list(line) for line in input_data.strip().split('\n')]

    if not grid:
        return 0
    
    R = len(grid)
    C = len(grid[0])

    start_col = -1
    if 'S' in grid[0]:
        start_col = grid[0].index('S')
    else:
        return 0, "No S found in input"
    
    splits = 0
    activeBeams = {start_col}

    for r in range(1,R):
        if not activeBeams:
            break

        next_beams = set()
        hit_splitters = set()

        for c in activeBeams:
            if 0 <= c < C and grid[r][c] == '^':
                hit_splitters.add(c)

        splits += len(hit_splitters)

        for c in activeBeams:
            if c in hit_splitters:
                left_col = c - 1
                right_col = c + 1

                if 0 <= left_col < C:
                    next_beams.add(left_col)
                if 0 <= right_col < C:
                    next_beams.add(right_col)
            else:
                if 0 <= c < C:
                    next_beams.add(c) # no split needed

        activeBeams = next_beams

    print(splits)

part1(input_data)