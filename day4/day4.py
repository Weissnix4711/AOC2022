with open('day4/data.txt') as f:
    data = [[[int(i) for i in d.split('-')] for d in p.split(',')] for p in f.read().splitlines()]

contained = lambda x, y : x.issubset(y) or y.issubset(x)
overlap = lambda x, y : bool(x.intersection(y) or y.intersection(x))

d = lambda x, y : [set(range(e[0], e[1] + 1)) for e in (x, y)]

con = [contained(*d(x, y)) for x, y in data]
dup = [overlap(*d(x, y)) for x, y in data]

print(f"Part 1: {sum(con)}")
print(f"Part 2: {sum(dup)}")
