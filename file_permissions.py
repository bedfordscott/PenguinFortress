#!/usr/bin/env python3
import subprocess

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Successfully executed: {command}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while executing {command}: {e}")

def set_file_permissions():
    print("Setting file permissions...")

    # Set permissions for critical system files
    # Example: Secure /etc/passwd and /etc/shadow
    run_command("sudo chmod 644 /etc/passwd")
    run_command("sudo chmod 600 /etc/shadow")

    # Secure SSH private keys
    run_command("sudo chmod 600 /etc/ssh/ssh_host_*_key")

    # Additional file permissions can be set here

def set_directory_permissions():
    print("Setting directory permissions...")

    # Example: Secure the /etc directory
    run_command("sudo chmod 755 /etc")

    # Additional directory permissions can be set here

if __name__ == "__main__":
    set_file_permissions()
    set_directory_permissions()
