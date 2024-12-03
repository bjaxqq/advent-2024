# Part 1
file_path = 'december-1st-input.txt'

left_list, right_list = [], []
with open(file_path, 'r') as file:
    for line in file:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

left_list.sort()
right_list.sort()

total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))
print(f"Total distance: {total_distance}")

# Part 2
from collections import Counter

file_path = 'december-1st-input.txt'

left_list = []
right_list = []
with open(file_path, 'r') as file:
    for line in file:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

right_counts = Counter(right_list)

similarity_score = sum(num * right_counts[num] for num in left_list)

print(f"Total Similarity Score: {similarity_score}")
