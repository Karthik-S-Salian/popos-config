#!/usr/bin/env python3
import gi
import os

gi.require_version("Wnck", "3.0")
gi.require_version("Gtk", "3.0")
from gi.repository import Wnck, Gtk

HISTORY_FILE = "/dev/shm/prev_workspace"
MAX_HISTORY = 20

def on_active_window_changed(screen, _):
    active_window = screen.get_active_window()
    if not active_window or active_window.is_skip_tasklist():
        return

    window_id = str(active_window.get_xid())
    history = []

    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r") as f:
                history = f.read().splitlines()
        except OSError:
            pass

    if window_id in history:
        history.remove(window_id)
    
    history.insert(0, window_id)
    history = history[:MAX_HISTORY]

    try:
        with open(HISTORY_FILE, "w") as f:
            f.write("\n".join(history))
    except OSError:
        pass
        
    with open(HISTORY_FILE, "r") as f:
            print(f.read())

def main():
    # Initialize file
    open(HISTORY_FILE, "w").close()
    
    screen = Wnck.Screen.get_default()
    screen.force_update()
    screen.connect("active-window-changed", on_active_window_changed)
    Gtk.main()

if __name__ == "__main__":
    main()
