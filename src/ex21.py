import re

def add_vecs(v1, v2, factor=1):
    return v1[0]+(factor*v2[0]), v1[1]+(factor*v2[1])

def subtract(v1, v2):
    return v1[0]-v2[0], v1[1]-v2[1]


def determine_direction_directional(pos, _target):
    move = subtract(_target, pos)

    my = move[1]
    mx = move[0]
    if move == (0, 0):
        return move

    action = (0, 0)
    if pos[1] == 0:
        if my == 1:
            return 0, 1
        else:
            return  mx/abs(mx), 0
    if pos[1] == 1:
        if abs(mx) > 0:
            return mx/abs(mx), 0
        else:
            return 0, -1


    return action

def determine_direction_main(pos, _target, _last_target):
    move = subtract(_target, pos)

    my = move[1]
    mx = move[0]
    if move == (0, 0):
        return 0, 0

    action = (0, 0)
    prioritize_x = True
    if _last_target in [(1, 3), (2, 3)] and _target[0] == 0 or (my > 0 and pos[0] != 0):
        prioritize_x = False
    if (prioritize_x and abs(mx) > 0) or my == 0:
        action = mx/abs(mx), 0
    elif (not prioritize_x and abs(my) > 0) or mx == 0:
        action = 0, my/abs(my)
    else:
        print('?')
    return action


def do_run(robot_pos):
    ans = 0
    seen = dict()

    for line in lines:
        last_target = (2, 3)
        out = ''
        for c in line:
            print('character ',  c)
            targets = [numeric_coordinate_map[c]]
            for ix_r in range(len(robot_pos)):
                print("robot nr: ", ix_r)
                new_targets = []
                new_pos = robot_pos[ix_r]
                for target in targets:
                    start_pos = new_pos
                    new_new_targets = []
                    if (target, start_pos, ix_r==0) in seen:
                        new_new_targets, new_pos = seen[(target, start_pos, ix_r==0)]
                    else:
                        while True:
                            if ix_r == 0:
                                direction = determine_direction_main(new_pos, target, last_target)
                            else:
                                direction = determine_direction_directional(new_pos, target)
                            if direction == (0, 0):
                                new_new_targets.append(directional_coordinate_map['A'])
                                break
                            else:
                                new_new_targets.append(directional_coordinate_map[direction])
                                new_pos = add_vecs(new_pos, direction)
                        seen[(target, start_pos, ix_r == 0)] = new_new_targets, new_pos
                    new_targets += new_new_targets

                targets = new_targets
                robot_pos[ix_r] = new_pos

                if ix_r == len(robot_pos)-1:
                    for m in targets:
                        out += character_map[pos_to_direction_map[m]]
            last_target = numeric_coordinate_map[c]
        numeric_part = int(re.findall('-?\\d+', line)[0])
        ans += len(out) * numeric_part
        print('intermediate score: ', ans)
    return ans



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
    print(do_run([(2, 3), (2, 0), (2, 0)]))
    print(do_run([(2, 3)] + 25 * [(2, 0)]))

