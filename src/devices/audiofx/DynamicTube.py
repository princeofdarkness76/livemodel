from LiveModel import DeviceBase

class DynamicTube(DeviceBase):

	def __init__(self,device):
		DeviceBase.__init__(self, device)

	def getDeviceOn(self):
		return self.params[0].value

	def setDeviceOn(self,value):
		self.params[0].value = value

	deviceOn = property(getDeviceOn,setDeviceOn, doc='0 : Device On (0.0,1.0:Q)')

	def getDryWet(self):
		return self.params[1].value

	def setDryWet(self,value):
		self.params[1].value = value

	dryWet = property(getDryWet,setDryWet, doc='1 : Dry/Wet (0.0,1.0)')

	def getDrive(self):
		return self.params[2].value

	def setDrive(self,value):
		self.params[2].value = value

	drive = property(getDrive,setDrive, doc='2 : Drive (-15.0,15.0)')

	def getOutput(self):
		return self.params[3].value

	def setOutput(self,value):
		self.params[3].value = value

	output = property(getOutput,setOutput, doc='3 : Output (-15.0,15.0)')

	def getBias(self):
		return self.params[4].value

	def setBias(self,value):
		self.params[4].value = value

	bias = property(getBias,setBias, doc='4 : Bias (0.0,1.0)')

	def getEnvelope(self):
		return self.params[5].value

	def setEnvelope(self,value):
		self.params[5].value = value

	envelope = property(getEnvelope,setEnvelope, doc='5 : Envelope (-3.0,3.0)')

	def getAttack(self):
		return self.params[6].value

	def setAttack(self,value):
		self.params[6].value = value

	attack = property(getAttack,setAttack, doc='6 : Attack (0.0,1.0)')

	def getRelease(self):
		return self.params[7].value

	def setRelease(self,value):
		self.params[7].value = value

	release = property(getRelease,setRelease, doc='7 : Release (0.0,1.0)')

	def getTone(self):
		return self.params[8].value

	def setTone(self,value):
		self.params[8].value = value

	tone = property(getTone,setTone, doc='8 : Tone (-1.0,1.0)')

	def getTubeType(self):
		return self.params[9].value

	def setTubeType(self,value):
		self.params[9].value = value

	tubeType = property(getTubeType,setTubeType, doc='9 : Tube Type (0.0,2.0:Q)')

