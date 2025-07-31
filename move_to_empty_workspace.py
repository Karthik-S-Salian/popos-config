import gi
gi.require_version("Wnck", "3.0")
gi.require_version("Gtk", "3.0")
from gi.repository import Wnck, GdkX11, Gdk

screen = Wnck.Screen.get_default()
screen.force_update()

workspaces = screen.get_workspaces()

active_screen = screen.get_active_window()

if not active_screen:
    exit(0)

active_screen.move_to_workspace(workspaces[-1])

now = GdkX11.x11_get_server_time(GdkX11.X11Window.lookup_for_display(Gdk.Display.get_default(),
GdkX11.x11_get_default_root_xwindow()))
active_screen.activate(now)