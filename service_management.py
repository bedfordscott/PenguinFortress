#!/usr/bin/env python3
import subprocess

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

def disable_unnecessary_services():
    services_to_disable = ['nfs-server', 'cups', 'smbd', 'snmpd']
    for service in services_to_disable:
        run_command(f"sudo systemctl disable {service}")
        run_command(f"sudo systemctl stop {service}")
        print(f"Disabled and stopped {service}")

if __name__ == "__main__":
    disable_unnecessary_services()
