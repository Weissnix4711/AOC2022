def move(stacks, command, reverse=False):
    """Execute move command on stacks, in-place. Optionally set reverse moves."""
    moved_creates = list(stacks[command[1] - 1])[:command[0]]
    stacks[command[1] - 1] = stacks[command[1] - 1].removeprefix(''.join(moved_creates))
    stacks[command[2] - 1] = ''.join(moved_creates[::-1 if reverse else 1]) + stacks[command[2] - 1]


def main():
    with open('day5/data.txt') as f:
        stacks, commands = f.read().split('\n\n')

    stacks = [''.join(stack).strip() for stack in list(zip(*stacks.split('\n')[:-1]))[1::4]]
    commands = [[int(a) for a in command.translate(str.maketrans({c: None for c in 'movefromto'})).split()] for command in commands.splitlines()]

    stacks2 = stacks.copy()

    for command in commands:
        move(stacks, command, True)
        move(stacks2, command, False)

    print(f"Part 1: {''.join([s[0] for s in stacks])}")
    print(f"Part 2: {''.join([s[0] for s in stacks2])}")


if __name__ == "__main__":
    main()
