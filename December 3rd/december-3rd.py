# Part 1
from pathlib import Path
import re

file_path = Path('December 3rd/december-3rd-input')

corrupted_memory = file_path.read_text()

pattern = r"mul\((\d+),(\d+)\)"
matches = re.findall(pattern, corrupted_memory)

total_sum = sum(int(x) * int(y) for x, y in matches)

print(f"Total sum: {total_sum}")

# Part 2
from pathlib import Path
import re

file_path = Path('December 3rd/december-3rd-input')

corrupted_memory = file_path.read_text()

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

print(f"Total sum of enabled multiplications: {total_sum}")