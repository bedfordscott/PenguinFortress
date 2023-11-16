#!/usr/bin/env python3
import subprocess

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

def configure_auditd():
    # Install auditd if not already installed
    run_command("sudo apt-get install auditd -y")
    
    # Enable and start auditd service
    run_command("sudo systemctl enable auditd")
    run_command("sudo systemctl start auditd")

    # Example rule: Log all actions by the root user
    with open('/etc/audit/audit.rules', 'a') as file:
        file.write('-w /etc/sudoers -p wa -k actions_root')

    # Restart auditd to apply changes
    run_command("sudo systemctl restart auditd")

if __name__ == "__main__":
    configure_auditd()
