from collections import Counter


def is_report_safe(report: list[int]) -> bool:
    if any(map(lambda v: v > 1, Counter(report).values())):
        return False
    elif report[0] < report[1]:
        direction = 1
    else:
        direction = -1

    prev = report[0]
    for level in report[1:]:
        if not 1 <= (level - prev) * direction <= 3:
            return False
        prev = level
    return True


def part_1_solution(file_path: str):
    safe_reports = 0
    with open(file_path) as input_data:
        for line in input_data:
            levels = list(map(int, line.split(" ")))
            if is_report_safe(levels):
                safe_reports += 1
    return safe_reports


def part_2_solution(file_path: str):
    safe_reports = 0
    with open(file_path) as input_data:
        for line in input_data:
            levels = list(map(int, line.split(" ")))
            if is_report_safe(levels):
                safe_reports += 1
            else:
                safe_reports += any(is_report_safe(levels[:i] + levels[i + 1:]) for i in range(len(levels)))
    return safe_reports


if __name__ == "__main__":
    assert part_1_solution("data/day2-test-case.txt") == 2
    print(part_1_solution("data/day2.txt"))
    assert part_2_solution("data/day2-test-case.txt") == 4
    print(part_2_solution("data/day2.txt"))

    # data = [[*map(int, l.split())] for l in open("data/day2.txt")]
    # f = lambda d: all(1 <= a - b <= 3 for a, b in zip(d, d[1:]))
    # g = lambda d: (d[:i] + d[i + n:] for i in range(len(d)))
    # for n in 0, 1: print(sum(any(f(e) or f(e[::-1]) for e in g(d)) for d in data))
