def part2(input_data: str) -> int:
    
    points = []
    for line in input_data.strip().split('\n'):
        if line.strip():
            x, y, z = map(int, line.strip().split(','))
            points.append((x, y, z))

    N = len(points)
    if N <= 1:
        return 0

    distance_edges = []
    for i in range(N):
        for j in range(i + 1, N):
            p1 = points[i]
            p2 = points[j]
            
            d_sq = (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2
            
            distance_edges.append((d_sq, i, j))

    distance_edges.sort(key=lambda x: x[0])

    parent = list(range(N))
    size = [1] * N
    
    circuit_count = N 

    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        nonlocal circuit_count
        root_i = find(i)
        root_j = find(j)

        if root_i != root_j:
            if size[root_i] < size[root_j]:
                root_i, root_j = root_j, root_i
            
            parent[root_j] = root_i
            size[root_i] += size[root_j]
            circuit_count -= 1
            return True
        return False
    
    last_connection_x_coords = None

    for d_sq, u, v in distance_edges:
        if circuit_count == 1:
            break
            
        if union(u, v):
            if circuit_count == 1:
                x1 = points[u][0]
                x2 = points[v][0]
                last_connection_x_coords = (x1, x2)
                break
    
    if last_connection_x_coords:
        x1, x2 = last_connection_x_coords
        return x1 * x2
    else:
        return 0

with open('./inputday8.txt') as file:
    input_data = file.read()

p2 = part2(input_data)
print(p2)