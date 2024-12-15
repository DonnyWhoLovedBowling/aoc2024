from collections import defaultdict
from itertools import islice, chain
from copy import deepcopy
from re import findall
from math import floor


def are_neighbours(v1, v2):
    return abs(v1[0]-v2[0]) < 2 and abs(v1[1]-v2[1]) < 2


class Robot:
    def __init__(self, x, y, vx, vy ):
        self._x = x
        self._y = y
        self._vx = vx
        self._vy = vy
        self._n_steps = 0
        self.has_neighbour = False

    def __repr__(self):
        return f"p: ({self._x}, {self._y}), v: ({self._vx}, {self._vy})"

    def do_n_steps(self, n):
        global height, width
        self._y = (self._y + (n*self._vy)) % height
        self._x = (self._x + (n*self._vx)) % width
        self._has_neighbour = False

    def get_pos(self):
        return self._x, self._y

    def get_q(self):
        global height, width
        b_y = floor(height/2.)
        b_x = floor(width/2.)
        if self._y < b_y and self._x < b_x:
            return 1
        if self._y > b_y and self._x < b_x:
            return 2
        if self._y < b_y and self._x > b_x:
            return 3
        if self._y > b_y and self._x > b_x:
            return 4

    @property
    def has_neighbour(self):
        return self._has_neighbour

    @has_neighbour.setter
    def has_neighbour(self, value):
        self._has_neighbour = value


def print_robots(_robots):
    global width, height
    for _i in range(height):
        _line = ''
        for j in range(width):
            if (j, _i) in _robots.keys() and _robots[(j, _i)] > 0:
                _line += str(_robots[(j, _i)])
            else:
                _line += '.'
        print(_line)


if __name__ == '__main__':
    in_file = open("../data/ex14.txt")
    lines = [l.replace('\\n', '').strip() for l in in_file.readlines()]
    height, width = 103, 101
    robot_map = defaultdict(int)
    robots_1 = []
    for i, line in enumerate(lines):
        nums = [int(n) for n in findall(r'-?\d*\.{0,1}\d+', line)]
        robots_1.append(Robot(*nums))

    print(robots_1)
    robots_2 = deepcopy(robots_1)

    robot_map = defaultdict(int)
    q_map = defaultdict(int)
    for r in robots_1:
        r.do_n_steps(100)
        robot_map[r.get_pos()] += 1
        q_map[r.get_q()] += 1

    ans_1 = 1
    for k,v in q_map.items():
        if k is None:
            continue
        ans_1 *= v

    print(ans_1)
    _iter = 0

    threshold = .7
    for r in robots_2:
        r.do_n_steps(_iter)
    high_neighbour_iters = []

    while True:
        robot_map = defaultdict(int)
        neighbours = set()
        no_neighbours = set()
        for r in robots_2:
            r.do_n_steps(1)
            robot_map[r.get_pos()] += 1
        _iter += 1
        for i, r1 in enumerate(robots_2):
            for j, r2 in enumerate(robots_2):
                if r2.has_neighbour or i == j:
                    continue
                if are_neighbours(r1.get_pos(), r2.get_pos()):
                    r1.has_neighbour = True
                    r2.has_neighbour = True
                    neighbours.add(i)
                    neighbours.add(j)
                    break
            if not r1.has_neighbour:
                no_neighbours.add(r1)
            # if len(no_neighbours) > ((1- threshold) * len(robots_2)):
            #     break

        if len(neighbours) > (0.5*len(robots_2)):
            high_neighbour_iters.append(_iter)
            odd_i = islice(high_neighbour_iters, 0, None, 2)
            even_i = islice(high_neighbour_iters, 1, None, 2)
            print(list(chain(odd_i)))
            print(list(chain(even_i)))
            print()

        if len(neighbours) > (threshold*len(robots_2)):
        # if True:
            print_robots(robot_map)
            print(_iter, float(len(neighbours)) / float(len(robots_2)))
            break






