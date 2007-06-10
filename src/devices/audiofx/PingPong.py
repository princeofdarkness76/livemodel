class PingPong:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def getDeviceOn(self):
		return self.params[0].value

	def setDeviceOn(self,value):
		self.params[0].value = value

	deviceOn = property(getDeviceOn,setDeviceOn, doc='0 : Device On (0.0,1.0:Q)')

	def getEqFreq(self):
		return self.params[1].value

	def setEqFreq(self,value):
		self.params[1].value = value

	eqFreq = property(getEqFreq,setEqFreq, doc='1 : EQ Freq (0.0,1.0)')

	def getEqWidth(self):
		return self.params[2].value

	def setEqWidth(self,value):
		self.params[2].value = value

	eqWidth = property(getEqWidth,setEqWidth, doc='2 : EQ Width (0.5,9.0)')

	def getDelayMode(self):
		return self.params[3].value

	def setDelayMode(self,value):
		self.params[3].value = value

	delayMode = property(getDelayMode,setDelayMode, doc='3 : Delay Mode (0.0,1.0:Q)')

	def getBeatDelay(self):
		return self.params[4].value

	def setBeatDelay(self,value):
		self.params[4].value = value

	beatDelay = property(getBeatDelay,setBeatDelay, doc='4 : Beat Delay (0.0,7.0:Q)')

	def getBeatSwing(self):
		return self.params[5].value

	def setBeatSwing(self,value):
		self.params[5].value = value

	beatSwing = property(getBeatSwing,setBeatSwing, doc='5 : Beat Swing (-0.333000004292,0.333000004292)')

	def getTimeDelay(self):
		return self.params[6].value

	def setTimeDelay(self,value):
		self.params[6].value = value

	timeDelay = property(getTimeDelay,setTimeDelay, doc='6 : Time Delay (1.0,200.0)')

	def getFeedback(self):
		return self.params[7].value

	def setFeedback(self,value):
		self.params[7].value = value

	feedback = property(getFeedback,setFeedback, doc='7 : Feedback (0.0,0.949999988079)')

	def getDryWet(self):
		return self.params[8].value

	def setDryWet(self,value):
		self.params[8].value = value

	dryWet = property(getDryWet,setDryWet, doc='8 : Dry/Wet (0.0,1.0)')

	def getFreeze(self):
		return self.params[9].value

	def setFreeze(self,value):
		self.params[9].value = value

	freeze = property(getFreeze,setFreeze, doc='9 : Freeze (0.0,1.0:Q)')

