from collections import defaultdict
from typing import List, Tuple, NewType

DISK_SIZE = 70_000_000
SPACE_NEEDED = 30_000_000

Commands = NewType('commands', List[Tuple[str, List[str]]])


with open('day7/data.txt') as f:
    commands: Commands = [tuple([command.splitlines()[0], command.splitlines()[1:]])
                          for command in f.read().strip().split('$ ')[1:]]

cur_dir: str = ''
sizes = defaultdict(int)

for command in commands:
    if command[0].startswith('cd '):
        next_dir = command[0].strip('cd ')
        if next_dir == '..':
            # Up a dir
            cur_dir = ''.join([u for x in cur_dir.split('/')
                              for u in (x, '/')][:-4])
        else:
            # cd to sub dir
            if command[0].removeprefix('cd ').startswith('/'):
                # absolute path
                cur_dir = command[0].removeprefix('cd ')
            else:
                # relative path
                cur_dir = cur_dir.removesuffix(
                    '/') + '/' + command[0].removeprefix('cd ')
        if not cur_dir.endswith('/'):
            cur_dir += '/'

    if command[0].startswith('ls'):
        contents = command[1]
        for c in contents:
            if not c.startswith('dir'):
                for i in range(len(cur_dir.split('/'))-1):
                    sizes[''.join([u for x in cur_dir.split('/')
                                   for u in (x, '/')][1:-2][:(2*i)+1])] += int(c.split()[0])


total = 0
smallest_large_dir = ''

free_space = (DISK_SIZE - sizes.get('/'))
to_delete = SPACE_NEEDED - free_space

for key, value in sizes.items():
    if value <= 100_000:
        total += value

    if value >= to_delete:
        if (sizes.get(smallest_large_dir) == None) or (value <= sizes.get(smallest_large_dir)):
            smallest_large_dir = key

print(f"Part 1: {total}")
print(f"Part 2: {sizes.get(smallest_large_dir)}")
