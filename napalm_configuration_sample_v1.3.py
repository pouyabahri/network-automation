import napalm
import subprocess

def ping_host(hostname):
    """Ping a host to check if it is reachable and capture the failure reason if unreachable."""
    try:
        result = subprocess.run(["ping", "-n", "1", hostname], capture_output=True, text=True, timeout=3)
        output = result.stdout.lower()

        if "request timed out" in output:
            return False, "Request Timed Out."
        elif "destination host unreachable" in output:
            return False, "Destination Host Unreachable."
        elif result.returncode == 0:
            return True, "Host is Reachable."
        else:
            return False, "Unknown Error"
    except subprocess.TimeoutExpired:
        return False, "Ping Command Timed Out."
    except Exception as e:
        return False, f"Error: {str(e)}"

def push_ios_config(hostname, username, password, config_commands):
    try:
        driver = napalm.get_network_driver('ios')  # Cisco IOS Driver
        device = driver(hostname=hostname, username=username, password=password, optional_args={'transport': 'ssh'})
        
        print(f'🔌 Connecting to {hostname} via SSH...')
        device.open()  # Attempting SSH connection
        
        config_string = '\n'.join(config_commands)
        device.load_merge_candidate(config=config_string)
        
        choice = input(f"💾 Commit changes on {hostname}? [y/N]: ")
        if choice.lower() == 'y':
            print(f'✅ Committing changes to {hostname}...')
            device.commit_config()
            print('Done.')
        else:
            print('❌ Discarding changes...')
            device.discard_config()

        device.close()
        print(f'🔒 Connection to {hostname} closed.\n')
    
    except napalm.base.exceptions.ConnectionException as e:
        print(f'❌ SSH Connection error with {hostname}: {e}')
    except Exception as e:
        print(f'❌ Error configuring {hostname}: {e}')

def main():
    hosts = [
        {'hostname': '203.0.0.1', 'username': 'admin', 'password': 'password123'},
        {'hostname': '192.168.1.1', 'username': 'admin', 'password': 'password123'}
    ]
    
    config_commands = [
        "hostname SW-CORE-1",

        "vlan 10",
        "vlan 20",
        "vlan 100",

        "spanning-tree vlan 10 root primary",
        "spanning-tree vlan 20 root primary",

        "track 10 int gi0/1 line-protocol",
        "track 20 int gi0/1 line-protocol",

        "int vlan 10",
        "no shut",
        "ip address 192.168.10.2 255.255.255.0",
        "standby 10 ip 192.168.10.1",
        "standby 10 priority 110",
        "standby 10 preempt",
        "standby 10 track 10 decrement 20",
        "standby 10 authentication 123",

        "int vlan 20",
        "no shut",
        "ip address 172.16.20.2 255.255.255.0",
        "standby 20 ip 172.16.20.1",
        "standby 20 priority 110",
        "standby 20 preempt",
        "standby 20 track 10 decrement 20",
        "standby 20 authentication 123",
        
        "int vlan 100",
        "no shut",
        "ip address 172.16.110.242 255.255.255.0",

        "ip routing",

        "ip default-gateway 172.16.110.241",

        "int gi0/1",
        "no shut",
        "switchport trunk encapsulation dot1q",
        "switchport mode trunk",

        "int gi0/2",
        "no shut",
        "switchport trunk encapsulation dot1q",
        "switchport mode trunk",
    ]
    
    for host in hosts:
        hostname = host['hostname']
        print(f'🔎 Pinging {hostname}...')
        reachable, reason = ping_host(hostname)
        if reachable:
            print(f'✅ {hostname} is reachable. Proceeding with configuration...')
            push_ios_config(host['hostname'], host['username'], host['password'], config_commands)
        else:
            print(f'❌ {hostname} is unreachable. Reason: {reason}')

if __name__ == '__main__':
    main()
