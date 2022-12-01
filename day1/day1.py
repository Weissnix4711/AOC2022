with open('day1/data.txt') as f:
    data = [s.split('\n') for s in f.read().strip().split('\n\n')]

elves = [sum([int(food) for food in elf]) for elf in data]
elves.sort()

print(f"Part 1) Highest: {elves[-1]}")
print(f"Part 2) Top three: {sum(elves[-3:])}")
