from cryptography.fernet import Fernet

encrypted_text = open("message.txt", "r").read()

key = open('key.txt', 'r').read()
f = Fernet(key)

decrypted_text = f.decrypt(encrypted_text.encode()).decode()
print(decrypted_text)

