from LiveModel import DeviceBase

class Velocity(DeviceBase):

	def __init__(self,device):
		DeviceBase.__init__(self, device)

	def getDeviceOn(self):
		return self.params[0].value

	def setDeviceOn(self,value):
		self.params[0].value = value

	deviceOn = property(getDeviceOn,setDeviceOn, doc='0 : Device On (0.0,1.0:Q)')

	def getDrive(self):
		return self.params[1].value

	def setDrive(self,value):
		self.params[1].value = value

	drive = property(getDrive,setDrive, doc='1 : Drive (-1.0,1.0)')

	def getCompand(self):
		return self.params[2].value

	def setCompand(self,value):
		self.params[2].value = value

	compand = property(getCompand,setCompand, doc='2 : Compand (-1.0,1.0)')

	def getRandom(self):
		return self.params[3].value

	def setRandom(self,value):
		self.params[3].value = value

	random = property(getRandom,setRandom, doc='3 : Random (0.0,64.0)')

	def getMode(self):
		return self.params[4].value

	def setMode(self,value):
		self.params[4].value = value

	mode = property(getMode,setMode, doc='4 : Mode (0.0,2.0:Q)')

	def getOperation(self):
		return self.params[5].value

	def setOperation(self,value):
		self.params[5].value = value

	operation = property(getOperation,setOperation, doc='5 : Operation (0.0,2.0:Q)')

	def getOutHi(self):
		return self.params[6].value

	def setOutHi(self,value):
		self.params[6].value = value

	outHi = property(getOutHi,setOutHi, doc='6 : Out Hi (0.0,127.0)')

	def getOutLow(self):
		return self.params[7].value

	def setOutLow(self,value):
		self.params[7].value = value

	outLow = property(getOutLow,setOutLow, doc='7 : Out Low (0.0,127.0)')

	def getRange(self):
		return self.params[8].value

	def setRange(self,value):
		self.params[8].value = value

	range = property(getRange,setRange, doc='8 : Range (0.0,127.0)')

	def getLowest(self):
		return self.params[9].value

	def setLowest(self,value):
		self.params[9].value = value

	lowest = property(getLowest,setLowest, doc='9 : Lowest (0.0,127.0)')

