import math
from pathlib import Path


def blink(stones: list[int], memory: dict[int, list[int]]) -> tuple[list[int], dict[int, list[int]]]:
    new_order = []
    for stone in stones:
        if stone not in memory:
            digits = int(math.log10(stone)) + 1
            if digits % 2 == 0:
                multiplier = 10 ** (digits // 2)
                left = stone // multiplier
                right = stone - left * multiplier
                memory[stone] = [left, right]
            else:
                memory[stone] = [stone * 2024]
        new_order += memory[stone]
    return new_order, memory


def part_1_solution(file_path: str) -> int:
    with open(file_path) as file_input:
        stones = map(int, file_input.read().strip("\n").split(" "))

    # memory = {0: [1]}
    # for _ in range(25):
    #     stones, memory = blink(stones, memory)
    # return len(stones)
    return sum(get_stone_score(stone, 25, {}) for stone in stones)


def get_stone_score(stone: int, remaining_blink: int, memory: dict[(int, int): int]) -> int:
    if remaining_blink == 0:
        return 1
    if (stone, remaining_blink) not in memory:
        if stone == 0:
            return get_stone_score(1, remaining_blink - 1, memory)
        digits = int(math.log10(stone)) + 1
        if digits % 2 == 0:
            multiplier = 10 ** (digits // 2)
            left = stone // multiplier
            right = stone - left * multiplier
            memory[(stone, remaining_blink)] = get_stone_score(left, remaining_blink - 1, memory) + get_stone_score(right, remaining_blink - 1, memory)
        else:
            memory[(stone, remaining_blink)] = get_stone_score(stone * 2024, remaining_blink - 1, memory)
    return memory[(stone, remaining_blink)]


def part_2_solution(file_path: str) -> int:
    with open(file_path) as file_input:
        stones = map(int, file_input.read().strip("\n").split(" "))
    return sum(get_stone_score(stone, 75, {}) for stone in stones)


if __name__ == "__main__":
    day = Path(__file__).stem
    assert part_1_solution(f"data/{day}-test-case.txt") == 55312
    print("test case passed")
    print(part_1_solution(f"data/{day}.txt"))
    print(part_2_solution(f"data/{day}.txt"))
