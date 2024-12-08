from collections import defaultdict
from itertools import combinations
from pathlib import Path


def part_1_solution(file_path: str) -> int:
    antennas = defaultdict(list)
    with open(file_path, "r") as input_data:
        for y, row in enumerate(input_data.read().splitlines()):
            for x, grid in enumerate(row):
                if grid != ".":
                    antennas[grid].append((x, y))

    antinodes = set()
    for antenna_coordinates in antennas.values():
        for (a1x, a1y), (a2x, a2y) in set(combinations(antenna_coordinates, 2)):
            dx = a1x - a2x
            dy = a1y - a2y
            antinodes |= {(a1x + dx, a1y + dy), (a2x - dx, a2y - dy)}
    return len([antinode for antinode in antinodes if 0 <= antinode[0] <= x and 0 <= antinode[1] <= y])


def part_2_solution(file_path: str) -> int:
    antennas = defaultdict(list)
    with open(file_path, "r") as input_data:
        for y, row in enumerate(input_data.read().splitlines()):
            for x, grid in enumerate(row):
                if grid != ".":
                    antennas[grid].append((x, y))

    antinodes = set()
    for antenna_coordinates in antennas.values():
        for (a1x, a1y), (a2x, a2y) in set(combinations(antenna_coordinates, 2)):
            dx = a1x - a2x
            dy = a1y - a2y
            while 0 <= a1x <= x and 0 <= a1y <= y:
                antinodes |= {(a1x, a1y)}
                a1x += dx
                a1y += dy
            while 0 <= a2x <= x and 0 <= a2y <= y:
                antinodes |= {(a2x, a2y)}
                a2x -= dx
                a2y -= dy
    return len([antinode for antinode in antinodes])


if __name__ == "__main__":
    day = Path(__file__).stem
    assert part_1_solution(f"data/{day}-test-case.txt") == 14
    print(part_1_solution(f"data/{day}.txt"))
    assert part_2_solution(f"data/{day}-test-case.txt") == 34
    print(part_2_solution(f"data/{day}.txt"))  # 436 too low
