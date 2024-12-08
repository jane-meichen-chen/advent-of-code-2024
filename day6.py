from functools import cached_property
from typing import Optional


def read_input(file_path: str) -> tuple[list[str], int, int, tuple[int, int]]:
    with open(file_path, 'r') as input_file:
        raw_input = input_file.read().strip("\n")
        map_ = []
        row, column = None, None
        direction = UP
        for y, line in enumerate(raw_input.splitlines()):
            if "^" in line:
                for x, grid in enumerate(line):
                    if grid == "^":
                        column, row = x, y
                        line.replace(grid, ".")
            map_.append(line)
    if row is None or column is None:
        raise ValueError("Cannot find starting point")
    return map_, row, column, direction


UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)


def turn_right(direction: tuple[int, int]) -> tuple[int, int]:
    return -direction[1], direction[0]


def is_edge(map_: list[str], column: int, row: int, direction: tuple[int, int]) -> bool:
    return (
        (row == 0 and direction == UP)
        or (row == len(map_) - 1 and direction == DOWN)
        or (column == 0 and direction == LEFT)
        or (column == len(map_[0]) - 1 and direction == RIGHT)
    )


def part_1_solution(file_path: str) -> int:
    map_, row, column, direction = read_input(file_path)

    def next_step(row, column, direction):
        x, y = direction
        next_grid = map_[row + y][column + x]
        if next_grid == "#":
            return row, column, turn_right(direction)
        return row + y, column + x, direction

    visited = {(column, row)}

    while True:
        if is_edge(map_, column, row, direction):
            break
        row, column, direction = next_step(row, column, direction)
        visited.add((column, row))
    return len(visited)


def part_2_solution(file_path: str) -> int:
    with open(file_path, 'r') as input_file:
        raw_input = input_file.read().strip("\n")
        lab_map = {}
        start = None
        for y, line in enumerate(raw_input.splitlines()):
            for x, grid in enumerate(line):
                if grid == "^":
                    start = (x, y)
                lab_map[(x, y)] = grid
    if start is None:
        raise ValueError("Cannot find starting point")

    def recurse(updated_map) -> tuple[set[tuple[int, int]], bool]:
        position, direction, seen = start, UP, set()
        while position in updated_map and (position, direction) not in seen:
            seen |= {(position, direction)}
            x, y = position
            i, j = direction
            if updated_map.get((x+i, y+j)) == "#":
                direction = (-j, i)
            else:
                position = (x+i, y+j)
        return {p for p, _ in seen}, (position, direction) in seen

    path = recurse(lab_map)[0]
    return sum(recurse(lab_map | {o: '#'})[1] for o in path)


if __name__ == "__main__":
    assert part_1_solution("data/day6-test-case.txt") == 41
    print("Test case passed for part 1")
    print(part_1_solution("data/day6.txt"))
    assert part_2_solution("data/day6-test-case.txt") == 6
    print("Test case passed for part 2")
    print(part_2_solution("data/day6.txt"))  # 1933

    # G = {i + j * 1j: c for i, r in enumerate(open("data/data.txt"))
    #      for j, c in enumerate(r.strip())}
    #
    # start = min(p for p in G if G[p] == '^')
    #
    # def walk(G):
    #     pos, dir, seen = start, -1, set()
    #     while pos in G and (pos, dir) not in seen:
    #         seen |= {(pos, dir)}
    #         if G.get(pos + dir) == "#":
    #             dir *= -1j
    #         else:
    #             pos += dir
    #     return {p for p, _ in seen}, (pos, dir) in seen
    #
    # path = walk(G)[0]
    # print(len(path), sum(walk(G | {o: '#'})[1] for o in path))
