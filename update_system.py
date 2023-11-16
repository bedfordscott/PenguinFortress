#!/usr/bin/env python3
import subprocess

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Successfully executed: {command}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while executing {command}: {e}")

def update_system():
    print("Updating the system...")

    # Update package list
    run_command("sudo apt-get update")

    # Upgrade all installed packages
    run_command("sudo apt-get upgrade -y")

    # Optionally, you can include a dist-upgrade
    # run_command("sudo apt-get dist-upgrade -y")

    # Clean up
    run_command("sudo apt-get autoremove -y")
    run_command("sudo apt-get autoclean")

if __name__ == "__main__":
    update_system()
