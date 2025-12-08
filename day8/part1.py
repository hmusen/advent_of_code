def teleporter(input_data, max_connections):
    
    points = []
    for line in input_data.strip().split('\n'):
        if line.strip():
            x, y, z = map(int, line.strip().split(','))
            points.append((x, y, z))

    N = len(points)
    if N < 3:
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

    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)

        if root_i != root_j:
            if size[root_i] < size[root_j]:
                root_i, root_j = root_j, root_i
            
            parent[root_j] = root_i
            size[root_i] += size[root_j]
            return True
        return False

    edges_processed = 0
    for d_sq, u, v in distance_edges:
        if edges_processed >= max_connections:
            break
        
        union(u, v)
        edges_processed += 1

    circuit_sizes = []
    for i in range(N):
        if parent[i] == i:
            circuit_sizes.append(size[i])

    circuit_sizes.sort(reverse=True)

    s1 = circuit_sizes[0] if len(circuit_sizes) > 0 else 1
    s2 = circuit_sizes[1] if len(circuit_sizes) > 1 else 1
    s3 = circuit_sizes[2] if len(circuit_sizes) > 2 else 1
    
    return s1 * s2 * s3

with open('./inputday8.txt') as file:
    input_data = file.read()

result = teleporter(input_data, max_connections=1000)
print(result)