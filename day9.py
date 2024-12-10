from copy import deepcopy
from pathlib import Path


def part_1_solution(file_path: str) -> int:
    with open(file_path, 'r') as input_file:
        input_string = input_file.read().strip("\n")

    is_file = True
    file_id = 0
    represents = []
    for block in input_string:
        if is_file:
            represents += [file_id for _ in range(int(block))]
        else:
            represents += [None for _ in range(int(block))]
        file_id += is_file
        is_file = not is_file

    left = 0
    right = len(represents) - 1
    result = 0
    while left <= right:
        if represents[left] is None and represents[right] is not None:
            represents[left] = represents[right]
            represents[right] = None
        while right > 0 and represents[right] is None:
            right -= 1
        while left < len(represents) and represents[left] is not None:
            result += left * int(represents[left])
            left += 1
    return result


def part_2_solution(file_path: str) -> int:
    with open(file_path, 'r') as input_file:
        input_string = input_file.read().strip("\n")

    disk = [(None, int(block)) if index % 2 else (index // 2, int(block)) for index, block in enumerate(input_string)]

    sorted_disk = deepcopy(disk)
    reversed_files = reversed([file for file in disk if file[0] is not None])
    for file_id, size in reversed_files:
        possible_moves = [block for block in sorted_disk if block[0] is None and block[1] >= size]
        if possible_moves:
            fill_id, fill_size = possible_moves[0]
            fill_index = sorted_disk.index((fill_id, fill_size))
            replace_index = sorted_disk.index((file_id, size))
            if fill_index > replace_index:
                continue
            sorted_disk[fill_index] = (fill_id, fill_size - size)
            sorted_disk[replace_index] = (None, size)
            sorted_disk.insert(fill_index, (file_id, size))

    def mul(x):
        a, b = x
        if a is None or b is None:
            return 0
        return a * b

    return sum(map(mul, enumerate(item for block in sorted_disk for item in [block[0] for _ in range(block[1])])))


if __name__ == "__main__":
    day = Path(__file__).stem
    # assert part_1_solution(f"data/{day}-test-case.txt") == 1928
    # print("test case passed")
    # print(part_1_solution(f"data/{day}.txt"))
    # assert part_2_solution(f"data/{day}-test-case.txt") == 2858
    # print("test case passed")
    print(part_2_solution(f"data/{day}.txt"))
