def add_vecs(v1, v2, factor=1):
    return v1[0]+(factor*v2[0]), v1[1]+(factor*v2[1])

def subtract(v1, v2):
    return v1[0]-v2[0], v1[1]-v2[1]

class BaseRobot:
    def __init__(self):
        self.pos = (2, 3)
        self.numeric_coordinate_map = {'7': (0, 0), '8': (1, 0), '9': (2, 0),
                                       '4': (0, 1), '5': (1, 1), '6': (2, 1),
                                       '1': (0, 2), '2': (1, 2), '3': (2, 2),
                                       '0': (1, 3), 'A': (2, 3)
                                        }
    def do_move(self, direction):
        self.pos = add_vecs(self.pos, direction)


class DirectionalRobot:
    def __init__(self, child_bot):
        self.pos = (2, 0)
        self.directional_coordinate_map = {(0,  1): (1, 1), 'A':     (2, 0),
                                           (-1, 0): (0, 1), (0, -1): (1, 0),
                                           (1,  0): (2, 1)
                                        }
        self.pos_to_direction_map = dict()
        for k, v in self.directional_coordinate_map.items():
            self.pos_to_direction_map[v] = k
        self.child_bot = child_bot

    def do_move(self, direction):
        if direction == 'A':
            direction_from_this_pos = self.pos_to_direction_map[self.pos]
            self.child_bot.do_move(direction_from_this_pos)
        else:
            self.pos = add_vecs(self.pos, direction)



if __name__ == '__main__':
    base_bot = BaseRobot()
    first_robot = DirectionalRobot(base_bot)
    second_robot = DirectionalRobot(first_robot)
    second_robot.do_move((-1, 0))
    second_robot.do_move((0, 1))
    second_robot.do_move((-1, 0))
    second_robot.do_move('A')

    print(base_bot.pos)
    print(first_robot.pos)
    print(second_robot.pos)
