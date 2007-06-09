import devices.instruments.Operator

class TestDev:
    def __init__(self):
        self.parameters = []
        self.x = 23
        
    def test(self,value=None):
        if value != None:
            self.x = value
        return self.x
            
            
device = TestDev() 

print(device.test())

print(device.test(43))


