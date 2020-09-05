import socket


IP = socket.gethostname()
PORT = 7654

done = False

while not done:
    client_socket = socket.socket()
    client_socket.connect((IP, PORT))
    user_choice = input("Select: ENCRYPT, DECRYPT or EXIT")
    if user_choice == "EXIT":
        client_socket.send("EXIT".encode('utf-8'))
        done = True
        break
    else:
        client_socket.send(user_choice.encode('utf-8'))
        server_ans = client_socket.recv(1024).decode("utf-8")
        client_socket.close()
        print(server_ans)

