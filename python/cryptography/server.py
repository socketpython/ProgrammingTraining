import socket
from cryptography.fernet import Fernet


IP = socket.gethostname()
PORT = 7654


def encrypt(text):
    key = Fernet.generate_key()

    file = open('key.txt', 'wb')
    file.write(key)  # The key is type bytes still
    file.close()

    text = text.encode()
    f = Fernet(key)
    return f.encrypt(text), f


def decrypt(text):
    key = open('key.txt', 'r').read()
    f = Fernet(key)
    original_text = f.decrypt(text.encode())

    return original_text


def main():
    done = False

    while not done:
        server_socket = socket.socket()
        server_socket.bind((IP, PORT))
        server_socket.listen()

        client_socket, client_address = server_socket.accept()

        print(f"Connection from {client_address} has been established!")

        client_message = str(client_socket.recv(1024).decode("utf-8"))

        if client_message[:7] == "ENCRYPT":
            encrypted_text, fernet_key = encrypt(client_message[7:])
            client_socket.send(encrypted_text)
        elif client_message[:7] == "DECRYPT":
            decrypted_text = decrypt(client_message[7:])
            client_socket.send(decrypted_text)
        elif client_message == "EXIT":
            client_socket.close()
            print(f"Connection from {client_address} has been closed!")
            break
        print(f"Connection from {client_address} has been closed!")
        client_socket.close()


if __name__ == '__main__':
    main()
