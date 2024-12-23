from copy import deepcopy

def add_vecs(v1, v2, factor=1):
    return v1[0]+(factor*v2[0]), v1[1]+(factor*v2[1])

def subtract(v1, v2):
    return v1[0]-v2[0], v1[1]-v2[1]


def determine_direction_directional(pos, target):
    move = subtract(target, pos)

    my = move[1]
    mx = move[0]
    if move == (0, 0):
        return 0, 0

    action = (0, 0)
    if pos == (0, 1):
        if mx < 0:
            action = (0, 0)
        elif my < 0:
            action = (1, 0)
        elif my > 0:
            action = (1, 0)
        elif mx > 0:
            action = (1, 0)

    if pos == (2, 1):
        if mx > 0:
            action = (0, 0)
        elif my < 0:
            action = (-1, 0)
        elif my > 0:
            action = (-1, 0)
        elif mx < 0:
            action = (-1, 0)

    if pos == (1, 0):
        if my > 0:
            action = (0, 1)
        elif my < 0:
            print('?')
        elif mx < 0:
            action = (0, 1)
        elif mx > 0:
            action = (1, 0)

    if pos == (1, 1):
        if my < 0:
            action = (0, -1)
        elif my > 0:
            print('?')
        elif mx < 0:
            action = (-1, 0)
        elif mx > 0:
            action = (1, 0)

    if pos == (2, 0):
        if my > 0:
            action = (-1, 0)
        elif mx > 0:
            action = (0, 1)
        elif my < 0:
            action = (-1, 0)
        elif mx < 0:
            action = (-1, 0)

    return action

def determine_direction_main(pos, target, pos_parent):
    move = subtract(target, pos)

    my = move[1]
    mx = move[0]
    if move == (0, 0):
        return 0, 0

    action = (0, 0)
    if pos == (0, 2):
        if my > 0 and mx > 0:
            action = (1, 0)
        elif my < 0:
            action = (0, -1)
        elif mx > 0:
            action = (1, 0)
        else:
            print('?', pos, move)

    elif pos == (1, 3):
        if my < 0 and mx < 0 :
            action = (0, -1)
        elif mx > 0:
            action = (1, 0)
        elif my < 0:
            action = (0, -1)
        else:
            print('?', pos, move)
    else:
        if my > 0:
            action = (0, 1)
        elif my < 0:
            action = (0, -1)
        elif mx > 0:
            action = (1, 0)
        elif mx < 0:
            action = (-1, 0)

    return action



if __name__ == '__main__':
    in_file = open("../data/ex21.txt")
    lines = [l.replace('\\n', '').strip() for l in in_file.readlines()]
    numeric_coordinate_map = {'7': (0, 0), '8': (1, 0), '9': (2, 0),
                              '4': (0, 1), '5': (1, 1), '6': (2, 1),
                              '1': (0, 2), '2': (1, 2), '3': (2, 2),
                                           '0': (1, 3), 'A': (2, 3)
                              }

    directional_coordinate_map = {(0,  1): (1, 1), 'A':     (2, 0),
                                  (-1, 0): (0, 1), (0, -1): (1, 0),
                                  (1,  0): (2, 1)
                                  }
    pos_to_direction_map = dict()
    for k, v in directional_coordinate_map.items():
        pos_to_direction_map[v] = k

    character_map = {(0, 1): 'v', (1, 0): '>', (0, -1): '^', (-1, 0): '<', 'A': 'A'}

    robot_pos = [(2, 3), (2, 0), (2, 0)]
    out = ''
    for line in lines:
        for c in line:
            targets = [numeric_coordinate_map[c]]
            for ix_r in range(len(robot_pos)):
                new_targets = []
                new_pos = robot_pos[ix_r]
                for target in targets:
                    while True:
                        if ix_r == 0:
                            direction = determine_direction_main(new_pos, target)
                        else:
                            direction = determine_direction_directional(new_pos, target)
                        if direction == (0, 0):
                            new_targets.append(directional_coordinate_map['A'])
                            break
                        else:
                            new_targets.append(directional_coordinate_map[direction])
                            new_pos = add_vecs(new_pos, direction)
                targets = new_targets
                robot_pos[ix_r] = new_pos

                if ix_r == len(robot_pos)-1:
                    for m in targets:
                        out += character_map[pos_to_direction_map[m]]
        out += '\n'
    print(out)


