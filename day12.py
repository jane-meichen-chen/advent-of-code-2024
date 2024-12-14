from pathlib import Path


def read_input(file_path: str) -> list[list[str]]:
    with open(file_path, "r") as input_file:
        return list(map(list, input_file.read().splitlines()))


def recurse(
    garden_map: list[list[str]],
    x: int,
    y: int,
    plant: str,
    visited: set[tuple[int, int]],
) -> tuple[list[tuple[int, int]], set[tuple[int, int]], int]:
    if (x, y) in visited and garden_map[y][x] == plant:
        return [], visited, -1
    if garden_map[y][x] != plant:
        return [], visited, 0
    visited.add((x, y))
    within_region = [(x, y)]
    perimeter_offset = 0
    if 0 < x:
        plants, visited, offset = recurse(garden_map, x - 1, y, plant, visited)
        perimeter_offset -= (bool(plants) - offset)
        within_region += plants
    if x < len(garden_map[0]) - 1:
        plants, visited, offset = recurse(garden_map, x + 1, y, plant, visited)
        perimeter_offset -= (bool(plants) - offset)
        within_region += plants
    if 0 < y:
        plants, visited, offset = recurse(garden_map, x, y - 1, plant, visited)
        perimeter_offset -= (bool(plants) - offset)
        within_region += plants
    if y < len(garden_map) - 1:
        plants, visited, offset = recurse(garden_map, x, y + 1, plant, visited)
        perimeter_offset -= (bool(plants) - offset)
        within_region += plants

    return within_region, visited, perimeter_offset


def part_1_solution(file_path: str) -> int:
    garden_map = read_input(file_path)
    cost = 0
    visited = set()
    for y, line in enumerate(garden_map):
        for x, plant in enumerate(line):
            if (x, y) not in visited:
                coords, visited, offset = recurse(garden_map, x, y, plant, visited)
                cost += len(coords) * (len(coords) * 4 + offset)
    return cost


def part_2_solution(file_path: str) -> int:
    with open(file_path, "r") as file_input:
        garden_map = {
            (x, y): plot for y, row in enumerate(file_input.read().splitlines()) for x, plot in enumerate(row)
        }
    regions = {coordinate: {coordinate} for coordinate in garden_map}
    for coordinate in garden_map:
        for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x, y = coordinate
            i, j = direction
            neighbour = (x + i, y + j)
            if neighbour in garden_map and garden_map[coordinate] == garden_map[neighbour]:
                regions[coordinate] |= regions[neighbour]
                for plot in regions[coordinate]:
                    regions[plot] = regions[coordinate]
    regions = set(map(tuple, regions.values()))
    cost = 0
    for region in regions:
        edges = {((x, y), (i, j)) for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)] for (x, y) in region if (x+i, y+j) not in region}
        fences = edges - {((x-j, y+i), (i, j)) for (x, y), (i, j) in edges}
        cost += len(region) * len(fences)
    return cost


def model_part_2_solution(file_path: str) -> int:
    # union find
    # https://topaz.github.io/paste/#XQAAAQA8AgAAAAAAAAAznIlVuhcHbNxnuSHT4g03cKSzy2i112g3COX3gkaAP2eV4rCwnp85fq6StaQsMZs9LAF/jtdNpR8tOXDEXAZZ0BxP9zCpZhNKNOuRAoJ5TAfe4S84LNHoB8uqxGt0fuRsIUYStsXt25X9+5xl0QwUn2RYLwl2dDyVL8chKy+DsOdN9EkMXPuB2RCljLnvvjVDZxzpo2yqOxWNkW84HI493yohqnR4lwQo2faeKbN0Wo7zR7W3J6H/IXyDNOqqLOOoaP/pIqjjkKf+9ShV4UWIb7qgMYMAxgNSjjrbaredI5MZM32X9wTaoicEPXmGGEj+imphvqGha2juQO3+4oZ+yJH83bJbjQFKHR4YV/Aopzby5H1BV91f3NrISbn7xbDEWfseiy6SYxuSq/qQao4av/7XTFQ=
    grid = {i + j * 1j: c for i, r in enumerate(open(file_path))
            for j, c in enumerate(r.strip())}

    sets = {p: {p} for p in grid}
    for p in grid:
        for n in p + 1, p - 1, p + 1j, p - 1j:
            if n in grid and grid[p] == grid[n]:
                sets[p] |= sets[n]
                for x in sets[p]:
                    sets[x] = sets[p]

    sets = {tuple(s) for s in sets.values()}

    def edge(ps):
        P = {(p, d) for d in (+1, -1, +1j, -1j) for p in ps if p + d not in ps}
        return P - {(p + d * 1j, d) for p, d in P}

    return sum(len(s) * len(edge(s)) for s in sets)


if __name__ == "__main__":
    day = Path(__file__).stem
    assert part_1_solution(f"data/{day}-test-case1.txt") == 140
    assert part_1_solution(f"data/{day}-test-case2.txt") == 772
    assert part_1_solution(f"data/{day}-test-case3.txt") == 1930
    print("test case passed")
    print(part_1_solution(f"data/{day}.txt"))
    assert part_2_solution(f"data/{day}-test-case1.txt") == 80
    assert part_2_solution(f"data/{day}-test-case2.txt") == 436
    assert part_2_solution(f"data/{day}-test-case4.txt") == 236
    assert part_2_solution(f"data/{day}-test-case3.txt") == 1206
    print("test case passed")
    print(part_2_solution(f"data/{day}.txt"))
