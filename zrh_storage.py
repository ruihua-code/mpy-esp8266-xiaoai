import os


def write_config(ssid, password):
    with open("wifi_config", 'w') as f:
        f.write(ssid+"\n")
        f.write(password+"\n")


def read_config():    
    if "wifi_config" in os.listdir():    
        with open("wifi_config", 'r') as f:
            ssid = f.readline()
            password = f.readline()
            return (ssid.strip(), password.strip())
    else:
        return None
