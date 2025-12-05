with open('./inputday5.txt') as file:
    lines = file.read().split('\n')

split = lines.index("")
ranges = lines[:split]
ingridients = lines[split+1:]

count = 0
for ingrid in ingridients:
    ingrid = int(ingrid)

    for r in ranges:
        dash = r.index('-')
        start = int(r[:dash])
        end = int(r[dash+1:])

        if start <= ingrid <= end:
            count += 1
            break
                   
print(count)



