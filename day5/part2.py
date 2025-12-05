with open('./inputday5.txt') as file:
    lines = file.read().split('\n')

split = lines.index("")
ranges = lines[:split]

count = 0
result = []
for r in ranges:
    dash = r.index('-')
    start = int(r[:dash])
    end = int(r[dash+1:])
    for i in range(start,end+1):
       if i not in result:
           result.append(i)
print(len(result))

# is this slow af?