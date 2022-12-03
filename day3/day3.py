def priority(i):
    return ((ord(i) & 0b111111) + 26) % 58

with open('day3/data.txt') as f:
    data = f.read().strip().split()

rucksacks = [[d[:len(d)//2],d[len(d)//2:]] for d in data]

priorities = []
for r in rucksacks:
    for i in r[0]:
        if i in r[1]:
            priorities.append(priority(i))
            break

print(f"Part 1: {sum(priorities)}")

groups = [data[i:i+3] for i in range(0, len(data), 3)]

badge_priorities = []
for group in groups:
    for item in group[0]:
        if item in group[1] and item in group[2]:
            badge_priorities.append(priority(item))
            break

print(f"Part 2: {sum(badge_priorities)}")
