def combo(_operand, a):
    global B, C
    if _operand < 4:
        return _operand
    if _operand == 4:
        return  a
    if _operand == 5:
        return B
    if _operand == 6:
        return C

def run_program(_opcode, a_orig):
    global B, C, last_hit, threshold
    a = a_orig
    _ix = 0
    _out = []
    while _ix < len(_opcode):
        op = _opcode[_ix]
        operand = _opcode[_ix + 1]
        inc_by_2 = True

        if op == 0:
            a = int(a / pow(2, combo(operand, a)))
        elif op == 1:
            B = B ^ operand
        elif op == 2:
            B = (combo(operand, a) % 8)
        elif op == 3:
            if a != 0:
                inc_by_2 = False
                _ix = operand
        elif op == 4:
            B = B ^ C
        elif op == 5:
            new_out = combo(operand, a) % 8
            _out.append(new_out)

        elif op == 6:
            print('did B!')
            B = int(a / pow(2, combo(operand, a)))
        elif op == 7:
            C = int(a / pow(2, combo(operand, a)))
        else:
            print('?')
        if inc_by_2:
            _ix += 2

    return _out


if __name__ == '__main__':
    in_file = open("../data/ex17.txt")
    lines = [l.replace('\\n', '').strip() for l in in_file.readlines()]
    A_cor, B, C = 0, 0, 0
    last_hit = 0
    threshold = 0
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

    print(run_program(opcode, A_cor))
    A_new = 1
    out = []
    ix = len(opcode)-1
    target_number = [opcode[ix]]
    ix_rels = []
    while True:
        out = run_program(opcode, A_new)
        if out == opcode:
            break
        if out == target_number:
            ix_rels.append(A_new-pow(8, len(opcode)-(ix+1)))
            A_new = pow(8, len(opcode)-ix)+8*(ix_rels[-1])
            ix -= 1
            target_number = [opcode[ix]] + target_number
        else:
            A_new += 1

    print(A_new)

