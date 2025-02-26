# Network Automation using Python and Ansible
This GitHub Repo focuses on using [Ansible](https://www.redhat.com/en/technologies/management/ansible/network-automation?sc_cid=7015Y000003t7aWQAQ) and [NAPALM](https://github.com/napalm-automation/napalm) for automating network management on Cisco IOS devices.

This project aims to streamline network management tasks by utilizing NAPALM and Ansible for network automation. NAPALM is a Python library that enables consistent interaction with network devices, regardless of vendor. Ansible, an agentless automation tool, simplifies configuration management and orchestration. Together, these technologies form a powerful solution for automating network operations.

## Prerequisites

- Python 3.x

- Ansible 2.9+

## Version History

### v1.2 (Latest)
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
### v1.1
- New: Added ping before establishing SSH session.
```python
def ping_host(hostname):
    """Ping a host to check if it is reachable."""
    try:
        result = subprocess.run(["ping", "-n", "1", hostname], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return result.returncode == 0  # 0 means the host is reachable
    except Exception:
        return False

for host in hosts:
        hostname = host['hostname']
        print(f'🔎 Pinging {hostname}...')
        if ping_host(hostname):
            print(f'✅ {hostname} is reachable. Proceeding with configuration...')
            push_ios_config(host['hostname'], host['username'], host['password'], config_commands)
        else:
            print(f'❌ {hostname} is unreachable. Skipping configuration.')
```
### v1.0
- Initial release.

## References

- [ansible-napalm-samples](https://github.com/network-automation/ansible-napalm-samples)
