#!/usr/bin/env python3
import os
import sys

SERVICE_TEMPLATE = """[Unit]
Description=Workspace Tracker Daemon
# Ensures the service waits for the GUI to be ready
After=graphical-session.target

[Service]
ExecStart={python_exe} {script_path}
Restart=always
RestartSec=3

[Install]
# Standard for user-level services
WantedBy=default.target
"""

def generate_service_file(script_filename="src/main.py", output_filename="workspace-tracker.service"):
    # 1. Get absolute path to the target script
    # Assuming the tracker script is in the same folder as this generator
    current_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_dir, script_filename)

    if not os.path.exists(script_path):
        print(f"Error: Could not find {script_path}")
        return

    # 2. Define the systemd user config path
    service_dir = os.path.expanduser("~/.config/systemd/user/")
    service_file_path = os.path.join(service_dir, output_filename)

    # 3. Format the content
    content = SERVICE_TEMPLATE.format(
        python_exe=sys.executable, # Uses the current python path automatically
        script_path=script_path
    )

    # 4. Write the file
    try:
        os.makedirs(service_dir, exist_ok=True)
        with open(service_file_path, "w") as f:
            f.write(content)
        print(f"✅ Service file written to: {service_file_path}")
        print("\nNext steps:")
        print(f"  systemctl --user daemon-reload")
        print(f"  systemctl --user enable {output_filename}")
        print(f"  systemctl --user start {output_filename}")
    except OSError as e:
        print(f"❌ Failed to write file: {e}")

if __name__ == "__main__":
    generate_service_file()
