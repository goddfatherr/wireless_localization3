import pandas as pd
import subprocess
import re

#This script scans and finds available APs (windows machine implementation)

output_file = "output.txt"

aps = []

bssid = signal_strength = detected_aps = None


def execute_netsh_cmd():

    netsh_command = ["netsh", "wlan", "show", "network", "mode=BSSID"]

    with open(output_file, "w") as f:
        subprocess.run(netsh_command, stdout=f, text=True)


def detect_aps():

    #parses the output of the netsh cmd

    execute_netsh_cmd()

    global aps, bssid, signal_strength, detected_aps

    aps = []

    with open(output_file, "r") as f:
    
        for line in f:

            if line.strip().startswith("BSSID"):
                bssid = ":".join(line.split(":")[1:]).strip()

            elif line.strip().startswith("Signal"):
                signal_strength = float(line.split(":")[1].strip().strip('%'))

                aps.append({
                    "bssid": bssid,
                    "dBm_signal": signal_strength,
                })  

        detected_aps = pd.DataFrame(aps)



    