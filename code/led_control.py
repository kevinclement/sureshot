from mpf.core.custom_code import CustomCode
from os.path import exists
import time

class LEDController(CustomCode):
    def on_load(self):
        self.log.debug("led_controller.Controller code on_load")
        if exists("/sys/class/gpio/export"): 
            self.log.debug("Found gpio export, turning off LED Control")    

            self.write_file("/sys/class/gpio/export", "17")
            time.sleep(1)
            self.write_file("/sys/class/gpio/gpio17/direction", "out")
            self.write_file("/sys/class/gpio/gpio17/value", "1")
            time.sleep(.4)
            self.write_file("/sys/class/gpio/gpio17/value", "0")
            time.sleep(.4)
            self.write_file("/sys/class/gpio/unexport", "17")
        else: 
            self.log.debug("NO gpio found, ignorning LED Control")

    def write_file(self, fname, txt):
        f = open(fname, "w")
        f.write(txt)
        f.close()
    