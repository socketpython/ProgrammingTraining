from cryptography.fernet import Fernet

key = Fernet.generate_key()
file_name = input("Enter file name ") + ".txt"
file = open(file_name, 'wb')
file.write(key)  # The key is type bytes still
file.close()

text = "This is the new text i wrote".encode()

f = Fernet(key)

encrypted_text = f.encrypt(text)
file = open('message.txt', 'wb')
file.write(encrypted_text)  # The key is type bytes still
file.close()
