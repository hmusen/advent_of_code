def p2(rotations):
    position = 50
    count = 0
    
    for rotation in rotations:
        direction = rotation[0]
        distance = int(rotation[1:])
        
        if direction == 'L':
            for _ in range(distance):
                position = (position - 1) % 100
                if position == 0:
                    count += 1
        else:  # 'R'
            for _ in range(distance):
                position = (position + 1) % 100
                if position == 0:
                    count += 1
    
    return count


# Read input file
with open('input.txt', 'r') as f:
    rotations = [line.strip() for line in f.readlines()]

# Solve both parts
part_two = p2(rotations)

print(f"Part Two: {part_two}")