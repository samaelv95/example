import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class VentanaNueva(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Actualizacion completa")
        self.set_size_request(200, 100)
        #centrar la ventana
        self.set_position(Gtk.WindowPosition.CENTER)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.label = Gtk.Label("Actualizacion completa")
        vbox.pack_start(self.label, True, True, 0)

        self.button = Gtk.Button("Cerrar")
        self.button.connect("clicked", self.on_button1_clicked)
        vbox.pack_start(self.button, True, True, 0)

    def on_button1_clicked(self, widget):
        Gtk.main_quit()
