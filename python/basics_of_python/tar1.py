"""
תרגיל ראשון:
1. 'l'
2. 'o, Wo'
3. 'Hello'
4. 'o, World!'
5. 'Hlo ol!'
6. 'llo, W'
7. 'r'
8. '!dlroW ,olleH'
"""


def calc(num_a, num_b):
    if type(num_a) == bin:
        num_a = int(num_a, 2)
    elif type(num_a) == oct:
        num_a = int(num_a, 8)
    elif type(num_a) == hex:
        num_a = int(num_a, 16)
    if type(num_b) == bin:
        num_a = int(num_a, 2)
    elif type(num_b) == oct:
        num_a = int(num_a, 8)
    elif type(num_b) == hex:
        num_a = int(num_a, 16)
        
    command = str(input("Enter the command (plus, minus, divide, times):"))
    if command == "plus":
        print(num_a + num_b)
    elif command == "minus":
        print(num_a + num_b)
    elif command == "divide":
        print(num_a + num_b)
    elif command == "times":
        print(num_a + num_b)


calc('0b1101', 24)
