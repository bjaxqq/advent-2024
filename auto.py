import os
import requests
import datetime

session_token = '53616c7465645f5fe48e0c08228e0c80365875bfd7ec673976eb02c722e91b0a67580b93bd62899245a566cb86df3203308657ad1a3ef39af44ff4a96d70846f'

base_folder = os.path.expanduser('~/Developer/advent-2024')

today = datetime.date.today()
month_name = today.strftime("%B")
day = today.day

suffix = "th"
if 10 <= day % 100 <= 20:
    suffix = "th"
elif day % 10 == 1:
    suffix = "st"
elif day % 10 == 2:
    suffix = "nd"
elif day % 10 == 3:
    suffix = "rd"
folder_name = f"{month_name} {day}{suffix}"

folder_path = os.path.join(base_folder, folder_name)

os.makedirs(folder_path, exist_ok=True)

url = f'https://adventofcode.com/{today.year}/day/{day}/input'

headers = {
    'Cookie': f'session={session_token}'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    input_file_path = os.path.join(folder_path, f"december-{day}{suffix}-input.txt")
    with open(input_file_path, 'w') as f:
        f.write(response.text)
    print(f"Input data for day {day} saved to {input_file_path}")
else:
    print(f"Failed to retrieve input for day {day}. Status code: {response.status_code}")

python_file_path = os.path.join(folder_path, f"december-{day}{suffix}.py")
with open(python_file_path, 'w') as f:
    f.write("# Part 1\n\n\n# Part 2\n")
print(f"Blank Python file created: {python_file_path}")
