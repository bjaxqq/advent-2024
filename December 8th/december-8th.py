from pathlib import Path

# Part 1
file_path = Path('December 8th/december-8th-input.txt')
puzzle = file_path.read_text().splitlines()

antinodes = []

for r_pos, row in enumerate(puzzle):
    for c_pos, char in enumerate(row):
        if char == ".":
            continue
        for i in range(len(puzzle)):
            loop_r = puzzle[i]
            for j in range(len(loop_r)):
                loop_c = loop_r[j]
                if i == r_pos and j == c_pos:
                    continue

                if char == loop_c:
                    dist_x = (j - c_pos) * 2
                    dist_y = (i - r_pos) * 2
                    coord_x = c_pos + dist_x
                    coord_y = r_pos + dist_y
                    if 0 <= coord_x < len(row) and 0 <= coord_y < len(puzzle):
                        coord = (coord_x, coord_y)
                        if coord not in antinodes:
                            antinodes.append(coord)
                    else:
                        break

print(f"Part 1: {len(antinodes)}")

# Part 2
my_map = [[x for x in each] for each in puzzle]
antinodes = []

for r_pos, row in enumerate(puzzle):
    for c_pos, char in enumerate(row):
        if char == ".":
            continue
        for i in range(len(puzzle)):
            loop_r = puzzle[i]
            for j in range(len(loop_r)):
                loop_c = loop_r[j]
                if i == r_pos and j == c_pos:
                    continue

                if char == loop_c:
                    if (c_pos, r_pos) not in antinodes:
                        antinodes.append((c_pos, r_pos))
                    if (j, i) not in antinodes:
                        antinodes.append((j, i))

                    coord_x = c_pos
                    coord_y = r_pos
                    dist_x = (j - c_pos)
                    dist_y = (i - r_pos)
                    while True:
                        coord_x += dist_x
                        coord_y += dist_y
                        if 0 <= coord_x < len(row) and 0 <= coord_y < len(puzzle):
                            coord = (coord_x, coord_y)
                            if coord not in antinodes:
                                antinodes.append(coord)
                                if puzzle[coord_y][coord_x] == ".":
                                    my_map[coord_y][coord_x] = "#"
                        else:
                            break

print(f"Part 2: {len(antinodes)}")