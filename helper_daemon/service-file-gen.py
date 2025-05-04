#!/usr/bin/env python3
import os

SERVICE_TEMPLATE = """[Unit]
Description=General Utility Daemon
After=graphical.target

[Service]
ExecStart=/usr/bin/env python3 {script_path}
Restart=on-failure

[Install]
WantedBy=default.target
"""

def generate_service_file(script_filename="src/main.py", output_path="~/.config/systemd/user/helper-daemon.service"):
    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_script_dir, script_filename)
    service_file_path = os.path.expanduser(output_path)
    content = SERVICE_TEMPLATE.format(script_path=script_path)
    os.makedirs(os.path.dirname(service_file_path), exist_ok=True)
    
    
    with open(service_file_path, "w") as f:
        f.write(content)

    print(f"Systemd service file written to: {service_file_path}")

if __name__ == "__main__":
    generate_service_file()
