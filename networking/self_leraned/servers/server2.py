#   Heights sockets Ex. 2.7 template - server side
#   Author: Barak Gonen, 2017

import socket
import glob
import os
import shutil
import subprocess
from pathlib import Path

IP = "0.0.0.0"
PORT = 8850


def receive_client_request(client_socket):
    """Receives the full message sent by the client

    Works with the protocol defined in the client's "send_request_to_server" function

    Returns:
        command: such as DIR, EXIT, SCREENSHOT etc
        params: the parameters of the command

    Example: 12DIR c:\cyber as input will result in command = 'DIR', params = 'c:\cyber'
    """
    client_message = client_socket.recv(1024).decode('utf-8')
    command, params = client_message.split(" ", 1)
    return command, params


def check_client_request(command, params):
    """Check if the params are good.

    For example, the filename to be copied actually exists

    Returns:
        valid: True/False
        error_msg: None if all is OK, otherwise some error message
    """
    if command == "DIR":
        files_list = glob.glob(params + "/*.*")
        if len(files_list) < 0:
            return False, IOError
        else:
            return True, None
    if command == "DELETE":
        files_list = glob.glob(params + "/*.*")
        for file in files_list:
            if file == params:
                return True, None
        return False, FileNotFoundError
    if command == "COPY":
        files_list = params.split(" ")
        for file in files_list:
            if os.path.isfile(file):
                return True, None
            else:
                return False, FileNotFoundError
    elif command == "EXECUTE":
        return True, None


def handle_client_request(command, params):
    """Create the response to the client, given the command is legal and params are OK

    For example, return the list of filenames in a directory

    Returns:
        response: the requested data
    """
    if command == "DIR":
        files_list = glob.glob(params + "/*.*")
        files_list = "".join(files_list)
        return files_list
    elif command == "DELETE":
        os.remove(params)
        return "True"
    elif command == "COPY":
        src, dst = params.split(' ')
        shutil.copy(src, dst)
        return "True"
    elif command == "EXECUTE":
        subprocess.call(str(params)[:str(params).index(".")])
        return "True"


def send_response_to_client(response, client_socket):
    """Create a protocol which sends the response to the client

    The protocol should be able to handle short responses as well as files
    (for example when needed to send the screenshot to the client)
    """
    client_socket.send(response.encode('utf-8'))


def main():
    # open socket with client
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen(5)
    client_socket, client_address = server_socket.accept()

    # handle requests until user asks to exit
    done = False
    while not done:
        command, params = receive_client_request(client_socket)
        valid, error_msg = check_client_request(command, params)
        if valid:
            response = handle_client_request(command, params)
            send_response_to_client(response, client_socket)
        else:
            send_response_to_client(error_msg, client_socket)

        if command == 'EXIT':
            done = True

    client_socket.close()
    server_socket.close()


if __name__ == '__main__':
    main()
