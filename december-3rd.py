# Part 1
import re

file_path = 'december-3rd-input'

with open(file_path, 'r') as file:
    corrupted_memory = file.read()

pattern = r"mul\((\d+),(\d+)\)"
matches = re.findall(pattern, corrupted_memory)
total_sum = sum(int(x) * int(y) for x, y in matches)

print(total_sum)

# Part 2
import re

file_path = 'december-3rd-input'

with open(file_path, 'r') as file:
    corrupted_memory = file.read()

pattern = r"(do\(\))|(don't\(\))|mul\((\d+),(\d+)\)"
matches = re.findall(pattern, corrupted_memory)

enabled = True
total_sum = 0

for match in matches:
    if match[0] == "do()":
        enabled = True
    elif match[1] == "don't()":
        enabled = False
    elif enabled and match[2] and match[3]:
        total_sum += int(match[2]) * int(match[3])

print(total_sum)
