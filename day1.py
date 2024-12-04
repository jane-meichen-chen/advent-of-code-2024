from collections import Counter
from heapq import heappush, heappop


def part_1_solution(file_path: str):
    left = []
    right = []
    with open(file_path) as input_data:
        for line in input_data:
            l, r = line.split("   ")
            heappush(left, int(l))
            heappush(right, int(r))

    total_distance = 0
    while left or right:
        l_value = heappop(left)
        r_value = heappop(right)
        total_distance += abs(l_value - r_value)
    return total_distance


def part_2_solution(file_path: str):
    left = []
    right = []
    with open(file_path) as input_data:
        for line in input_data:
            l, r = line.split("   ")
            heappush(left, int(l))
            heappush(right, int(r))

    left_counter = Counter(left)
    right_counter = Counter(right)
    similarity_score = 0
    for key, value in left_counter.items():
        similarity_score += key * right_counter.get(key, 0) * value
    return similarity_score


if __name__ == "__main__":
    assert part_1_solution("data/day1-test-case.txt") == 11
    print(part_1_solution("data/day1.txt"))
    assert part_2_solution("data/day1-test-case.txt") == 31
    print(part_2_solution("data/day1.txt"))
