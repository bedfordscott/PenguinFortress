#!/usr/bin/env python3
import subprocess

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Successfully executed: {command}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while executing {command}: {e}")

def enforce_strong_password_policy():
    print("Enforcing strong password policy...")

    # Install the required package for password quality control
    run_command("sudo apt-get install libpam-pwquality -y")

    # Update password policy
    with open('/etc/pam.d/common-password', 'a') as file:
        file.write('password requisite pam_pwquality.so retry=3 minlen=12 difok=3')

    print("Password policy updated.")

def disable_root_login():
    print("Disabling root login...")
    
    # This line disables root login via SSH
    run_command("sudo sed -i 's/^PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config")

    # Optionally, lock the root account
    run_command("sudo passwd -l root")

    print("Root login disabled.")

if __name__ == "__main__":
    enforce_strong_password_policy()
    disable_root_login()
