import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Update")

        self.label = Gtk.Label(label="Hello World", angle=25, halign=Gtk.Align.END)

        self.button = Gtk.Box()
        print(dir(self.button.props))

        """self.button = Gtk.Button(label="Click Here")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)"""
        #self.button.disconnect_by_func(self.on_button_clicked)

        #boton para cerrar la ventana
        """self.button2 = Gtk.Button(label="Click Here To Close")
        self.button2.connect("clicked", Gtk.main_quit)
        self.add(self.button2)"""

    def on_button_clicked(self, widget):
        print("Hello World")
        self.button.disconnect_by_func(self.on_button_clicked)

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()