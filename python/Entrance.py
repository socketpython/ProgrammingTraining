units = ["1133", "2222", "4546", "7878", "9999", "1919"]
incidents = ["standard malware", "apt", "live intruder", "data leakage"]
events = {}


def start():
    private_num = int(input("Enter your private number: "))
    user_name = input("Enter your user name: ")
    unit_num = input("Enter the unit number: ")
    if unit_num == "?":
        print(units)
        unit_num = input("Enter the unit number: ")
    if units.count(unit_num) == 0:
        print("The unit does not exist")
        unit_num = input("Enter the unit number: ")
    date = input("Enter the date(dd/mm/yyyy): ")
    incident_type = input(f"Enter the type of the incident{incidents}: ").lower()
    if incident_type == "other":
        incident_type = input(f"Enter the type of the incident: ").lower()
        incidents.append(incident_type)
    for inc in incidents:
        if incident_type == inc:
            if inc == incidents[0]:
                malware_type = input("Enter the type of the malware(Worm - 1, Trojan Horse - 2, Rootkit - 3): ")
                if malware_type == "1":
                    event_key = incident_type.capitalize() + " - Worm"
                elif malware_type == "2":
                    event_key = incident_type.capitalize() + " - Trojan Horse"
                elif malware_type == "3":
                    event_key = incident_type.capitalize() + " - Rootkit"
                
                severity = input("Enter the severity of the event (Critical - 1, Medium - 2, Low - 3): ")
                if malware_type == "1":
                    severity_level = "Critical"
                elif malware_type == "2":
                    severity_level = "Medium"
                elif malware_type == "3":
                    severity_level = "Low"
                events[event_key] = severity_level

            elif inc == incidents[1] or inc == incidents[0] or unit_num == "2222" or unit_num == "1919":
                events[inc] = "Critical"
            
            else:
                event_key = inc
                severity = input("Enter the severity of the event (Critical - 1, Medium - 2, Low - 3")
                if malware_type == "1":
                    severity_level = "Critical"
                elif malware_type == "2":
                    severity_level = "Medium"
                elif malware_type == "3":
                    severity_level = "Low"
                events[event_key] = severity_level
    path = r"C:\Logs\logfile.txt"
    
    with open(path, "a") as f:
        data = f"""
Name: {user_name}
Unit: {unit_num}
Personal: {private_num}
Incident Type: {event_key}, Risk: {severity_level}
Incident's Date: {date}
{"*" * 60}
"""
        f.write(data)
