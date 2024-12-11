from collections import defaultdict
from copy import deepcopy as dc

number_map = defaultdict(list)
init_input_map = defaultdict(int)


def process_number(_i):
    if _i in number_map:
        ans = number_map[_i]
    elif int(_i) == 0:
        ans = ['1']
    elif len(_i) % 2 == 0:
        ans = [str(int(_i[0:int(len(_i)/2):])), str(int(_i[int(len(_i)/2):]))]
    else:
        ans = [str(2024*int(_i))]
    return ans


def do_loop(_input_map, _n):
    input_map = dc(_input_map)
    for _ in range(_n):
        new_input_map = defaultdict(int)
        for k, v in input_map.items():
            new_list = process_number(k)
            for n in new_list:
                if n in new_input_map:
                    new_input_map[n] += v
                else:
                    new_input_map[n] = v
        input_map = dc(new_input_map)

    print(sum(input_map.values()))


_input = '6571 0 5851763 526746 23 69822 9 989'.split(' ')
for i in set(_input):
    init_input_map[i] = _input.count(i)

do_loop(init_input_map, 25)
do_loop(init_input_map, 75)
