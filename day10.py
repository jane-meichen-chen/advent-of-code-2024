from pathlib import Path


def search(_map, x, y, value) -> list[tuple[int, int]]:
    if _map[y][x] == value:
        if value == 9:
            return [(x, y)]
        search_results = []
        if x > 0:
            search_results.append(search(_map, x-1, y, value+1))
        if x < len(_map[0]) - 1:
            search_results.append(search(_map, x+1, y, value+1))
        if y > 0:
            search_results.append(search(_map, x, y-1, value+1))
        if y < len(_map) - 1:
            search_results.append(search(_map, x, y+1, value+1))
        return [c for r in search_results for c in r]
    return []


def part_1_solution(file_path: str) -> int:
    with open(file_path, 'r') as input_file:
        topographical_map = [list(map(int, line)) for line in input_file.read().splitlines()]

    trailhead_scores = [
        len(set(search(topographical_map, col, row, value)))
        for row, line in enumerate(topographical_map)
        for col, value in enumerate(line)
        if value == 0
    ]
    return sum(trailhead_scores)


def part_2_solution(file_path: str) -> int:
    with open(file_path, 'r') as input_file:
        topographical_map = [list(map(int, line)) for line in input_file.read().splitlines()]

    trailhead_scores = [
        len(search(topographical_map, col, row, value))
        for row, line in enumerate(topographical_map)
        for col, value in enumerate(line)
        if value == 0
    ]
    return sum(trailhead_scores)


if __name__ == "__main__":
    day = Path(__file__).stem
    assert part_1_solution(f"data/{day}-test-case.txt") == 36
    print("test case passed")
    print(part_1_solution(f"data/{day}.txt"))
    assert part_2_solution(f"data/{day}-test-case.txt") == 81
    print("test case passed")
    print(part_2_solution(f"data/{day}.txt"))
