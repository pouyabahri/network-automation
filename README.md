# Network Automation using Python and Ansible
This GitHub Repo focuses on using [NAPALM](https://github.com/napalm-automation/napalm) for automating network management on Cisco IOS devices.

This project aims to streamline network management tasks by utilizing NAPALM for network automation. NAPALM is a Python library that allows consistent interaction with network devices, regardless of vendor which simplifies configuration management and orchestration. It is a powerful solution for automating network operations.

## Version History

### v1.1 (Latest)
- New: Added ping before establishing SSH session.

```python
import subprocess

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
