from datetime import datetime

today_day_number = datetime.now().day
# create part1 - day{today_day_number}.py
with open(f"day{today_day_number} - part1.py", "w") as file:
    file.write(f"""from helper import read_input
today_input = read_input()
print(today_input)
    """)
# create part2 - day{today_day_number}.py
with open(f"day{today_day_number} - part2.py", "w") as file:
    file.write(f"""from helper import read_input
today_input = read_input()
print(today_input)
    """)