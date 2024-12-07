from pathlib import Path

def parse_input(file_path):
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()

    grid = []
    start_pos = None
    direction = None

    directions = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}

    for y, line in enumerate(lines):
        row = []
        for x, char in enumerate(line):
            if char in directions:
                start_pos = (x, y)
                direction = directions[char]
                row.append('.')
            else:
                row.append(char)
        grid.append(row)

    return grid, start_pos, direction

def move_guard(grid, position, direction):
    x, y = position
    dx, dy = direction
    new_position = (x + dx, y + dy)

    if not (0 <= new_position[1] < len(grid) and 0 <= new_position[0] < len(grid[0])):
        return position, direction, False

    if grid[new_position[1]][new_position[0]] == '#':
        direction = (dy, -dx)
        return position, direction, True

    return new_position, direction, True

def simulate_path(grid, start_pos, direction):
    visited = set()
    position = start_pos

    while True:
        visited.add(position)
        position, direction, on_map = move_guard(grid, position, direction)
        if not on_map:
            break

    return visited

def find_loop_positions(grid, start_pos, direction):
    loop_positions = set()
    original_grid = [row[:] for row in grid]

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (x, y) == start_pos or grid[y][x] != '.':
                continue

            grid[y][x] = '#'
            visited = simulate_path(grid, start_pos, direction)

            if len(visited) == len(simulate_path(grid, start_pos, direction)):
                loop_positions.add((x, y))

            grid = [row[:] for row in original_grid]

    return loop_positions

def main():
    file_path = 'December 6th/december-6th-input.txt'
    grid, start_pos, direction = parse_input(file_path)

    visited_positions = simulate_path(grid, start_pos, direction)
    print(f"Total visited positions: {len(visited_positions)}")

    loop_positions = find_loop_positions(grid, start_pos, direction)
    print(f"Total loop-causing positions: {len(loop_positions)}")

if __name__ == "__main__":
    main()
