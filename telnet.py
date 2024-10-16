pip install paramiko
import telnetlib
import time

# Telnet connection parameters
HOST = "192.168.56.101"  # Replace with your device's IP
USERNAME = "cisco"     # Replace with your username
PASSWORD = "cisco123!"  # Replace with your password
NEW_HOSTNAME = "R1"

# Establish Telnet connection
tn = telnetlib.Telnet(HOST)

# Login
tn.read_until(b"Username: ")
tn.write(USERNAME.encode('ascii') + b"\n")
tn.read_until(b"Password: ")
tn.write(PASSWORD.encode('ascii') + b"\n")

# Change hostname
tn.write(b"configure terminal\n")
tn.write(f"hostname {NEW_HOSTNAME}\n".encode('ascii'))
tn.write(b"end\n")

# Show running configuration
tn.write(b"show running-config\n")
time.sleep(2)  # Wait for the command to execute
output = tn.read_very_eager().decode('ascii')

# Save to file
with open('running_config_telnet.txt', 'w') as file:
    file.write(output)

# Close connection
tn.write(b"exit\n")
tn.close()

print("Telnet connection established, hostname changed, and running configuration saved.")
