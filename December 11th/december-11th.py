from collections import defaultdict

def transform_stone(stone):
    if stone == 0:
        return [1]
    num_digits = len(str(stone))
    if num_digits % 2 == 0:
        half = num_digits // 2
        left = int(str(stone)[:half])
        right = int(str(stone)[half:])
        return [left, right]
    else:
        return [stone * 2024]

def simulate_blinks_optimized(initial_stones, num_blinks):
    stone_counts = defaultdict(int)
    for stone in initial_stones:
        stone_counts[stone] += 1

    for _ in range(num_blinks):
        new_stone_counts = defaultdict(int)
        for stone, count in stone_counts.items():
            transformed_stones = transform_stone(stone)
            for new_stone in transformed_stones:
                new_stone_counts[new_stone] += count
        stone_counts = new_stone_counts

    total_stones = sum(stone_counts.values())
    return total_stones

initial_stones = [64599, 31, 674832, 2659361, 1, 0, 8867, 321]

num_stones_25 = simulate_blinks_optimized(initial_stones, 25)

num_stones_75 = simulate_blinks_optimized(initial_stones, 75)

print(f"After 25 blinks, you will have {num_stones_25} stones.")
print(f"After 75 blinks, you will have {num_stones_75} stones.")