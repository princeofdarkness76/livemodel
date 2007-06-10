class GrainDelay:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def getDeviceOn(self):
		return self.params[0].value

	def setDeviceOn(self,value):
		self.params[0].value = value

	deviceOn = property(getDeviceOn,setDeviceOn, doc='0 : Device On (0.0,1.0:Q)')

	def getSpray(self):
		return self.params[1].value

	def setSpray(self,value):
		self.params[1].value = value

	spray = property(getSpray,setSpray, doc='1 : Spray (0.0,1.0)')

	def getFrequency(self):
		return self.params[2].value

	def setFrequency(self,value):
		self.params[2].value = value

	frequency = property(getFrequency,setFrequency, doc='2 : Frequency (0.0,1.0)')

	def getPitch(self):
		return self.params[3].value

	def setPitch(self,value):
		self.params[3].value = value

	pitch = property(getPitch,setPitch, doc='3 : Pitch (-36.0,12.0)')

	def getRandom(self):
		return self.params[4].value

	def setRandom(self,value):
		self.params[4].value = value

	random = property(getRandom,setRandom, doc='4 : Random (0.0,1.0)')

	def getFeedback(self):
		return self.params[5].value

	def setFeedback(self,value):
		self.params[5].value = value

	feedback = property(getFeedback,setFeedback, doc='5 : Feedback (0.0,0.949999988079)')

	def getDrywet(self):
		return self.params[6].value

	def setDrywet(self,value):
		self.params[6].value = value

	drywet = property(getDrywet,setDrywet, doc='6 : DryWet (0.0,1.0)')

	def getDelayMode(self):
		return self.params[7].value

	def setDelayMode(self,value):
		self.params[7].value = value

	delayMode = property(getDelayMode,setDelayMode, doc='7 : Delay Mode (0.0,1.0:Q)')

	def getBeatDelay(self):
		return self.params[8].value

	def setBeatDelay(self,value):
		self.params[8].value = value

	beatDelay = property(getBeatDelay,setBeatDelay, doc='8 : Beat Delay (0.0,7.0:Q)')

	def getBeatSwing(self):
		return self.params[9].value

	def setBeatSwing(self,value):
		self.params[9].value = value

	beatSwing = property(getBeatSwing,setBeatSwing, doc='9 : Beat Swing (-0.333000004292,0.333000004292)')

	def getTimeDelay(self):
		return self.params[10].value

	def setTimeDelay(self,value):
		self.params[10].value = value

	timeDelay = property(getTimeDelay,setTimeDelay, doc='10 : Time Delay (1.0,128.0)')

