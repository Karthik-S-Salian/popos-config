#!/usr/bin/env python3
import gi
gi.require_version("Wnck", "3.0")
gi.require_version("Gtk", "3.0")
from gi.repository import Wnck, Gtk

screen = Wnck.Screen.get_default()
screen.force_update()

# list existing workspaces
workspaces = screen.get_workspaces()
# get the (index of) current one
currws = workspaces.index(screen.get_active_workspace())

# len(workspaces)-1  because last workspace will always be empty so skip that
next_workspace = workspaces[(currws + 1)%(len(workspaces)-1)]
# and activate it...
next_workspace.activate(Gtk.get_current_event_time())