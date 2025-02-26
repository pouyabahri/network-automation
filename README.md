# Network Automation using Python and Ansible

## Overview

This project focuses on automating network configuration, management, and monitoring tasks using Ansible and Python. It simplifies repetitive network operations, enhances consistency, and reduces human errors.

## Prerequisites

- Python 3.x

- Ansible 2.9+

## Version History

### v1.2
- New: Added backup capability.
```python
def create_backup_log(hosts, commands):
    """Create a backup log file in the Downloads folder."""
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_filename = f"config_backup_{timestamp}.txt"
    backup_filepath = os.path.join(downloads_path, backup_filename)
    
    try:
        with open(backup_filepath, "w") as backup_file:
            for host in hosts:
                backup_file.write(f"Device IP: {host['hostname']}\n")
                backup_file.write("Commands Executed:\n")
                backup_file.write("\n".join(commands) + "\n\n")
        print(f"📂 Backup saved: {backup_filepath}")
    except Exception as e:
        print(f"❌ Error saving backup: {e}")
```

## References

- [ansible-napalm-samples](https://github.com/network-automation/ansible-napalm-samples)
