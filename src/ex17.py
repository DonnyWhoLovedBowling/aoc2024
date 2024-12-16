from collections import defaultdict

def combo(_operand, A):
    global B, C
    if _operand < 4:
        return _operand
    if _operand == 4:
        return  A
    if _operand == 5:
        return B
    if _operand == 6:
        return C

def run_program(_opcode, A_orig, pt2=False):
    global B, C
    A = A_orig
    ix = 0
    out = []
    while ix < len(_opcode):
        op = _opcode[ix]
        operand = _opcode[ix + 1]
        inc_by_2 = True

        if op == 0:
            A = int(A / pow(2, combo(operand, A)))
        elif op == 1:
            B = B ^ operand
        elif op == 2:
            B = (combo(operand, A) % 8)
        elif op == 3:
            if A != 0:
                inc_by_2 = False
                ix = operand
        elif op == 4:
            B = B ^ C
        elif op == 5:
            new_out = combo(operand, A) % 8
            if pt2:
                if len(out) >= len(_opcode):
                    return []
                if _opcode[len(out)] != new_out:
                    return []
            out.append(new_out)
        elif op == 6:
            B = int(A / pow(2, combo(operand, A)))
        elif op == 7:
            C = int(A / pow(2, combo(operand, A)))
        else:
            print('?')
        if inc_by_2:
            ix += 2

    return out


if __name__ == '__main__':
    in_file = open("../data/ex17.txt")
    lines = [l.replace('\\n', '').strip() for l in in_file.readlines()]
    A_cor, B, C = 0,0,0
    opcode = []
    for line in lines:
        if 'A' in line:
            A_cor = int(line.split(':')[1])
        elif 'B' in line:
            B = int(line.split(':')[1])
        elif 'C' in line:
            C = int(line.split(':')[1])
        elif line == '':
            continue
        else:
            opcode = [int(n) for n in line.split(':')[1].split(',')]

    # out = run_program(opcode, A_cor)
    # print(out)
    A_new = 0
    out = []
    while out != opcode:
        out = run_program(opcode, A_new, True)
        A_new += 1
        if A_new % 100000 == 0:
            print(A_new)
    print(A_new)

