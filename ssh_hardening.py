#!/usr/bin/env python3
import subprocess

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Successfully executed: {command}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while executing {command}: {e}")

def harden_ssh():
    print("Hardening SSH configuration...")

    # Disable root SSH login
    run_command("sudo sed -i 's/^PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config")

    # Disable SSH password authentication, enforce key-based authentication
    run_command("sudo sed -i 's/^#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config")
    run_command("sudo sed -i 's/^PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config")

    # Optionally, change the default SSH port (e.g., to 2222)
    # run_command("sudo sed -i 's/^#Port 22/Port 2222/' /etc/ssh/sshd_config")

    # Reload SSH to apply changes
    run_command("sudo systemctl reload sshd")

if __name__ == "__main__":
    harden_ssh()
