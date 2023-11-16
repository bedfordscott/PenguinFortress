#!/usr/bin/env python3
import subprocess

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

def secure_cron_jobs():
    # Restricting permissions for cron directories
    cron_dirs = ['/etc/cron.d', '/etc/cron.daily', '/etc/cron.hourly', '/etc/cron.monthly', '/etc/cron.weekly']
    for dir in cron_dirs:
        run_command(f"sudo chmod -R go-rwx {dir}")
        print(f"Secured {dir}")

if __name__ == "__main__":
    secure_cron_jobs()
