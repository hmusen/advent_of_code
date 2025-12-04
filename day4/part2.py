def total_removed(lines):
    grid = [list(line) for line in lines if line.strip()]
    R = len(grid)
    C = len(grid[0])

    dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

    def neighbours(r,c):
        return sum(
            1 for dr, dc in dirs
            if 0 <= r+dr < R and 0 <= c+dc < C
            and grid[r+dr][c+dc] == '@'
        )
    
    total = 0

    while True: 
        remove = []

        for r in range(R):
            for c in range(C):
                if grid[r][c] == '@' and neighbours(r,c) < 4:
                    remove.append((r,c))

        
        if not remove:
            break

        for r,c in remove:
            grid[r][c] = '.'
            total +=1 

    print(total)

with open('./inputday4.txt') as file:
    lines = file.read().splitlines()

total_removed(lines)