import os

in_file = open("../data/ex1.txt")
lines = [l.replace('\\n', '') for l in in_file.readlines()]
first, second = [], []
total_dist = 0
similarity_score = 0

for line in lines:
    first.append(int(line.split()[0]))
    second.append(int(line.split()[1]))

first.sort()
second.sort()

for i in range(len(first)):
    total_dist += abs(first[i]-second[i])
    similarity_score += second.count(first[i])*first[i]


print(total_dist)
print(similarity_score)