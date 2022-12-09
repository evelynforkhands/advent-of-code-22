import uuid

from helper import read_input

today_input = read_input()
file_system = {}
current_directory = file_system
path = []


def current_directory_path(path, file_system):
    current_directory = file_system

    for directory in path:
        current_directory = current_directory[directory]
    return current_directory


for line in today_input:
    if "$" in line:
        vals = line.split(" ")
        if len(vals) == 3:
            etc, command, dir = vals
        elif len(vals) == 2:
            etc, command = vals
        if command == "ls":
            current_command = "ls"
        elif command == "cd":
            if dir == "..":
                path.pop()
            else:
                path.append(dir)
            current_directory = current_directory_path(path, file_system)
    else:
        size, file = line.split(" ")
        if size == "dir":
            current_directory[file] = {}
        else:
            current_directory[file] = int(size)


# recursively calculate the size of every directory
def calculate_size(file_system):
    size = 0
    for key, value in file_system.items():
        if type(value) == int:
            size += value
        else:
            size += calculate_size(value)
    return size

sizes = {}
# recursively find all dictionaaries in file_system
def find_all_dictionaries(file_system):
    for key, value in file_system.items():
        if type(value) == dict:
            # if the key is already in sizes, add a random uuid to it
            if key in sizes:
                sizes[str(uuid.uuid4())] = calculate_size(value)
                find_all_dictionaries(value)
            else:
                sizes[key] = calculate_size(value)
                find_all_dictionaries(value)


find_all_dictionaries(file_system)
# total size of the file system is the size of the root directory
total_size = calculate_size(file_system)
# sort the sizes dictionary by value
print(30000000 - 70000000 + total_size)
print(sorted([s for s in sizes.values() if s > 2805968]))
# find the
