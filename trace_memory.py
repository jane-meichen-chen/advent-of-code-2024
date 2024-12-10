import sys
import tracemalloc


DAY = sys.argv[1]
tracemalloc.start()
__import__(f"day{DAY}").part_1_solution(f"data/day{DAY}.txt")
print(tracemalloc.get_traced_memory())
tracemalloc.stop()

tracemalloc.start()
__import__(f"day{DAY}").part_2_solution(f"data/day{DAY}.txt")
print(tracemalloc.get_traced_memory())
tracemalloc.stop()
