import os
import sys
import requests
import subprocess
import wget
import threading
from threading import Thread
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject

class ProgressBarWindow(Gtk.Window):

    done = 0.0

    def __init__(self):
        Gtk.Window.__init__(self, title="Update")
        self.set_border_width(10)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.progressbar = Gtk.ProgressBar()
        vbox.pack_start(self.progressbar, True, True, 0)

        button = Gtk.Button("update")
        button.connect("clicked", self.on_show_text_toggled)
        vbox.pack_start(button, True, True, 0)

    def on_show_text_toggled(self, button):
        self.read()
        

    def on_timeout(self, data):
        """
        Update value on the progress bar
        """
        new_value = self.progressbar.get_fraction() + 0.01

        if new_value > 1:
            return False

        self.progressbar.set_fraction(new_value)
        return True

    #def download(self):
        #p = os.popen("wget -N -P /home/systmatic2/Desktop/examples/actualizaciones/ http://www.colmex.mx/pdf/historiaminima.pdf")

    def read(self):
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
                    print (float(done / 100)) #aqui mandamos a actualizar la barra de progreso    
                    Thread(target = self.progressbar.set_fraction(done / 100)).start()
                    sys.stdout.flush()
        return "pdf.pdf"


win = ProgressBarWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()