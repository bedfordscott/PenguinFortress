#!/usr/bin/env python3
import subprocess

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Successfully executed: {command}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while executing {command}: {e}")

def install_configure_ufw():
    print("Installing UFW...")
    run_command("sudo apt-get install ufw -y")

    print("Setting default UFW policies...")
    run_command("sudo ufw default deny incoming")
    run_command("sudo ufw default allow outgoing")

    # Add additional basic rules here. For example:
    # Allow SSH
    # run_command("sudo ufw allow ssh")

    # Enable UFW
    print("Enabling UFW...")
    run_command("sudo ufw enable")

if __name__ == "__main__":
    install_configure_ufw()
