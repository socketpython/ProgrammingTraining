# data_proc.py
#
# Programmer   : Elad L
# Student no.  : 217
# Date         : 03/10/2020
#
# ---------------------------------------------------

# Imports
from functools import reduce


def add_if_lower(word, letter):
    if letter.islower():
        return word + letter
    return word


def excer_reduce():
    file_path = r"C:\Users\Elad_Levi\Desktop\secret.txt"
    with open(file_path, "r") as file:
        data = file.read()
    print(reduce(add_if_lower, data))


def excer_filter():
    file_path = r"C:\Users\Elad_Levi\Desktop\auth.log"
    with open(file_path, "r") as file:
        data = file.read().splitlines()

    print("\n".join(list(filter(lambda line: "Success" in line, data))))


first_excer = lambda a, b, c: a + b + c
print(first_excer(1, 2, 3))

second_excer = lambda a="python", b="linux", c="AD": f"{a} {b} {c}"
print(second_excer("a"))

third_excer = lambda num1, num2: max(num1, num2)
print(third_excer(34, 56))

fourth_excer = lambda string: f"{string[0]}{string}{string[-1]}"
print(fourth_excer("Cyber"))

fifth_excer = map(lambda num: num * 2, range(1, 101))
print(list(fifth_excer))

seventh_excer = filter(lambda num: num > 0, range(-10, 11))
print(list(seventh_excer))

eighth_excer = reduce(lambda last, current: last + current, range(50))
print(eighth_excer)

ninth_excer = reduce(lambda last, current: last * current, range(1, 5))
print(ninth_excer)

tenth_excer = reduce(lambda last, current: last + current, range(2, 101, 2)) / len(range(2, 101, 2))
print(tenth_excer)

eleventh_excer = filter(lambda num: num % 2 == 0, range(1, 101))
print(list(eleventh_excer))

twelevth_excer = reduce(lambda crnt_max, num: num if num > crnt_max else crnt_max, range(100))
print(twelevth_excer)

usernames_list = ["u1237463", "u1375431", "u12475112", "u832593"]
thirteenth_excer = map(lambda username: f"BSMCH\{username}", usernames_list)
print(list(thirteenth_excer))

fourteenth_excer = filter(lambda user: user[0] == "u" and user[1:].isnumeric() and len(user) == 8, usernames_list)
print(list(fourteenth_excer))

fifteenth_excer = reduce(lambda crnt_sum, num: int(crnt_sum) + int(num), list(str(1234)))
print(fifteenth_excer)

def sixteenth_excer():
    num = int(input("Enter num: "))
    fibon = [1, 1]
    last_num = 1
    crnt_num = 1
    next_num = 2
    while num > 0:
        if next_num == last_num + crnt_num:
            fibon.append(next_num)
            last_num, crnt_num = crnt_num, next_num
            num -= 1
        next_num += 1
    return fibon[:num - 2]
print(sixteenth_excer())
