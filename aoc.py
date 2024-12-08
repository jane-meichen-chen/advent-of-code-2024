from sys import argv


day = argv[1]
print(__import__(f"day{day}").part_1_solution(f"data/day{day}.txt"))
print(__import__(f"day{day}").part_2_solution(f"data/day{day}.txt"))
