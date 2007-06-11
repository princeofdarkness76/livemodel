from LiveModel import *
from devices.instruments.Operator import Operator

class TestDev:
    def __init__(self):
        self.parameters = []

def offlineTest():        
    device = TestDev() 
    op = Operator(device)

def onlineTest():
    op = Operator(getTrack(0).devices[0])
    return op

