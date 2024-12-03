from copy import deepcopy as dc

in_file = open("../data/ex2.txt")
lines = [l.replace('\\n', '') for l in in_file.readlines()]
reports = []
n_safe_1 = 0
n_safe_2 = 0


def is_safe(_diff, _last_direction):
    direction = diff < 0
    if not (0 < abs(_diff) < 4):
        return False
    if (_last_direction is not None) and (direction != _last_direction):
        return False
    return True


for line in lines:
    unsafe = False
    unsafe_2 = False
    retries = 0
    report = [int(c) for c in line.split()]
    last_direction = None
    for i in range(len(report)-1):
        diff = report[i] - report[i+1]
        unsafe = not is_safe(diff,last_direction)
        if unsafe:
            break
        last_direction = diff < 0
    if unsafe:
        for j in range(len(report)):
            report_2 = dc(report)
            report_2.pop(j)
            last_direction = None
            for i in range(len(report_2) - 1):
                diff = report_2[i] - report_2[i + 1]
                unsafe_2 = not is_safe(diff, last_direction)
                if unsafe_2:
                    break
                last_direction = diff < 0
            if not unsafe_2:
                n_safe_2 += 1
                break
    else:
        n_safe_1 += 1

print(n_safe_1)
print(n_safe_2+n_safe_1)



