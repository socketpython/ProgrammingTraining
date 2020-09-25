import subprocess


def main():
    pcap_path = r"C:\Users\Elad_Levi\Downloads\SummerWinds.pcapng"
    #filter_request = 'icmp and '
    command = f"tshark -r {pcap_path} -Y \"icmp.type == 8\""

    res = subprocess.Popen(command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True)
    out, err = res.communicate()

    if out:
        packets = out.decode().split("\n")
        attacker_ip = ""
        victims_ip = []
        for packet in packets:
            if len(packet) > 20:
                vals = packet.split(" ")
                new_list = []
                for val in vals:
                    if val != "":
                        new_list.append(val)
                attacker_ip = new_list[2]
                victims_ip.append(new_list[4])

        print(f"The attacker's ip is: {attacker_ip}")
        count = 1
        for ip in victims_ip:
            print(f"Victim number {count}: {ip}")
            count += 1
    else:
        print(err.decode())


if __name__ == "__main__":
    main()
