with open('./input_day2.txt') as f:
    print(sum(
        x for r in f.read().split(',')
        for a,b in [map(int, r.split('-'))]
        for x in range(a, b+1)
        if (s := str(x))[:len(s)//2] == s[len(s)//2:] and len(s) % 2 == 0
    ))
