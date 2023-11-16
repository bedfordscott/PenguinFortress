#!/usr/bin/env python3
import subprocess

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

def setup_intrusion_detection():
    # Example: Installing and configuring Fail2Ban
    run_command("sudo apt-get install fail2ban -y")
    run_command("sudo systemctl enable fail2ban")
    run_command("sudo systemctl start fail2ban")

if __name__ == "__main__":
    setup_intrusion_detection()
