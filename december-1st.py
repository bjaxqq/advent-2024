# Part 1
# Steps:
# 1. Separate the data into two different lists
# 2. Sort both of the lists
# 3. Match both numbers from smallest to largest and compute difference
# 4. Sum differences to get total difference

# Code:
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
# Steps:
# 1. Separate the data into two different lists
# 2. Count the occurrences in the left list for each number
# 3. Compute the similarity score by iterating through the right list, multiplying the number by its count in the right list, and adding to a running total
# 4. Output the similarity score

# Code:
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
