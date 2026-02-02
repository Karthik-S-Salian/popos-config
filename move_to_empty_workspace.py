#!/usr/bin/env python3
import gi
gi.require_version("Wnck", "3.0")
gi.require_version("Gtk", "3.0")
from gi.repository import Wnck, GdkX11, Gdk

screen = Wnck.Screen.get_default()
screen.force_update()

workspaces = screen.get_workspaces()
last_ws = workspaces[-1]
prev_ws = workspaces[-2] if len(workspaces) >= 2 else None

active_window = screen.get_active_window()
if not active_window:
    exit(0)

current_ws = active_window.get_workspace()

# Count windows in previous workspace
def windows_in_workspace(ws):
    return [
        w for w in screen.get_windows()
        if w.get_workspace() == ws and not w.is_skip_tasklist()
    ]

# Check conditions
if current_ws == prev_ws:
    prev_ws_windows = windows_in_workspace(prev_ws)
    last_ws_windows = windows_in_workspace(last_ws)

    # If previous workspace has only this window AND last workspace is empty  do nothing
    if len(prev_ws_windows) == 1 and prev_ws_windows[0] == active_window and len(last_ws_windows) == 0:
        exit(0)

# Otherwise move to last workspace
active_window.move_to_workspace(last_ws)

now = GdkX11.x11_get_server_time(
    GdkX11.X11Window.lookup_for_display(
        Gdk.Display.get_default(),
        GdkX11.x11_get_default_root_xwindow()
    )
)
active_window.activate(now)
