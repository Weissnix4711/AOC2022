import networkx as nx

TRANS = str.maketrans('SE', 'az')


def index_2d(list, v):
    """Return index of element v in 2d list"""
    for i, x in enumerate(list):
        if v in x:
            return (i, x.index(v))


def get_data(filename: str) -> list:
    """Open file and return data as a 2d list"""
    with open(filename) as f:
        data = [list(l) for l in f.read().strip().splitlines()]

    # Transpose matrix (swap x and y axis)
    data = list(map(list, zip(*data)))

    return data


def main():
    # Get data
    data = get_data('day12/data.txt')

    # Unweighted, directional graph
    graph = nx.DiGraph()

    # Find all edges which are possible to traverse
    edges = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if (j+1 < len(data[0])) and ((ord(data[i][j+1].translate(TRANS)) - ord(data[i][j].translate(TRANS))) <= 1):
                edges.append((f'{i},{j}', f'{i},{j+1}'))

            if (j-1 >= 0) and ((ord(data[i][j-1].translate(TRANS)) - ord(data[i][j].translate(TRANS))) <= 1):
                edges.append((f'{i},{j}', f'{i},{j-1}'))

            if (i+1 < len(data)) and ((ord(data[i+1][j].translate(TRANS)) - ord(data[i][j].translate(TRANS))) <= 1):
                edges.append((f'{i},{j}', f'{i+1},{j}'))

            if (i-1 >= 0) and ((ord(data[i-1][j].translate(TRANS)) - ord(data[i][j].translate(TRANS))) <= 1):
                edges.append((f'{i},{j}', f'{i-1},{j}'))

    # Add edges
    graph.add_edges_from(edges)

    # Find start and end positions
    start_pos = ','.join(map(str, index_2d(data, 'S')))
    end_pos = ','.join(map(str, index_2d(data, 'E')))

    # Find all shortest paths to given end node
    all_shortest_paths = list(
        nx.single_target_shortest_path_length(graph, end_pos))

    # Find coordinates of all 'a' nodes
    all_a_nodes = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 'a':
                all_a_nodes.append(str(i) + ',' + str(j))

    # Find intersection of all_a_nodes and all_shortest_paths
    all_paths_from_a = [
        tup for tup in all_shortest_paths if tup[0] in all_a_nodes]
    shortest_path_from_an_a = all_paths_from_a[0]

    # Part1: Shortest path from start to end
    print(f"Part 1: {nx.shortest_path_length(graph, start_pos, end_pos)}")

    # Part 2: Shortest path from any 'a' node to end
    print(
        f"Part 2: Distance {shortest_path_from_an_a[1]} from ({shortest_path_from_an_a[0]})")


if __name__ == "__main__":
    main()
