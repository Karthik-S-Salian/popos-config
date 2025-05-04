#!/usr/bin/env python3
import gi
gi.require_version("Wnck", "3.0")
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Wnck, GdkX11, Gdk

screen = Wnck.Screen.get_default()
screen.force_update()

active_workspace = screen.get_active_workspace()
active_window = screen.get_active_window()

# Get windows in the current workspace
windows = []
for window in screen.get_windows():
    if window.is_in_viewport(active_workspace) and not window.is_skip_tasklist():
        windows.append(window)
        
        
if len(windows)<2:
    exit(0)

# Sort by stacking order (bottom to top, topmost is last)
windows.sort(key=lambda w: w.get_sort_order())

if active_window in windows:
    idx = windows.index(active_window)
    next_idx = (idx + 1) % len(windows)
    next_window = windows[next_idx]
else:
    # If no active window or not found in list, activate first
    next_window = windows[0]


now = GdkX11.x11_get_server_time(GdkX11.X11Window.lookup_for_display(Gdk.Display.get_default(),
GdkX11.x11_get_default_root_xwindow()))
next_window.activate(now)
