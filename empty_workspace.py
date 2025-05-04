#!/usr/bin/env python3
import gi
gi.require_version("Wnck", "3.0")
gi.require_version("Gtk", "3.0")
from gi.repository import Wnck, Gtk

screen = Wnck.Screen.get_default()
screen.force_update()

# list existing workspaces
workspaces = screen.get_workspaces()
last_workspace = workspaces[-1]
last_workspace.activate(Gtk.get_current_event_time())