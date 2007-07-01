import LiveModel
import LiveUtils

class DeviceManager:
    
    def __init__(self, liveFlash):
        self.devices = []
        self._liveFlash = liveFlash
    
    def createDevice(self,trackID,deviceID):
        self._liveFlash.show_message("Create device " + str(trackID) + " : " + str(deviceID));
        return LiveModel.DeviceBase(LiveUtils.getTrack(trackID).devices[deviceID])
        
    def addDevice(self,device,uid = None):
        """
        Add a new device, optionally specifying the UID. Note, extra space isnt created automatically.
        the supplied UID must be within the existing range to take effect or a new one will be created
        TODO : use a dictionary instead?
        """
        if(uid != None and len(self.devices) > uid):
            self.devices[uid] = device
        else:
            self.devices.append(device)
            uid = len(self.devices) - 1

        self._liveFlash.show_message("Add device " + str(uid));
        return uid
    
    def removeDevice(self,id):
        self.devices[id] = []
        
    def getDevice(self, id):
        return self.devices[id]
    