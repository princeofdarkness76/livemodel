from LiveModel import DeviceBase

class Pitch(DeviceBase):

	def __init__(self,device):
		DeviceBase.__init__(self, device)

	def getDeviceOn(self):
		return self.params[0].value

	def setDeviceOn(self,value):
		self.params[0].value = value

	deviceOn = property(getDeviceOn,setDeviceOn, doc='0 : Device On (0.0,1.0:Q)')

	def getPitch(self):
		return self.params[1].value

	def setPitch(self,value):
		self.params[1].value = value

	pitch = property(getPitch,setPitch, doc='1 : Pitch (-48.0,48.0)')

	def getLowest(self):
		return self.params[2].value

	def setLowest(self,value):
		self.params[2].value = value

	lowest = property(getLowest,setLowest, doc='2 : Lowest (0.0,127.0)')

	def getRange(self):
		return self.params[3].value

	def setRange(self,value):
		self.params[3].value = value

	range = property(getRange,setRange, doc='3 : Range (0.0,127.0)')

