#!/usr/bin/env python3
from audit_logging import configure_auditd
from cron_job_security import secure_cron_jobs
from file_permissions import set_file_permissions, set_directory_permissions
from firewall_configuration import install_configure_ufw
from kernel_hardening import harden_kernel
from malware_scanning import install_configure_malware_scanner
from network_security import disable_unused_network_services, secure_network_protocols
from service_management import disable_unnecessary_services
from ssh_hardening import harden_ssh
from update_system import update_system
from user_management import enforce_strong_password_policy, disable_root_login

def main():
    print("Starting system hardening process...")
    
    # Update system
    update_system()

    # User management
    enforce_strong_password_policy()
    disable_root_login()

    # SSH hardening
    harden_ssh()

    # Firewall configuration
    install_configure_ufw()

    # File permissions
    set_file_permissions()
    set_directory_permissions()

    # Network security
    disable_unused_network_services()
    secure_network_protocols()

    # Service management
    disable_unnecessary_services()

    # Audit logging
    configure_auditd()

    # Cron job security
    secure_cron_jobs()

    # Kernel hardening
    harden_kernel()

    # Malware scanning
    install_configure_malware_scanner()

    print("System hardening process completed.")

if __name__ == "__main__":
    main()
