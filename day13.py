import re
from pathlib import Path


def cosine_similarity(A: list[int], B: list[int]) -> int:
    dot_product = sum(a * b for a, b in zip(A, B))
    mag_a = sum(a * a for a in A) ** 0.5
    mag_b = sum(b * b for b in B) ** 0.5
    return dot_product / (mag_a * mag_b)


def token_count(ax, ay, bx, by, px, py) -> int:
    if cosine_similarity([ax, ay], [bx, by]) == 1:
        ca, cb = -1, -1
        if px % bx == 0 and py % by == 0 and px // bx == py // by:
            cb = px // bx
        if px % ax == 0 and py % ay == 0 and px // ax == py // by:
            ca = px // ax
        if ca > -1 and cb > -1:
            return min(ca * 3, cb)
        if ca > -1:
            return ca * 3
        if cb > -1:
            return cb
        return 0

    cb = (py * ax - ay * px) / (by * ax - ay * bx)
    ca = (px - bx * cb) / ax
    if not ca.is_integer() or not cb.is_integer():
        return 0
    return 3 * ca + cb


def part_1_solution(file_path: str) -> int:
    tokens = 0
    pattern = (
        r"Button A: X\+(?P<ax>\d+), Y\+(?P<ay>\d+)\n"
        r"Button B: X\+(?P<bx>\d+), Y\+(?P<by>\d+)\n"
        r"Prize: X=(?P<px>\d+), Y=(?P<py>\d+)"
    )
    with open(file_path, "r") as input_file:
        for values in re.findall(pattern, input_file.read()):
            ax, ay, bx, by, px, py = list(map(int, values))
            tokens += token_count(ax, ay, bx, by, px, py)
    return tokens


def part_2_solution(file_path: str) -> int:
    tokens = 0
    pattern = (
        r"Button A: X\+(?P<ax>\d+), Y\+(?P<ay>\d+)\n"
        r"Button B: X\+(?P<bx>\d+), Y\+(?P<by>\d+)\n"
        r"Prize: X=(?P<px>\d+), Y=(?P<py>\d+)"
    )
    with open(file_path, "r") as input_file:
        for values in re.findall(pattern, input_file.read()):
            ax, ay, bx, by, px, py = list(map(int, values))
            px += 10_000_000_000_000
            py += 10_000_000_000_000
            tokens += token_count(ax, ay, bx, by, px, py)
    return tokens


if __name__ == "__main__":
    day = Path(__file__).stem
    assert part_1_solution(f"data/{day}-test-case.txt") == 480
    print("%.0f" % part_1_solution(f"data/{day}.txt"))
    assert part_2_solution(f"data/{day}-test-case.txt") == 875318608908
    print("%.0f" % part_2_solution(f"data/{day}.txt"))
