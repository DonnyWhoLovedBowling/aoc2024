import numpy as np
from re import findall
#
#
# |ba[0] bb[0]| |a|    pr[0]
# |ba[1] bb[1]| |b|  = pr[1]
#
#
class Machine:
    def __init__(self, _a, _b, _prize):
        self.button_a = a
        self.button_b = b
        self.prize = _prize
        self.pushes = []
    def __repr__(self):
        return str(self.button_a) + ' ' + str(self.button_b) + ' ' + str(self.prize)

    def solve(self):
        p = np.array(self.prize)
        m = np.array([[self.button_a[0], self.button_b[0]], [self.button_a[1], self.button_b[1]]])
        try:
            x = np.linalg.solve(m, p)
            self.pushes = x
        except np.linalg.LinAlgError:
            return 0
        if (not round(self.pushes[0], 3).is_integer()) or (not round(self.pushes[1], 3).is_integer()):
            return 0
        self.pushes = round(self.pushes[0]), round(self.pushes[1])
        p_calc = np.matmul(m, np.array(self.pushes))
        if p_calc[0] == p[0] and p_calc[1] == p[1] and self.pushes[0] >= 0 and self.pushes[1] >= 0:
            return 3*self.pushes[0] + self.pushes[1]
        return 0

    def adjust(self):
        add = np.int64(10000000000000)
        self.prize = np.int64(add + self.prize[0]), np.int64(add + self.prize[1])

if __name__ == '__main__':
    in_file = open("data/ex13.txt")
    lines = [l.replace('\\n', '').strip() for l in in_file.readlines()]
    machines = []
    ans_1 = 0
    for line in lines:
        nums = [int(n) for n in findall(r'[0-9]+', line)]

        if 'A' in line:
            a = [nums[0], nums[1]]
        if 'B' in line:
            b = [nums[0], nums[1]]
        if 'P' in line:
            prize = [nums[0], nums[1]]
            machine = Machine(a, b, prize)
            machines.append(machine)
            ans_1 += machine.solve()
    print(ans_1)
    ans_2 = 0
    for machine in machines:
        machine.adjust()
        ans_2 += machine.solve()
    print(f'{ans_2:.20f}'
)




