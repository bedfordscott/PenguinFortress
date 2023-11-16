# PenguinFortress
## Linux Security Suite
### Overview
The Linux Security Suite is a comprehensive collection of scripts designed to enhance the security of Linux systems. This suite covers a wide range of security aspects including system updates, user management, network security, file permissions, and more, providing a robust approach to hardening Linux environments.

### Contents
This suite contains the following scripts:

audit_logging.py: Configures audit logging.
cron_job_security.py: Secures cron jobs.
file_permissions.py: Sets secure file permissions.
firewall_configuration.py: Configures the firewall.
kernel_hardening.py: Applies kernel-level security enhancements.
malware_scanning.py: Sets up malware scanning tools.
network_security.py: Secures network configurations.
service_management.py: Manages system services.
ssh_hardening.py: Secures SSH configurations.
update_system.py: Updates the system packages.
user_management.py: Manages user accounts and enforces password policies.
main.py: The main script that runs all the above scripts.

### Prerequisites
Python 3.x
Root or sudo access on the system
Tested on Debian-based Linux systems (adjustments may be required for other distributions)
### Usage
To use the Linux Security Suite, clone this repository and run the main.py script:

git clone [repo-url]
cd [repo-directory]
sudo python3 main.py

### Warning
This suite performs significant changes to system configurations. Use with caution.
It is highly recommended to test each script individually in a non-production environment before running the entire suite.
Ensure you have proper backups and recovery procedures in place.

### Customization
Each script can be modified to suit specific security requirements and environments. Please review and test any changes thoroughly before implementation.

### Contributions
Contributions to the Linux Security Suite are welcome. Please submit pull requests for any enhancements, bug fixes, or improvements.
