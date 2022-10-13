from mpf.core.mode import Mode
from os.path import exists
import time

class Trigger_Pi(Mode):

    def write_file(self, fname, txt):
        f = open(fname, "w")
        f.write(txt)
        f.close()

    def mode_start(self, **kwargs):
        self.log.debug("Trigger_Pi mode start")

        if exists("/sys/class/gpio/export"): 
            self.log.debug("Found gpio export, turning off LED Control")
            
            self.write_file("/sys/class/gpio/export", "17")
            self.write_file("/sys/class/gpio/gpio17/direction", "out")
            self.write_file("/sys/class/gpio/gpio17/value", "1")
            time.sleep(.4)
            self.write_file("/sys/class/gpio/gpio17/value", "0")
            self.write_file("/sys/class/gpio/unexport", "17")
        else: 
            self.log.debug("NO gpio found, ignorning LED Control")
        
        self.stop()
    