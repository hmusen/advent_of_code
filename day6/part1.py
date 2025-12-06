import math

with open('./inputday6.txt') as file:
    raw = file.read()

rows = [line.split() for line in raw.strip().split("\n")]
columns = list(zip(*rows))


total = 0
subtot = []
for i in columns:
    res = []
    for number in i[:-1]:
        res.append(int(number))
    if i[-1] == "*":
        subtot.append(math.prod(res))
    else:
        subtot.append(sum(res))

print(sum(subtot))



    


        


# put into res and go from there


# total = 0
# for i, col in enumerate(columns, 1):
#     print(i)



    
    # for item in col:
    #     if str(col[-1:]) == '*':
           


