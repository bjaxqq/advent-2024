def parse_data(data):
    blocks, gaps = [], []
    for i, d in enumerate(map(int, data)):
        (blocks if i % 2 == 0 else gaps).append(d)
    return blocks, gaps

def calculate_checksum(blocks):
    checksum = 0
    position = 0
    for bid, size in blocks:
        checksum += bid * size * (2 * position + size - 1) // 2
        position += size
    return checksum

def part_1(data):
    blocks, gaps = parse_data(data)
    result_blocks = []
    gap_index = 0
    for bid, bsize in enumerate(blocks):
        result_blocks.append((bid, bsize))
        while gap_index < len(gaps) and bsize > 0:
            gap_size = gaps[gap_index]
            if gap_size <= bsize:
                result_blocks.append((bid, gap_size))
                bsize -= gap_size
                gap_index += 1
            else:
                result_blocks.append((bid, bsize))
                gaps[gap_index] -= bsize
                bsize = 0
    return calculate_checksum(result_blocks)

def part_2(data):
    blocks, gaps = parse_data(data)
    block_positions = []
    gap_map = {i: [] for i in range(10)}
    position = 0
    for bid, bsize in enumerate(blocks):
        block_positions.append((position, bid, bsize))
        position += bsize
    position = 0
    for gap_size in gaps:
        gap_map[gap_size].append(position)
        position += gap_size
    checksum = 0
    for bpos, bid, bsize in reversed(block_positions):
        best_pos = bpos
        available_gaps = [(gpos, gsize) for gsize, gpositions in gap_map.items() for gpos in gpositions if gsize >= bsize]
        if available_gaps:
            best_gap = min(available_gaps, key=lambda x: (x[0], x[1]))
            if best_gap[0] < bpos:
                best_pos = best_gap[0]
                gap_map[best_gap[1]].remove(best_gap[0])
                new_gap_size = best_gap[1] - bsize
                if new_gap_size > 0:
                    gap_map[new_gap_size].append(best_gap[0] + bsize)
        checksum += bid * bsize * (2 * best_pos + bsize - 1) // 2
    return checksum

data = open("December 9th/december-9th-input.txt").read()
print("Part 1:", part_1(data))
print("Part 2:", part_2(data))
