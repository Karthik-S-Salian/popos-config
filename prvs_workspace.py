#!/usr/bin/env python3
import gi
import sys

gi.require_version("Wnck", "3.0")
gi.require_version("Gtk", "3.0")
from gi.repository import Wnck, Gtk, Gdk

def get_previous_workspace(screen):
    file_path = "/dev/shm/prev_workspace"
    
    try:
        with open(file_path, "r") as f:
            history_ids = f.read().splitlines()
    except FileNotFoundError:
        return None

    workspaces = screen.get_workspaces()
    if not workspaces:
        return None

    window_map = {w.get_xid(): w for w in screen.get_windows()}
    found_first = False

    for xid_str in history_ids:
        try:
            xid = int(xid_str)
            if xid in window_map:
                window = window_map[xid]
                if window.is_skip_tasklist():
                    continue
                
                if not found_first:
                    found_first = True
                    continue
                
                return window.get_workspace()
        except ValueError:
            continue

    return None

def main():
    screen = Wnck.Screen.get_default()
    screen.force_update()
    
    while Gtk.events_pending():
        Gtk.main_iteration()

    target_workspace = get_previous_workspace(screen)

    if target_workspace:
        target_workspace.activate(Gtk.get_current_event_time())

if __name__ == "__main__":
    main()
