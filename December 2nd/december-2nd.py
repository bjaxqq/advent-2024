# Part 1
from pathlib import Path

file_path = Path('December 2nd/december-2nd-input')

with file_path.open('r') as file:
    reports = [list(map(int, line.split())) for line in file]

def is_safe(report):
    return all(1 <= report[i+1] - report[i] <= 3 or -3 <= report[i+1] - report[i] <= -1 for i in range(len(report) - 1))

safe_count = sum(is_safe(report) for report in reports)

print(f"Number of safe reports: {safe_count}")

# Part 2
from pathlib import Path

file_path = Path('December 2nd/december-2nd-input')

with file_path.open('r') as file:
    reports = [list(map(int, line.split())) for line in file]

def is_sequence_safe(report):
    return all(1 <= report[i+1] - report[i] <= 3 or -3 <= report[i+1] - report[i] <= -1 for i in range(len(report) - 1))

def is_safe_with_dampener(report):
    if is_sequence_safe(report):
        return True

    return any(is_sequence_safe(report[:i] + report[i+1:]) for i in range(len(report)))

safe_count = sum(is_safe_with_dampener(report) for report in reports)

print(f"Number of safe reports with problem dampener: {safe_count}")
