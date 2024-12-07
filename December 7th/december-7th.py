# Part 1
from pathlib import Path
from itertools import product

file_path = Path('December 7th/december-7th-input.txt')
calibration_data = file_path.read_text().splitlines()

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for num, op in zip(numbers[1:], operators):
        if op == '+':
            result += num
        elif op == '*':
            result *= num
    return result

def can_solve_equation(target, numbers):
    num_slots = len(numbers) - 1
    for operator_combination in product(['+', '*'], repeat=num_slots):
        if evaluate_expression(numbers, operator_combination) == target:
            return True
    return False

total_calibration_result = 0

for line in calibration_data:
    target, *numbers = map(int, line.replace(':', '').split())
    if can_solve_equation(target, numbers):
        total_calibration_result += target

print(f"Total Calibration Result: {total_calibration_result}")

# Part 2
from pathlib import Path
from itertools import product

file_path = Path('December 7th/december-7th-input.txt')
calibration_data = file_path.read_text().splitlines()

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for num, op in zip(numbers[1:], operators):
        if op == '+':
            result += num
        elif op == '*':
            result *= num
        elif op == '||':
            result = int(f"{result}{num}")  # Concatenate as a number
    return result

def can_solve_equation(target, numbers):
    num_slots = len(numbers) - 1
    for operator_combination in product(['+', '*', '||'], repeat=num_slots):
        if evaluate_expression(numbers, operator_combination) == target:
            return True
    return False

total_calibration_result = 0

for line in calibration_data:
    target, *numbers = map(int, line.replace(':', '').split())
    if can_solve_equation(target, numbers):
        total_calibration_result += target

print(f"Total Calibration Result: {total_calibration_result}")