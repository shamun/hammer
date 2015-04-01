import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst
from gi.repository import Gtk
print Gst.version()
print Gtk.get_major_version()
win = Gtk.Window()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()