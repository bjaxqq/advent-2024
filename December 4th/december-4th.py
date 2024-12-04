# Part 1
from pathlib import Path

file_path = Path('December 4th/december-4th-input.txt')
word_search = file_path.read_text().splitlines()

target_word = "XMAS"
target_length = len(target_word)

directions = [
    (0, 1),   # Right
    (0, -1),  # Left
    (1, 0),   # Down
    (-1, 0),  # Up
    (1, 1),   # Down-Right
    (-1, -1), # Up-Left
    (1, -1),  # Down-Left
    (-1, 1)   # Up-Right
]

def in_bounds(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols

def count_occurrences(grid, word, directions):
    rows, cols = len(grid), len(grid[0])
    count = 0

    for row in range(rows):
        for col in range(cols):
            for dr, dc in directions:
                match = True
                for i in range(len(word)):
                    nr, nc = row + i * dr, col + i * dc
                    if not in_bounds(nr, nc, rows, cols) or grid[nr][nc] != word[i]:
                        match = False
                        break
                if match:
                    count += 1
    return count

total_count = count_occurrences(word_search, target_word, directions)
print(f"Total occurrences of '{target_word}': {total_count}")

# Part 2
from pathlib import Path

file_path = Path('December 4th/december-4th-input.txt')
word_search = file_path.read_text().splitlines()

def count_x_mas(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if (grid[i][j] == 'A' and
                ((grid[i-1][j-1] == 'M' and grid[i+1][j+1] == 'S') or
                 (grid[i-1][j-1] == 'S' and grid[i+1][j+1] == 'M')) and
                ((grid[i-1][j+1] == 'M' and grid[i+1][j-1] == 'S') or
                 (grid[i-1][j+1] == 'S' and grid[i+1][j-1] == 'M'))):
                count += 1

    return count

result = count_x_mas(word_search)
print(f"Number of X-MAS occurrences: {result}")