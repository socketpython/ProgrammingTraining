import socket
import subprocess as sub

IP = socket.gethostbyname(socket.gethostname())
PORT = 7654


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((IP, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                command = conn.recv(1024).decode()
                proc = sub.Popen(command, stdout=sub.PIPE, stderr=sub.PIPE, shell=True)
                out, err = proc.communicate()
                print(out.decode(), err)
                if out:
                    conn.send(str(len(out)).encode())
                    conn.send(out)
                elif err:
                    conn.send(str(len(err)).encode())
                    conn.send(err)
                else:
                    msg = "There is no output for your command".encode()
                    conn.send(str(len(msg)).encode())
                    conn.send(msg)


if __name__ == "__main__":
    main()
