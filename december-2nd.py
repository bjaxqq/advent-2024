# Part 1
file_path = 'december-2nd-input'

with open(file_path, 'r') as file:
    data = file.readlines()

reports = [list(map(int, line.split())) for line in data]

def is_safe(report):
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]
    
    if all(1 <= diff <= 3 for diff in differences):
        return True
    if all(-3 <= diff <= -1 for diff in differences):
        return True
    return False

safe_count = sum(is_safe(report) for report in reports)

print(f"Number of safe reports: {safe_count}")

# Part 2
file_path = 'december-2nd-input'

with open(file_path, 'r') as file:
    data = file.readlines()

reports = [list(map(int, line.split())) for line in data]

def is_sequence_safe(report):
    """Check if a sequence of levels is safe."""
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]
    return (
        all(1 <= diff <= 3 for diff in differences) or
        all(-3 <= diff <= -1 for diff in differences)
    )

def is_safe_with_dampener(report):
    if is_sequence_safe(report):
        return True

    for i in range(len(report)):
        reduced_report = report[:i] + report[i+1:]
        if is_sequence_safe(reduced_report):
            return True

    return False

safe_count = sum(is_safe_with_dampener(report) for report in reports)

print(f"Number of safe reports with problem dampener: {safe_count}")
