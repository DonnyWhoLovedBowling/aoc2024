import re

in_file = open("../data/ex3.txt")
lines = [l.replace('\\n', '') for l in in_file.readlines()]
print(len(lines))

pattern = re.compile(r'mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\)')
total_1 = 0
total_2 = 0
enabled = True
for line in lines:
    for x in re.findall(pattern, line):
        print(x[0:4])
        if x[0:4] == 'mul(':
            print('mul')
            nums = x[4:-1].split(',')
            total_1 += int(nums[0]) * int(nums[1])
            if enabled:
                total_2 += int(nums[0]) * int(nums[1])
        elif x == 'do()':
            enabled = True
            print('enabled')
        elif x == 'don\'t()':
            enabled = False
            print('disabled')

        # print(nums)

print(total_1)
print(total_2)

