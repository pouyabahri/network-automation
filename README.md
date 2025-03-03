# Network Automation using Python and Ansible
This GitHub Repo focuses on using [NAPALM](https://github.com/napalm-automation/napalm) for automating network management on Cisco IOS devices.

This project aims to streamline network management tasks by utilizing NAPALM for network automation. NAPALM is a Python library that allows consistent interaction with network devices, regardless of vendor which simplifies configuration management and orchestration. It is a powerful solution for automating network operations.

## Version History

### v1.3 (Latest)
- New: Added specific error handling for Ping failures (e.g., "Request Timed Out", "Destination Host Unreachable").

```python
if "request timed out" in output:
            return False, "Request Timed Out"
        elif "destination host unreachable" in output:
            return False, "Destination Host Unreachable"
        elif result.returncode == 0:
            return True, "Host is Reachable"
        else:
            return False, "Unknown Error"
    except subprocess.TimeoutExpired:
        return False, "Ping Command Timed Out"
    except Exception as e:
        return False, f"Error: {str(e)}"
```
Output:
```
🔎 Pinging 203.0.0.1...
❌ 203.0.0.1 is unreachable. Reason: Request Timed Out
```

### v1.2
- New: Added specific error handling for SSH connection failures (e.g., authentication issues, timeouts).

```python
    except napalm.base.exceptions.ConnectionException as e:
        print(f'❌ SSH Connection error with {hostname}: {e}')
    except Exception as e:
        print(f'❌ Error configuring {hostname}: {e}')
```
Output:
```
🔎 Pinging 203.0.0.1...
✅ 203.0.0.1 is reachable. Proceeding with configuration...
🔌 Connecting to 203.0.0.1 via SSH...
❌ SSH Connection error with 203.0.0.1: Authentication failed.
```

### v1.1
- New: Added ping before establishing SSH session.
- Improved console output.

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
