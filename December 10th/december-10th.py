from collections import deque

def parse_input(file_path):
    with open(file_path, 'r') as file:
        grid = [list(map(int, line.strip())) for line in file]
    return grid

def find_trailheads(grid):
    trailheads = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                trailheads.append((i, j))
    return trailheads

def bfs_score(grid, start):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start[0], start[1], 0)])
    visited = set()
    reachable_nines = set()

    while queue:
        row, col, current_height = queue.popleft()
        if (row, col) in visited:
            continue
        visited.add((row, col))

        if grid[row][col] == 9:
            reachable_nines.add((row, col))

        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == current_height + 1:
                    queue.append((nr, nc, current_height + 1))

    return len(reachable_nines)

def count_distinct_trails_rating(grid, start):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dp = [[0] * cols for _ in range(rows)]
    dp[start[0]][start[1]] = 1

    for height in range(10):
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == height:
                    for dr, dc in directions:
                        ni, nj = i + dr, j + dc
                        if 0 <= ni < rows and 0 <= nj < cols:
                            if grid[ni][nj] == height + 1:
                                dp[ni][nj] += dp[i][j]

    total_trails = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 9:
                total_trails += dp[i][j]

    return total_trails

def calculate_scores_and_ratings(grid):
    trailheads = find_trailheads(grid)
    total_score = 0
    total_rating = 0

    for trailhead in trailheads:
        score = bfs_score(grid, trailhead)
        total_score += score

        rating = count_distinct_trails_rating(grid, trailhead)
        total_rating += rating

    return total_score, total_rating

file_path = 'December 10th/december-10th-input.txt'
grid = parse_input(file_path)
total_score, total_rating = calculate_scores_and_ratings(grid)

print(f"The sum of the scores of all trailheads is: {total_score}")
print(f"The sum of the ratings of all trailheads is: {total_rating}")