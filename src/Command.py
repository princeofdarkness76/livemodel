# LiveModel, a device model for controlling Ableton Live
# Copyright (C) 2007 Martin Wood-Mitrovski (martin@relivethefuture.com)
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# For questions regarding this module contact
# Martin Wood-Mitrovski 
# martin@relivethefuture.com

import Live
from LiveUtils import *
import DeviceManager

class FlashCommands:
    
    def __init__(self, deviceManager):
        self.Live = Live.Application.get_application().get_document()
        self.callbackManager = CallbackManager()
        
        # General Commands
        self.callbackManager.add(self.numTracks, "nt")
        self.callbackManager.add(self.numDevicesOnTrack, "ntd")
        self.callbackManager.add(self.getDeviceInfo, "gdi")
        self.callbackManager.add(self.bindDevice, "bind")
        
        # Device Commands
        self.callbackManager.add(self.storePatch,"store")
        self.callbackManager.add(self.loadPatch,"load")   
        self.callbackManager.add(self.interp,"interp")
        self.callbackManager.add(self.blerp,"blerp")
        self.callbackManager.add(self.randomize,"rnd")
        
        self.deviceManager = deviceManager
        
    def handleCommand(self,command):
        parts = command.split(" ")
        res = self.callbackManager.dispatch(parts)
        if res == -1:
            return "Command not found"
        elif res == -2:
            return "Error in command"
        else:
            return res

    def numTracks(self,cmd):
        return len(getTracks())
    
    def numDevicesOnTrack(self,cmd):
        if(len(cmd) != 2):
            return "numDevicesOnTrack requires 1 argument : trackID"
        
        trackNum = int(cmd[1])
        return len(getTrack(trackNum).devices)
    
    def getDeviceInfo(self,cmd):
        if(len(cmd) != 3):
            return "getDeviceInfo requires 2 arguments : trackID deviceID"

        trackNum = int(cmd[1])
        deviceNum = int(cmd[2])
        if(trackNum < len(getTracks())):
            dev = getTrack(trackNum).devices[deviceNum]
            return "Device (" + dev.class_name + ") " + dev.name + " with " + str(len(dev.parameters)) + " params"
        else:
            return "trackID out of range"    
        
    def bindDevice(self,cmd):
        if(len(cmd) < 3):
            return "Bind requires 2 or 3 arguments : trackID deviceID [UID]"
        
        trackNum = int(cmd[1])
        deviceNum = int(cmd[2])
        
        dev = self.deviceManager.createDevice(trackNum,deviceNum)
        
        if(len(cmd) == 4):
            return "UID " + str(self.deviceManager.addDevice(dev,int(cmd[3]))) 
        else:
            return "UID " + str(self.deviceManager.addDevice(dev))
        
    
    def storePatch(self,cmd):
        if(len(cmd) != 3):
            return "Store requires 2 arguments : deviceUID patchIndex"
        
        deviceID = int(cmd[1])
        patchID = int(cmd[2])
        device = self.deviceManager.getDevice(deviceID)
        device.storePatch(patchID)
        return "Stored " + cmd[2]
        
    def loadPatch(self,cmd):
        if(len(cmd) != 3):
            return "Load requires 2 arguments : deviceUID patchIndex"
        
        deviceID = int(cmd[1])
        patchID = int(cmd[2])
        device = self.deviceManager.getDevice(deviceID)
        device.loadPatch(patchID)
        return "Loaded " + cmd[2]
        
    def randomize(self,cmd):
        if(len(cmd) != 2):
            return "Randomize requires 1 argument : deviceUID"
        
        deviceID = int(cmd[1])
        device = self.deviceManager.getDevice(deviceID)
        device.randomize()
        return "Randomized " + cmd[1]
        
    def interp(self,cmd):
        if(len(cmd) != 5):
            return "Interp requires 4 arguments : deviceUID patchA patchB amount"
        
        deviceID = int(cmd[1])
        patchA = int(cmd[2])
        patchB = int(cmd[3])
        amount = float(cmd[4])
        device = self.deviceManager.getDevice(deviceID)
        device.interp(patchA,patchB,amount)
        return "Interp " + cmd[2] + " -> " + cmd[3] + " by " + cmd[4]

    def blerp(self,cmd):
        if(len(cmd) != 8):
            return "Blerp requires 7 arguments : deviceUID patchA patchB patchC patchD x y"
        
        deviceID = int(cmd[1])
        patchA = int(cmd[2])
        patchB = int(cmd[3])
        patchC = int(cmd[4])
        patchD = int(cmd[5])
        x = float(cmd[6])
        y = float(cmd[7])
        device = self.deviceManager.getDevice(deviceID)
        device.bilinearInterp(patchA,patchB,patchC,patchD,x,y)
        return "Blerp " + cmd[2] + "," + cmd[3] + "," + cmd[4] + "," + cmd[5] + " by " + cmd[6] + "," + cmd[7]
    
class CallbackManager:

    def __init__(self):
        self.callbacks = {}

    def dispatch(self, message):
        try:
            address = message[0]
            return self.callbacks[address](message)
        except KeyError, e:
            print "key not found"
            return -1
            # address not found
            pass
        except None, e:
            print "Exception in", address, "callback :", e
            return -2
        
        return 0

    def add(self, callback, name):
        """Adds a callback to our set of callbacks,
        or removes the callback with name if callback
        is None."""
        if callback == None:
            del self.callbacks[name]
        else:
            self.callbacks[name] = callback
