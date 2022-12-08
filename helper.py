import inspect


def read_input():
    day_number = inspect.stack()[1].filename.split(' - ')[0][-1]
    return open(f"input{day_number}.txt", "r").read().split("\n")[:-1]