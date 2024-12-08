from timeit import timeit


DAY = 5
print(timeit(lambda: __import__(f"day{DAY}").part_1_solution(f"data/day{DAY}.txt"), number=100))
print(timeit(lambda: __import__(f"day{DAY}").part_2_solution(f"data/day{DAY}.txt"), number=100))
