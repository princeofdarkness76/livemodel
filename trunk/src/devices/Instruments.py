def test():
    s = Simpler(getTrack(0).devices[0])
    
class Device:
    def __init__(self,device):
        self.device = device
        self.params = device.parameters
        print "Init device with " + str(len(self.params))
        
class Instrument(Device):
    def __init__(self,device):
        Device.__init__(self,device)
        
class Simpler(Instrument):
    def __init__(self,device):
        if device.class_name != "OriginalSimpler":
            print "Device isnt simpler"
            return
        Instrument.__init__(self,device)
        
    def togglePower(self):
        self.device.parameters[0] = not self.device.parameters[0]
        
    def snap(self,onOff):
        self.params[1] = onOff
        
    def sampleStart(self,pos):
        self.params[2] = pos
        
    def sampleLength(self,length):
        self.params[3] = length
        
    def loop(self,onOff):
        self.params[4] = onOff
        
    def loopLength(self,length):
        self.params[5] = length
    
    def loopFade(self, length):
        self.params[6] = length
        
    def spread(self,amount):
        self.params[7] = amount
        
