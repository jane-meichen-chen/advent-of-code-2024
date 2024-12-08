import math
from pathlib import Path


def is_equation_possible(expected_result: int, number_components: list[int], concat_operator: bool = False) -> bool:
    if len(number_components) == 1:
        return expected_result == number_components[0]
    elif expected_result <= 0:
        return False
    *other, value = number_components
    if expected_result % value == 0 and is_equation_possible(expected_result // value, other, concat_operator):
        return True
    elif concat_operator and str(expected_result).endswith(str(value)):
        remaining_value = (expected_result - value) // 10 ** (int(math.log10(value)) + 1)
        if is_equation_possible(remaining_value, other, concat_operator):
            return True
    return is_equation_possible(expected_result - value, other, concat_operator)


def part_1_solution(file_path: str) -> int:
    total_calibration_result = 0
    with open(file_path, "r") as input_file:
        for line in input_file.read().strip("\n").split("\n"):
            result, components = line.split(": ")
            result = int(result)
            components = list(map(int, components.split(" ")))
            if is_equation_possible(result, components):
                total_calibration_result += result
    return total_calibration_result


def part_2_solution(file_path: str) -> int:
    total_calibration_result = 0
    with open(file_path, "r") as input_file:
        for line in input_file.read().strip("\n").split("\n"):
            result, components = line.split(": ")
            result = int(result)
            components = list(map(int, components.split(" ")))
            if is_equation_possible(result, components, concat_operator=True):
                total_calibration_result += result
    return total_calibration_result


if __name__ == "__main__":
    day = Path(__file__).stem
    assert part_1_solution(f"data/{day}-test-case.txt") == 3749
    print(part_1_solution(f"data/{day}.txt"))
    assert part_2_solution(f"data/{day}-test-case.txt") == 11387
    print(part_2_solution(f"data/{day}.txt"))  # 2971918631869 too low
