class Simpler(Instrument):
    def __init__(self,device):
        if device.class_name != "Simpler":
            print "Device isnt simpler"
            return
        
        self.device = device
        
    def togglePower(self):
        self.device.parameters[0] = not self.device.parameters[0]
        