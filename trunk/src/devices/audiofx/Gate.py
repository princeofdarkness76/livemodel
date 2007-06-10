from LiveModel import DeviceBase

class Gate(DeviceBase):

	def __init__(self,device):
		DeviceBase.__init__(self, device)

	def getDeviceOn(self):
		return self.params[0].value

	def setDeviceOn(self,value):
		self.params[0].value = value

	deviceOn = property(getDeviceOn,setDeviceOn, doc='0 : Device On (0.0,1.0:Q)')

	def getThreshold(self):
		return self.params[1].value

	def setThreshold(self,value):
		self.params[1].value = value

	threshold = property(getThreshold,setThreshold, doc='1 : Threshold (0.0,1.0)')

	def getAttack(self):
		return self.params[2].value

	def setAttack(self,value):
		self.params[2].value = value

	attack = property(getAttack,setAttack, doc='2 : Attack (0.0,1.0)')

	def getHold(self):
		return self.params[3].value

	def setHold(self,value):
		self.params[3].value = value

	hold = property(getHold,setHold, doc='3 : Hold (0.0,1.0)')

	def getRelease(self):
		return self.params[4].value

	def setRelease(self,value):
		self.params[4].value = value

	release = property(getRelease,setRelease, doc='4 : Release (0.0,1.0)')

	def getFloor(self):
		return self.params[5].value

	def setFloor(self,value):
		self.params[5].value = value

	floor = property(getFloor,setFloor, doc='5 : Floor (-75.0,0.0)')

