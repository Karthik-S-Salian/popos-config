#!/usr/bin/env python3
import gi
gi.require_version("Wnck", "3.0")
gi.require_version("Gtk", "3.0")
from gi.repository import Wnck, Gtk

screen = Wnck.Screen.get_default()
screen.force_update()

previous_active_windows = []

with open("/dev/shm/prev_workspace", "r") as f:
    previous_active_windows = f.read().split()
    
def get_prvs_workspace():
    workspaces = screen.get_workspaces()
    
    if len(workspaces)<2:
        return None

    windows = {x.get_xid():x for  x in screen.get_windows()}
    
    
    for w in screen.get_windows():
        print(w.get_xid(),w.get_name())
    
    print(previous_active_windows)
    
    print(windows)
    
    first = True
    for window in previous_active_windows:
        
        window_id  = int(window)
        if window_id in windows and not windows[window_id].is_skip_tasklist():
            if first:
                first = False
            else:
                print("insde")
                return windows[window_id].get_workspace()
    return workspaces[-1]

prvs_workspace = get_prvs_workspace()

if prvs_workspace:
    prvs_workspace.activate(Gtk.get_current_event_time())