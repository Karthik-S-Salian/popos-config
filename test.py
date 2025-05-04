#!/usr/bin/env python3
import gi
gi.require_version("Wnck", "3.0")
gi.require_version("Gtk", "3.0")
from gi.repository import Wnck, Gtk

screen = Wnck.Screen.get_default()
screen.force_update()

active_workspace = screen.get_active_workspace()
active_window = screen.get_active_window()

for w in screen.get_windows():
    if not w.is_skip_tasklist():
        print(w.get_xid())