def add_vecs(v1, v2, factor=1):
    return v1[0]+(factor*v2[0]), v1[1]+(factor*v2[1])

def move_recursive(delta, to_be_moved, full_set: set=None):
    global boxes_l, boxes_r, walls_2, robot_2
    new_to_be_moved = set()
    full_set.update(to_be_moved)
    for p in to_be_moved:
        new_pos = add_vecs(p, delta)

        if new_pos in walls_2:
            return False
        elif new_pos in boxes_l or new_pos in boxes_r:
            if delta[1] != 0:
                if new_pos in boxes_r:
                    new_to_be_moved.add(new_pos)
                    new_to_be_moved.add(add_vecs(new_pos, (-1, 0)))
                if new_pos in boxes_l:
                    new_to_be_moved.add(new_pos)
                    new_to_be_moved.add(add_vecs(new_pos, (1, 0)))
            else:
                new_to_be_moved.add(new_pos)
        if not move_recursive(delta, new_to_be_moved, full_set):
            return False
    return True

def move(delta):
    global walls, boxes, robot
    new_robot_pos = add_vecs(robot, delta)
    cursor = new_robot_pos
    while True:
        if cursor in walls:
            new_robot_pos = robot
            break
        if cursor in boxes:
            cursor = add_vecs(cursor, delta)
            continue
        else:
            break
    if new_robot_pos == robot:
        return
    elif new_robot_pos in boxes:
        boxes.remove(new_robot_pos)
        boxes.add(cursor)
        robot = new_robot_pos
    else:
        robot = new_robot_pos

def move_shit(delta):
    global boxes_l, boxes_r, walls_2, robot_2
    shit_to_be_moved = set()
    if not move_recursive(delta, {robot_2}, shit_to_be_moved):
        return
    robot_2 = add_vecs(robot_2, delta)

    to_be_moved_r = shit_to_be_moved.intersection(boxes_r)
    to_be_moved_l = shit_to_be_moved.intersection(boxes_l)
    boxes_r.difference_update(to_be_moved_r)
    boxes_l.difference_update(to_be_moved_l)

    for _b in to_be_moved_r:
        boxes_r.add(add_vecs(_b, delta))
    for _b in to_be_moved_l:
        boxes_l.add(add_vecs(_b, delta))

def print_warehouse(_size):
    global boxes, walls, robot
    for _i in range(_size):
        _line = ''
        for _j in range(_size):
            if (_j, _i) in boxes:
                _line += 'O'
            elif (_j, _i) in walls:
                _line += '#'
            elif (_j, _i) == robot:
                _line += '@'
            else:
                _line += '.'
        print(_line)

def print_warehouse_2(_size):
    global boxes_l, boxes_r, walls_2, robot_2
    for _i in range(int(_size / 2)):
        _line = ''
        for _j in range(_size):
            if (_j, _i) in boxes_l:
                _line += '['
            elif (_j, _i) in boxes_r:
                _line += ']'
            elif (_j, _i) in walls_2:
                _line += '#'
            elif (_j, _i) == robot_2:
                _line += '@'
            else:
                _line += '.'
        print(_line)


if __name__ == '__main__':
    in_file = open("../data/ex15.txt")
    lines = [l.replace('\\n', '').strip() for l in in_file.readlines()]
    walls = set()
    walls_2 = set()

    boxes = set()
    boxes_l = set()
    boxes_r = set()

    robot = ()
    robot_2 = ()

    for i, line in enumerate(lines):
        if line.strip().replace('\\n', '') == '':
            print_warehouse_2(len(lines[0]) * 2)
        for j, c in enumerate(line):
            if c == '#':
                walls.add((j, i))
                walls_2.add(((j*2), i))
                walls_2.add(((j*2)+1, i))
            elif c == 'O':
                boxes.add((j, i))
                boxes_l.add(((2*j), i))
                boxes_r.add(((2*j)+1, i))
            elif c == '@':
                robot = (j, i)
                robot_2 = (j*2, i)
            elif c == '>':
                move((1, 0))
                move_shit((1, 0))
            elif c == '<':
                move((-1, 0))
                move_shit((-1, 0))
            elif c == 'v':
                move((0, 1))
                move_shit((0, 1))
            elif c == '^':
                move((0, -1))
                move_shit((0, -1))
            # if c in '><^v':
            #     print(c)
            #     print_warehouse_2(len(lines[0]) * 2)

    ans_1 = 0
    size = len(lines[0])*2
    # print_warehouse(len(lines[0]))
    print_warehouse_2(size)

    for b in boxes:
        ans_1 += (b[0]+100*b[1])
    print(ans_1)

    ans_2 = 0
    for b in boxes_l:
        y = b[1]
        x = b[0]
        ans_2 += (x+100*y)
    print(ans_2)




