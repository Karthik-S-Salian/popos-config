#!/usr/bin/env python3
import gi
gi.require_version("Wnck", "3.0")
gi.require_version("Gtk", "3.0")
from gi.repository import Wnck, Gtk

def on_workspace_changed(screen, _):
    
    previous_active_windows = []
    
    with open("/dev/shm/prev_workspace", "r") as f:
        previous_active_windows = f.read().split()
        
    if not screen.get_active_window() or screen.get_active_window().is_skip_tasklist():
        return

    current_active_window_id = str(screen.get_active_window().get_xid())
    
    if current_active_window_id in previous_active_windows:
        previous_active_windows.remove(current_active_window_id)
    previous_active_windows.insert(0,current_active_window_id)
    
    print(previous_active_windows)
    with open("/dev/shm/prev_workspace", "w") as f:
        f.write("\n".join(previous_active_windows))
    
# Initialize the screen and force update
screen = Wnck.Screen.get_default()
screen.force_update()

# Connect to the 'active_workspace_changed' signal
screen.connect("active_window_changed", on_workspace_changed)

with open("/dev/shm/prev_workspace", "w") as f:
    pass

# Start the GTK main loop to listen for events
Gtk.main()

