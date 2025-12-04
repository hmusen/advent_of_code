with open('./inputday4.txt') as file:
    lines = file.read().split('\n')

def rolls(lines):
    grid = [list(line) for line in lines if line.strip()!='']
    R = len(grid)
    C = len(grid[0] if R>0 else 0)
    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    accessCount = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] != '@':
                continue
            neighbours = 0
            for dr,dc in dirs:
                nr, nc = r+dr, c+dc
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == '@':
                    neighbours += 1
            if neighbours < 4:
                accessCount += 1
    print(accessCount)

rolls(lines)