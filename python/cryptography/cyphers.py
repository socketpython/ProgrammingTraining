import string


abc = list(string.ascii_lowercase)


# הצפנת צופן מונואלפביתי
def encrypt_mono(key, plain_txt):
    global abc
    
    temp = abc[:]
    for letter in key:
        temp.remove(letter)
    
    new_abc = list(key) + temp
    cypher_dict = dict(zip(abc, new_abc))

    cypher_txt = ""
    for letter in plain_txt:
        try:
            cypher_txt += cypher_dict[letter]
        except:
            cypher_txt += letter

    return cypher_txt


# פענוח צופן מונואלפביתי
def decrypt_mono(key, cypher_txt):
    global abc
    
    temp = abc[:]
    for letter in key:
        temp.remove(letter)
    
    new_abc = list(key) + temp
    cypher_dict = dict(zip(new_abc, abc))

    plain_txt = ""
    for letter in cypher_txt:
        try:
            plain_txt += cypher_dict[letter]
        except:
            plain_txt += letter

    return plain_txt


# הצפנת צופן קיסר
def encrypt_ceaser(shift, plain_txt):
    global abc
    shift = len(abc) - shift
    new_abc = abc[shift:] + abc[:shift]
    cypher_dict = dict(zip(new_abc, abc))

    cypher_txt = ""
    for letter in plain_txt:
        try:
            cypher_txt += cypher_dict[letter]
        except:
            cypher_txt += letter

    return cypher_txt


# פענוח צופן קיסר
def decrypt_ceaser(shift, cypher_txt):
    global abc
    shift = len(abc) - shift
    new_abc = abc[shift:] + abc[:shift]
    cypher_dict = dict(zip(abc, new_abc))

    plain_txt = ""
    for letter in cypher_txt:
        try:
            plain_txt += cypher_dict[letter]
        except:
            plain_txt += letter

    return plain_txt


# הצפנת צופן גדר
def encrypt_fence(num_of_lines, plain_txt):
    global abc

    temp = []
    for i in range(num_of_lines):
        temp.append([])
    index = 0
    for letter in plain_txt:
        temp[index].append(letter)
        if index == num_of_lines - 1:
            index = 0
        elif index < num_of_lines - 1:
            index += 1
    for line in temp:
        print(" ".join(line))


key = "phoenix"
shift = 7
plain_txt = "python is the best language"

print("Mono cypher:")
cypher_txt = encrypt_mono(key, plain_txt)
clear_txt = decrypt_mono(key, cypher_txt)
print(f"\tCypher text: {cypher_txt}\n\tClear text: {clear_txt}\n")

print("Ceaser cypher:")
cypher_txt = encrypt_ceaser(shift, plain_txt)
clear_txt = decrypt_ceaser(shift, cypher_txt)
print(f"\tCypher text: {cypher_txt}\n\tClear text: {clear_txt}\n")

encrypt_fence(3, plain_txt)
