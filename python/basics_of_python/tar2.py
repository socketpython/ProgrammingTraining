def first_excersize(first_path, second_path):
    with open(first_path, "r") as first:
        first_data = first.read()
    with open(second_path, "r") as second:
        second_data = second.read()
    return first_data == second_data


def second_excersize(first_name, second_name, third_name):
    with open(first_name, "r") as first:
        a = first.readline()
        b = first.readlines()[-1]
    with open(second_name, "r") as second:
        c = second.readline()
        d = second.readlines()[-1]
    with open(third_name, "w") as third:
        third.write(f"{a}{b}\n{c}{d}")
