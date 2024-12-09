from itertools import chain

def visualize(full_string):
    _vis_string = []
    for e in full_string:
        _vis_string.append(e[0]*[e[1]])
    return list(chain(*_vis_string))


if __name__ == '__main__':
    in_file = open("../data/ex9.txt")
    line = [l.replace('\\n', '').strip() for l in in_file.readlines()][0]
    full_string_1 = []
    full_string_2 = []
    file_id = 0

    for i, num in enumerate(line):
        if i % 2 == 0:
            if num == '0':
                print('zero file size!')
            full_string_2.append((int(num), str(file_id)))
            full_string_1 += int(num) * [str(file_id)]
            file_id += 1
        else:
            full_string_2.append((int(num), '.'))
            full_string_1 += int(num) * '.'


    for i in range(len(full_string_1)):
        if full_string_1[i] == '.':
            full_string_1 = full_string_1[:i] + [full_string_1[-1]] + full_string_1[i + 1:-1]
        while full_string_1[-1] == '.':
            full_string_1 = full_string_1[:-1]
        if (i + 1) >= len(full_string_1):
            break

    ans_1 = 0
    for i,c in enumerate(full_string_1):
        ans_1 += i*int(c)
    print(ans_1)

    first_space = 0
    for i in range(-1, -1*len(full_string_2), -1):
        if i % 1000 == 0:
            print(i, len(full_string_2), first_space)
        if abs(i) > len(full_string_2):
            break
        elem_file = full_string_2[i]
        if elem_file[1] == '.':
            continue
        for j in range(0, len(full_string_2)):
            if j >= len(full_string_2)+i:
                break
            elem_space = full_string_2[j]
            if elem_space[1].isnumeric():
                continue
            first_space = j
            if elem_file[0] > elem_space[0]:
                continue
            elif elem_file[0] == elem_space[0]:
                full_string_2[j] = elem_file
                full_string_2[i] = elem_space
                break
            else:
                diff = elem_space[0] - elem_file[0]
                full_string_2 = full_string_2[:j] + [elem_file] + [(diff, '.')] + full_string_2[j+1:]
                full_string_2[i] = (elem_file[0], '.')
                break

    vis_string = visualize(full_string_2)
    ans_2 = 0
    for i,c in enumerate(vis_string):
        if not c.isnumeric():
            continue
        ans_2 += i*int(c)
    print(ans_2)

