import socket

current_port = 8111
ip = "127.0.0.1"


def receive_msg(client_socket):
    message = client_socket.recv(1024).decode('utf-8')
    next_port = int(message[-4:])
    message = message[:-4]
    return message, next_port


done = False

while not done:
    my_socket = socket.socket()
    my_socket.connect((ip, current_port))
    msg = input("Enter the message and in the end enter the next port\n")
    current_port = int(msg[-4:])
    if msg == "exit":
        done = True
        break
    my_socket.send(msg.encode('utf-8'))
    my_socket.close()

    my_socket = socket.socket()
    my_socket.bind((ip, current_port))
    my_socket.listen(1)
    print(f"Side B listening to port {current_port}")

    client_socket, client_address = my_socket.accept()
    message, current_port = receive_msg(client_socket)
    print("Side A: " + message)
    print("Side A disconnected")
    my_socket.close()

my_socket.close()
