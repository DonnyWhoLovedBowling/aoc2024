from threading import Thread, Lock
from itertools import product
import time

def calc_line(_i: int, _pt2: bool, lock: Lock):
    global lines, ans
    line = lines[_i]
    target = int(line.split(':')[0])
    numbers = [int(i.strip()) for i in line.split(':')[1].strip().split(' ')]
    operator_sets = list(product('+*|', repeat=len(numbers) - 1))
    for operator_set in list(operator_sets):
        total = numbers[0]
        for _i in range(1, len(numbers)):
            operator = operator_set[_i - 1]
            if operator == '+':
                total += numbers[_i]
            elif _pt2 and operator == '|':
                total = int(str(total) + str(numbers[_i]))
            else:
                total *= numbers[_i]
            if total > target:
                break
            if total == target:
                lock.acquire()
                ans += total
                lock.release()
                return


if __name__ == '__main__':
    in_file = open("../data/ex7.txt")
    lines = [l.replace('\\n', '').strip() for l in in_file.readlines()]
    ans = 0
    l = Lock()
    start = time.time()

    for pt2 in [False, True]:
        processes = []
        start = time.time()
        for i in range(len(lines)):
            calc_line(i, pt2, l)
        end = time.time()
        print(ans, ', took: ', round(end - start, 2), ' seconds')

    ans = 0
    for pt2 in [False, True]:
        processes = []
        start = time.time()

        for i in range(len(lines)):
            p = Thread(target=calc_line, args=(i, pt2, l))
            processes.append(p)
            p.start()
        for p in processes:
            p.join()
        end = time.time()
        print(ans, ', took: ', round(end - start, 2), ' seconds')
    exit()
