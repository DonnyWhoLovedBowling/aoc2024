def count_xmas(text: str) -> int:
    return text.count('XMAS') + text.count('SAMX')

def is_x_mas(ix: int, iy: int) -> bool:
    global lines
    is_x_max = False
    if lines[iy][ix] != 'A':
        return False
    if ((lines[iy-1][ix-1] == 'S' and lines[iy+1][ix+1] == 'M') or
        (lines[iy-1][ix-1] == 'M' and lines[iy+1][ix+1] == 'S')):
            if ((lines[iy-1][ix+1] == 'S' and lines[iy+1][ix-1] == 'M') or
                (lines[iy-1][ix+1] == 'M' and lines[iy+1][ix-1] == 'S')):
                    is_x_max = True
    return is_x_max


in_file = open("../data/ex4.txt")
lines = [l.replace('\\n', '').strip() for l in in_file.readlines()]
print(len(lines[0]))

total_1, total_2 = 0, 0
y_max = len(lines[0])
for i in range(y_max):
    total_1 += count_xmas(lines[i])
    total_1 += count_xmas(''.join([l[i] for l in lines]))
    total_1 += count_xmas(''.join([lines[j][j+i] for j in range(0, y_max-i)]))
    total_1 += count_xmas(''.join([lines[j][i-j] for j in range(i, -1, -1)]))

    if 0 < i < len(lines[0])-1:
        total_1 += count_xmas(''.join([lines[y_max-j-1][i+j] for j in range(0, y_max-i)]))
        total_1 += count_xmas(''.join([lines[y_max-j-1][i-j] for j in range(0, i+1)]))

for i in range(1, y_max-1):
    for j in range(1, y_max-1):
        total_2 += is_x_mas(i, j)

print(total_1)
print(total_2)
