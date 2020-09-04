#   Heights sockets Ex. 2.7 template - client side
#   Author: Barak Gonen, 2017


import socket


IP = "127.0.0.1"
PORT = 8850


def valid_request(request):
    """Check if the request is valid (is included in the available commands)

    Return:
        True if valid, False if not
    """
    request = request.split(" ", 1)[0]
    if request == "DIR" or request == "DELETE" or request == "COPY" or request == "EXECUTE" or request == "EXIT":
        return True
    else:
        return False


def send_request_to_server(my_socket, request):
    """Send the request to the server. First the length of the request (2 digits), then the request itself

    Example: '04EXIT'
    Example: '12DIR c:\cyber'
    """
    my_socket.send(request.encode('utf-8'))


def handle_server_response(my_socket, request):
    """Receive the response from the server and handle it, according to the request

    For example, DIR should result in printing the contents to the screen,
    while SEND_FILE should result in saving the received file and notifying the user
    """
    request = request.split(" ", 1)[0]
    response = my_socket.recv(1024).decode('utf-8')
    if response == "True":
        response = True
    if response == "False":
        response = False
    if request == "DIR":
        files_list = response.split(":")
        for file in files_list:
            print(file)
    elif request == "COPY":
        if response:
            print("Copied successfully")
        else:
            print("Couldn't copy")
    elif request == "DELETE":
        if response:
            print("Deleted successfully")
        else:
            print("Couldn't delete")
    elif request == "EXECUTE":
        if response:
            print("Executed")
        else:
            print("Error executing")


def main():
    # open socket with the server
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((IP, PORT))

    # print instructions
    print('Welcome to remote computer application. Available commands are:\n')
    print('DIR\nDELETE\nCOPY\nEXECUTE\nEXIT')

    done = False
    # loop until user requested to exit
    while not done:
        request = input("Please enter command:\n")
        if valid_request(request):
            send_request_to_server(my_socket, request)
            handle_server_response(my_socket, request)
            if request == 'EXIT':
                done = True
    my_socket.close()


if __name__ == '__main__':
    main()
