def add_vec(pos1, pos2):
    return pos1[0]+pos2[0], pos1[1]+pos2[1]


def turn_right(_direction):
    return _direction[1]*-1, _direction[0]


def do_loop(_obstacles):
    global startpos, startdir, lines
    _guard = startpos
    _direction = startdir
    _path = {_guard}
    mem = set()
    while True:
        new_pos = add_vec(_guard, _direction)
        if new_pos in _obstacles:
            _direction = turn_right(_direction)
        elif 0 > new_pos[0] or new_pos[0] >= len(lines) or 0 > new_pos[1] or new_pos[1] >= len(lines):
            break
        else:
            _guard = new_pos
            _path.add(_guard)
        key = (_guard, _direction)
        if key in mem:
            _path = set()
            break
        mem.add(key)
    return _path

if __name__ == '__main__':
    in_file = open("../data/ex6.txt")
    lines = [l.replace('\\n', '').strip() for l in in_file.readlines()]
    total_1 = 0
    total_2 = 0


    obstacles = {(j, i) for i in range(len(lines)) for j in range(len(lines)) if '#' ==  lines[i][j]}
    startpos = [(lines[i].index('^'), i) for i in range(len(lines)) if '^' in lines[i]][0]
    startdir = (0, -1)
    loops = 0

    path = do_loop(obstacles)
    print(len(path))

    for p in path:
        obstacles.add(p)
        if do_loop(obstacles) == set():
            loops += 1
        obstacles.remove(p)

    print(loops)
