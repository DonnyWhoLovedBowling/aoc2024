def count_xmas(text: str) -> int:
    return text.count('XMAS') + text.count('SAMX')

in_file = open("../data/ex4.txt")
lines = [l.replace('\\n', '').strip() for l in in_file.readlines()]

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
        if lines[j][i] != 'A':
            continue
        if ((lines[j - 1][i - 1] == 'S' and lines[j + 1][i + 1] == 'M') or
                (lines[j - 1][i - 1] == 'M' and lines[j + 1][i + 1] == 'S')):
            if ((lines[j - 1][i + 1] == 'S' and lines[j + 1][i - 1] == 'M') or
                    (lines[j - 1][i + 1] == 'M' and lines[j + 1][i - 1] == 'S')):
                total_2 += 1

print(total_1)
print(total_2)
