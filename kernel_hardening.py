#!/usr/bin/env python3
import subprocess

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

def harden_kernel():
    # Example: Disable IPv6
    run_command("echo 'net.ipv6.conf.all.disable_ipv6 = 1' | sudo tee -a /etc/sysctl.conf")
    run_command("echo 'net.ipv6.conf.default.disable_ipv6 = 1' | sudo tee -a /etc/sysctl.conf")

    # Reload sysctl to apply changes
    run_command("sudo sysctl -p")

if __name__ == "__main__":
    harden_kernel()
