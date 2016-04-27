import requests
from VentanaNueva import VentanaNueva
import comparar
import gi
import sys
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject

class Actualizacion(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Actualizacion")
        self.set_border_width(10)
        self.set_size_request(400, 100)
        #Centrar la ventana
        self.set_position(Gtk.WindowPosition.CENTER)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.progressbar = Gtk.ProgressBar()
        vbox.pack_start(self.progressbar, True, True, 0)

        button = Gtk.Button("Actualizar")
        button.connect("clicked", self.read)
        vbox.pack_start(button, True, True, 0)

    """Funcion que descarga el archivo de internet"""
    def read(self, button):
        res = requests.get("http://www.colmex.mx/pdf/historiaminima.pdf", stream=True)
        with open("actualizaciones/pdf.pdf", "wb") as f:
            total_length = res.headers.get('content-length')
            if total_length is None:
                f.write(res.content)

            else:
                dl = 0
                total_length = int(total_length)
                for data in res.iter_content(chunk_size=1024):
                    dl += len(data)
                    f.write(data)
                    done = float(100 * dl / total_length)
                    self.update_pogress(done)
                    while Gtk.events_pending():
        				Gtk.main_iteration()
                    sys.stdout.flush()
   
        
        self.window = VentanaNueva()
        self.window.connect("delete-event", Gtk.main_quit)
        self.window.show_all()

        

    def update_pogress(self, porcentaje):
    	#print (porcentaje/100)
    	self.progressbar.set_fraction(porcentaje / 100)


win = Actualizacion()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()