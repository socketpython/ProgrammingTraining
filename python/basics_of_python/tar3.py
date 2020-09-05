def multi_board():
    a = []
    for i in range(9):
        a.append(list(range(9)))
    for i in range(1, 10):
        for j in range (1, 10):
            a[i-1][j-1] = i * j
    return a


def pitiya():
    rating = "EMPTY"
    eight_plus = 0
    five_to_seven = 0
    less_than_four = 0
    while True:
        rating = input("Enter the rating (1-10): ")
        if rating == "exit":
            break
        rating = int(rating)
        if 8 <= rating <= 10:
            eight_plus += 1
        elif 5 <= rating <= 7:
            five_to_seven += 1
        elif 1 <= rating <= 4:
            less_than_four += 1
    print(f"8-10: {eight_plus}, 5-7: {five_to_seven}, 1-4: {less_than_four}")


def for_loop():
    num = int(input("Enter a number: "))
    res = ""  #the final string
    for i in range(2, num + 2):  #going through the numbers
        a = ""
        for j in range(1, i):  #going through 1 to i (which is the current middle number)
            a +=  str(j)
        res += f"{a[:-1]}{a[::-1]} * "  #adds the string to the reversed version
    res = res[:-3]  #remove the last " * "
    return f"{res[:-num*2-1]} * {res[::-1]}"
