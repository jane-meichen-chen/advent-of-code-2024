import tracemalloc


DAY = 4
tracemalloc.start()
__import__(f"day{DAY}").part_1_solution(f"data/day{DAY}.txt")
tracemalloc.stop()
print(tracemalloc.get_traced_memory())

tracemalloc.start()
__import__(f"day{DAY}").part_2_solution(f"data/day{DAY}.txt")
tracemalloc.stop()
print(tracemalloc.get_traced_memory())
