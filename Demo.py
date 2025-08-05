import multiprocessing
import time

def square(index, value):
    value[index] = value[index] ** 2

start = time.perf_counter()

value = multiprocessing.Array('i', [1, 2, 5, 3, 4])
processes = []

for i in range(5):  # 5 numbers = 5 processes
    p = multiprocessing.Process(target=square, args=(i, value))
    p.start()
    processes.append(p)

for process in processes:
    process.join()

print(list(value))

end = time.perf_counter()
print(f"The program finished in {round(end - start, 2)} seconds")
