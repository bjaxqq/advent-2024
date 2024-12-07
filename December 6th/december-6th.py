# Part 1
from pathlib import Path

file_path = Path('december-6th-input.txt')

lab_map = [list(line.strip()) for line in file_path.read_text().splitlines()]

DIRECTIONS = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
TURN_RIGHT = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

for r, row in enumerate(lab_map):
    for c, cell in enumerate(row):
        if cell in DIRECTIONS:
            guard_start = (r, c)
            guard_dir = cell
            break

def simulate_patrol(lab_map, guard_start, guard_dir):
    rows, cols = len(lab_map), len(lab_map[0])
    guard_pos = guard_start
    visited_positions = set()
    visited_positions.add(guard_pos)
    
    while True:
        dr, dc = DIRECTIONS[guard_dir]
        next_pos = (guard_pos[0] + dr, guard_pos[1] + dc)
        
        if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
            break
        
        if lab_map[next_pos[0]][next_pos[1]] == '#':
            guard_dir = TURN_RIGHT[guard_dir]
        else:
            guard_pos = next_pos
            visited_positions.add(guard_pos)
    
    return len(visited_positions)

result_part1 = simulate_patrol(lab_map, guard_start, guard_dir)
print(f"Distinct positions visited by the guard: {result_part1}")
