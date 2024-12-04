import re


def mul(a, b):
    return a * b


def part_1_solution(file_path: str) -> int:
    summed_value = 0
    with open(file_path, "r") as input_file:
        for line in input_file:
            valid_operations = re.findall(r"mul\(\d+,\d+\)", line)
            for op in valid_operations:
                summed_value += eval(op)
    return summed_value


def part_2_solution(file_path: str) -> int:
    summed_value = 0
    disabled = False
    with open(file_path, "r") as input_file:
        for line in input_file:
            valid_operations = re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", line)
            for op in valid_operations:
                if op == "don't()":
                    disabled = True
                elif op == "do()":
                    disabled = False
                elif not disabled:
                    summed_value += eval(op)
    return summed_value


if __name__ == "__main__":
    assert part_1_solution("data/day3-test-case1.txt") == 161
    print(part_1_solution("data/day3.txt"))
    assert part_2_solution("data/day3-test-case2.txt") == 48
    print(part_2_solution("data/day3.txt"))
