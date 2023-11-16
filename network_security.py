#!/usr/bin/env python3
import subprocess

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Successfully executed: {command}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while executing {command}: {e}")

def disable_unused_network_services():
    print("Disabling unused network services...")

    # Example: Disable Telnet
    run_command("sudo systemctl disable telnetd")

    # Example: Disable FTP
    run_command("sudo systemctl disable vsftpd")

    # Add commands to disable other unused network services

def secure_network_protocols():
    print("Securing network protocols...")

    # Example: Disable IPv6 if not used
    run_command("echo 'net.ipv6.conf.all.disable_ipv6 = 1' | sudo tee -a /etc/sysctl.conf")
    run_command("echo 'net.ipv6.conf.default.disable_ipv6 = 1' | sudo tee -a /etc/sysctl.conf")
    run_command("sudo sysctl -p")

    # Add other commands to secure network protocols as per your requirements

if __name__ == "__main__":
    disable_unused_network_services()
    secure_network_protocols()
