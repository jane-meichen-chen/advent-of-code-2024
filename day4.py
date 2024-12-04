SEARCH_TARGET = "XMAS"


def find_xmas(word_search: list[list[str]], row: int, column: int) -> int:
    count = 0
    # >
    count += (
        column + 4 <= len(word_search[0])
        and "".join(word_search[row][column:column + 4]) == SEARCH_TARGET
    )
    # <
    count += (
        column - 3 >= 0
        and "".join(word_search[row][column-3:column+1][::-1]) == SEARCH_TARGET
    )
    # v
    count += (
        row + 4 <= len(word_search)
        and (
            "".join(
                [
                    word_search[row][column],
                    word_search[row + 1][column],
                    word_search[row + 2][column],
                    word_search[row + 3][column],
                ]
            )
            == SEARCH_TARGET
        )
    )
    # ^
    count += (
        row - 3 >= 0
        and (
            "".join(
                [
                    word_search[row][column],
                    word_search[row - 1][column],
                    word_search[row - 2][column],
                    word_search[row - 3][column],
                ]
            )
            == SEARCH_TARGET
        )
    )
    # v>
    count += (
        column + 4 <= len(word_search[0])
        and row + 4 <= len(word_search)
        and "".join(
            [
                word_search[row][column],
                word_search[row + 1][column + 1],
                word_search[row + 2][column + 2],
                word_search[row + 3][column + 3],
            ]
        )
        == SEARCH_TARGET
    )
    # ^>
    count += (
        column + 4 <= len(word_search[0])
        and row - 3 >= 0
        and "".join(
            [
                word_search[row][column],
                word_search[row - 1][column + 1],
                word_search[row - 2][column + 2],
                word_search[row - 3][column + 3],
            ]
        )
        == SEARCH_TARGET
    )
    # <v
    count += (
        column - 3 >= 0
        and row + 4 <= len(word_search)
        and "".join(
            [
                word_search[row][column],
                word_search[row + 1][column - 1],
                word_search[row + 2][column - 2],
                word_search[row + 3][column - 3],
            ]
        )
        == SEARCH_TARGET
    )
    # <^
    count += (
        column - 3 >= 0
        and row - 3 >= 0
        and "".join(
            [
                word_search[row][column],
                word_search[row - 1][column - 1],
                word_search[row - 2][column - 2],
                word_search[row - 3][column - 3],
            ]
        )
        == SEARCH_TARGET
    )
    return count


def find_x_mas(word_search: list[list[str]], row: int, column: int) -> bool:
    if column + 2 > len(word_search[0]) or row + 2 > len(word_search) or column + 2 > len(word_search[0]) or row - 1 < 0 or column - 1 < 0:
        return False
    # \
    backward = [word_search[row - 1][column - 1], word_search[row][column], word_search[row + 1][column + 1]]
    # /
    forward = [word_search[row + 1][column - 1], word_search[row][column], word_search[row - 1][column + 1]]
    if "MAS" not in ["".join(backward), "".join(backward[::-1])]:
        return False
    if "MAS" not in ["".join(forward), "".join(forward[::-1])]:
        return False
    return True


def part_1_solution(file_path: str) -> int:
    with open(file_path, 'r') as input_file:
        word_search = [list(line.strip("\n")) for line in input_file]

    count = sum(find_xmas(word_search, row, column) for row, line in enumerate(word_search) for column, char in enumerate(line) if char == "X")
    return count


def part_2_solution(file_path: str) -> int:
    with open(file_path, 'r') as input_file:
        word_search = [list(line.strip("\n")) for line in input_file]

    count = sum(find_x_mas(word_search, row, column) for row, line in enumerate(word_search) for column, char in enumerate(line) if char == "A")
    return count


if __name__ == "__main__":
    assert part_1_solution("data/day4-test-case.txt") == 18
    print(part_1_solution("data/day4.txt"))
    assert part_2_solution("data/day4-test-case.txt") == 9
    print(part_2_solution("data/day4.txt"))
