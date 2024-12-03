# Part 1
from pathlib import Path

file_path = Path('December 1st/december-1st-input.txt')

with file_path.open('r') as file:
    pairs = [tuple(map(int, line.split())) for line in file]

left_list, right_list = zip(*pairs)
left_list = sorted(left_list)
right_list = sorted(right_list)

total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))
print(f"Total distance: {total_distance}")

# Part 2
from pathlib import Path
from collections import Counter

file_path = Path('December 1st/december-1st-input.txt')

with file_path.open('r') as file:
    left_list, right_list = zip(*(map(int, line.split()) for line in file))

right_counts = Counter(right_list)

similarity_score = sum(right_counts[num] * num for num in left_list)

print(f"Total Similarity Score: {similarity_score}")

