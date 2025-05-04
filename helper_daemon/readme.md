## Helper daemon:
It will contains all the scripts that require to listen for system events

### 📦 Features
Tracks the previously focused workspace.


### 🚀 Requirements
Python 3

GTK 3

libwnck-3

gi.repository (PyGObject)

### Install dependencies:

```bash
sudo apt install python3-gi gir1.2-gtk-3.0 gir1.2-wnck-3.0
pip install pygobject

```

### 🛠 Installation

clone and cd into here

make file executable
```bash
find . -type f -name "*.py" -exec chmod +x {} \;
```


Run the included generator to create a systemd user service:
```bash
python3 generate_service.py
```

Enable and start the user service:
```bash
systemctl --user daemon-reexec
systemctl --user daemon-reload
systemctl --user enable --now helper-daemon.service
```