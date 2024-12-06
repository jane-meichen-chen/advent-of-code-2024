from collections import defaultdict


class IncorrectOrder(Exception):
    pass


def part_1_solution(file_path: str) -> int:
    rules = defaultdict(list)
    with open(file_path, 'r') as input_file:
        _rules, updates = input_file.read().strip("\n").split("\n\n")
        for line in _rules.split("\n"):
            before, after = line.split("|")
            rules[before].append(after)

        sum_page = 0
        for update in updates.split("\n"):
            update_list = update.split(",")
            try:
                for i in range(1,len(update_list)+1):
                    for j in range(len(update_list)-i):
                        if update_list[-i] not in rules[update_list[j]]:
                            raise IncorrectOrder
            except IncorrectOrder:
                continue
            else:
                sum_page += int(update_list[len(update_list)//2])
    return sum_page


class CustomNumber:
    def __init__(self, value, rules):
        self.rules: list[str] = rules
        self.value: str = value

    def __lt__(self, other: "CustomNumber"):
        return f"{self.value}|{other.value}" in self.rules


def part_2_solution(file_path: str) -> int:
    with open(file_path, 'r') as input_file:
        rules, updates = input_file.read().strip("\n").split("\n\n")
        rules = rules.split("\n")
        sum_page = 0
        for update in updates.split("\n"):
            update_list = [CustomNumber(value, rules) for value in update.split(",")]
            sorted_list = sorted(update_list)
            if sorted_list == update_list:
                continue
            sum_page += int(sorted_list[len(sorted_list)//2].value)
    return sum_page


if __name__ == "__main__":
    assert part_1_solution("data/day5-test-case.txt") == 143
    print(part_1_solution("data/day5.txt"))
    assert part_2_solution("data/day5-test-case.txt") == 123
    print(part_2_solution("data/day5.txt"))
