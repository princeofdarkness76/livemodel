import Live

from devices import *
from devices.instruments import *

instrumentMap = {'Operator':Operator.Operator,'Impulse':Impulse.Impulse,'Simpler':Simpler.Simpler}

def bindInstruments():
    tracks = Live.Application.get_application().get_document().tracks
    for track in tracks:
        for device in track.devices:
