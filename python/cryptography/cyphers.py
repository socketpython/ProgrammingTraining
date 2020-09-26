import string


abc = list(string.ascii_lowercase)


# הצפנת צופן מונואלפביתי
def encrypt_mono(key, plain_txt):
    global abc
    
    temp = abc[:]
    for letter in key:
        temp.remove(letter)
    
    new_abc = list(key) + temp
    cipher_dict = dict(zip(abc, new_abc))

    cipher_txt = ""
    for letter in plain_txt:
        try:
            cipher_txt += cipher_dict[letter]
        except:
            cipher_txt += letter

    return cipher_txt


# פענוח צופן מונואלפביתי
def decrypt_mono(key, cipher_txt):
    global abc
    
    temp = abc[:]
    for letter in key:
        temp.remove(letter)
    
    new_abc = list(key) + temp
    cipher_dict = dict(zip(new_abc, abc))

    plain_txt = ""
    for letter in cipher_txt:
        try:
            plain_txt += cipher_dict[letter]
        except:
            plain_txt += letter

    return plain_txt


# הצפנת צופן קיסר
def encrypt_ceaser(shift, plain_txt):
    global abc
    shift = len(abc) - shift
    new_abc = abc[shift:] + abc[:shift]
    cipher_dict = dict(zip(new_abc, abc))

    cipher_txt = ""
    for letter in plain_txt:
        try:
            cipher_txt += cipher_dict[letter]
        except:
            cipher_txt += letter

    return cipher_txt


# פענוח צופן קיסר
def decrypt_ceaser(shift, cipher_txt):
    global abc
    shift = len(abc) - shift
    new_abc = abc[shift:] + abc[:shift]
    cipher_dict = dict(zip(abc, new_abc))

    plain_txt = ""
    for letter in cipher_txt:
        try:
            plain_txt += cipher_dict[letter]
        except:
            plain_txt += letter

    return plain_txt


# הצפנת צופן גדר
def encrypt_fence(num_of_lines, plain_txt):
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

    cipher_txt = ""
    for line in temp:
        cipher_txt += "".join(line)
    return cipher_txt
    

# פענוח צופן גדר
def decrypt_fence(num_of_lines, cipher_txt):
    clear_txt = ""
    length = len(cipher_txt)

    left = 0
    if length % num_of_lines == 0:
        num = length / num_of_lines
    else:
        num = (length // num_of_lines) + 1
        left = length % num_of_lines

    a = []
    for i in range(1, num_of_lines + 1):
        if i <= left:
            a.append(list(cipher_txt[:num]))
            cipher_txt = cipher_txt[num:]
        else:
            a.append(list(cipher_txt[:num - 1]))
            cipher_txt = cipher_txt[num - 1:]
    
    clear_txt = ""
    for i in range(length):
        for j in range(num_of_lines):
            try:
                clear_txt += a[j][i]
            except:
                break
    return clear_txt


def mono():
    print("Mono cipher:\n")
    choice = input("Encrypt or Decrypt? (e/d) ").lower()
    key = input("Enter the key: ")
    txt = input("Enter the text: ")
    if choice == "e":
        print(encrypt_mono(key, txt))
    elif choice == "d":
        print(decrypt_mono(key, txt))


def ceaser():
    print("Ceaser cipher:\n")
    choice = input("Encrypt or Decrypt? (e/d) ").lower()
    shift = int(input("Enter the shift number: "))
    txt = input("Enter the text: ")
    if choice == "e":
        print(encrypt_ceaser(shift, txt))
    elif choice == "d":
        print(decrypt_ceaser(shift, txt))


def fence():
    print("Fence cipher:\n")
    choice = input("Encrypt or Decrypt? (e/d) ").lower()
    num_of_lines = int(input("Enter the number of lines: "))
    txt = input("Enter the text: ")
    if choice == "e":
        print(encrypt_ceaser(num_of_lines, txt))
    elif choice == "d":
        print(decrypt_ceaser(num_of_lines, txt))


def main():
    options = ["mono", "ceaser", "fence", "exit"]

    choice = 0
    while choice != len(options):
        index = 1
        for option in options:
            print(f"{index}. {option}")
            index += 1
        choice = int(input("Enter the number according to the cipher you want: "))
        if choice == 1:
            mono()
        elif choice == 2:
            ceaser()
        elif choice == 3:
            fence()


if __name__ == "__main__":
    main()
