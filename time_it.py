import sys
from timeit import timeit


DAY = sys.argv[1]
print(timeit(lambda: __import__(f"day{DAY}").part_1_solution(f"data/day{DAY}.txt"), number=10))
print(timeit(lambda: __import__(f"day{DAY}").part_2_solution(f"data/day{DAY}.txt"), number=10))
