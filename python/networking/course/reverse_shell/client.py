import socket

IP = "192.168.1.101"
PORT = 7654


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    while True:
        command = input("Enter command: ").encode()
        s.send(command)
        length = int(s.recv(1024).decode())
        print(length)
        output = s.recv(length).decode()
        print(output)


if __name__ == "__main__":
    main()
