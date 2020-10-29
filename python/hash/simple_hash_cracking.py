import hashlib


def main():
    is_success = False
    pass_hash = "c62d929e7b7e7b6165923a5dfc60cb56" #q1w2e3r4
    word_list = "passwords_dict.txt" # the path to the dictionary

    try:
        with open(word_list, "r") as pass_file:
            passwords = pass_file.read().splitlines()
    except:
        print("No file was found")
        quit()

    for password in passwords:
        encoded_pass = password.encode()
        digest = hashlib.md5(encoded_pass.strip()).hexdigest()

        #print(digest, "\n", pass_hash)
        if digest == pass_hash:
            print(f"password found: {password}")
            is_success = True
            break

    if not is_success:
        print("The password wasn't in the list")


if __name__ == "__main__":
    main()
