def first_marker(data, length):
    for i in range(length, len(data)+1):
        if len(set(data[i-length:i])) == length:
            return i


def main():
    with open('day6/data.txt') as f:
        data = f.read().strip()
    print(f"Part 1: {first_marker(data, 4)}")
    print(f"Part 2: {first_marker(data, 14)}")


if __name__ == "__main__":
    main()
