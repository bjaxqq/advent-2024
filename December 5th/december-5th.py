# Part 1
from pathlib import Path
from collections import defaultdict, deque

file_path = Path('December 5th/december-5th-input.txt')
rules_section, updates_section = file_path.read_text().strip().split("\n\n")

rules = [tuple(map(int, line.split('|'))) for line in rules_section.splitlines()]
updates = [list(map(int, line.split(','))) for line in updates_section.splitlines()]

def is_valid_update(ordering_rules, update):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    update_set = set(update)
    
    for x, y in ordering_rules:
        if x in update_set and y in update_set:
            graph[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0

    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_order = []
    
    while queue:
        current = queue.popleft()
        sorted_order.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_order == update

valid_updates = [update for update in updates if is_valid_update(rules, update)]
middle_page_numbers = [update[len(update) // 2] for update in valid_updates]
result_part1 = sum(middle_page_numbers)

print(f"Sum of middle page numbers for valid updates: {result_part1}")

# Part 2
def topological_sort(ordering_rules, update):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    update_set = set(update)
    
    for x, y in ordering_rules:
        if x in update_set and y in update_set:
            graph[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0

    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_order = []
    
    while queue:
        current = queue.popleft()
        sorted_order.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_order

incorrect_updates = [update for update in updates if not is_valid_update(rules, update)]
fixed_updates = [topological_sort(rules, update) for update in incorrect_updates]

fixed_middle_page_numbers = [update[len(update) // 2] for update in fixed_updates]
result_part2 = sum(fixed_middle_page_numbers)

print(f"Sum of middle page numbers for fixed updates: {result_part2}")
