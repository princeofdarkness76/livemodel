class SimpleDelay:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def getDeviceOn(self):
		return self.params[0].value

	def setDeviceOn(self,value):
		self.params[0].value = value

	deviceOn = property(getDeviceOn,setDeviceOn, doc='0 : Device On (0.0,1.0:Q)')

	def getLinkOn(self):
		return self.params[1].value

	def setLinkOn(self,value):
		self.params[1].value = value

	linkOn = property(getLinkOn,setLinkOn, doc='1 : Link On (0.0,1.0:Q)')

	def getLDelayMode(self):
		return self.params[2].value

	def setLDelayMode(self,value):
		self.params[2].value = value

	lDelayMode = property(getLDelayMode,setLDelayMode, doc='2 : L Delay Mode (0.0,1.0:Q)')

	def getLBeatDelay(self):
		return self.params[3].value

	def setLBeatDelay(self,value):
		self.params[3].value = value

	lBeatDelay = property(getLBeatDelay,setLBeatDelay, doc='3 : L Beat Delay (0.0,7.0:Q)')

	def getLBeatSwing(self):
		return self.params[4].value

	def setLBeatSwing(self,value):
		self.params[4].value = value

	lBeatSwing = property(getLBeatSwing,setLBeatSwing, doc='4 : L Beat Swing (-0.333000004292,0.333000004292)')

	def getLTimeDelay(self):
		return self.params[5].value

	def setLTimeDelay(self,value):
		self.params[5].value = value

	lTimeDelay = property(getLTimeDelay,setLTimeDelay, doc='5 : L Time Delay (1.0,300.0)')

	def getRDelayMode(self):
		return self.params[6].value

	def setRDelayMode(self,value):
		self.params[6].value = value

	rDelayMode = property(getRDelayMode,setRDelayMode, doc='6 : R Delay Mode (0.0,1.0:Q)')

	def getRBeatDelay(self):
		return self.params[7].value

	def setRBeatDelay(self,value):
		self.params[7].value = value

	rBeatDelay = property(getRBeatDelay,setRBeatDelay, doc='7 : R Beat Delay (0.0,7.0:Q)')

	def getRBeatSwing(self):
		return self.params[8].value

	def setRBeatSwing(self,value):
		self.params[8].value = value

	rBeatSwing = property(getRBeatSwing,setRBeatSwing, doc='8 : R Beat Swing (-0.333000004292,0.333000004292)')

	def getRTimeDelay(self):
		return self.params[9].value

	def setRTimeDelay(self,value):
		self.params[9].value = value

	rTimeDelay = property(getRTimeDelay,setRTimeDelay, doc='9 : R Time Delay (1.0,300.0)')

	def getFeedback(self):
		return self.params[10].value

	def setFeedback(self,value):
		self.params[10].value = value

	feedback = property(getFeedback,setFeedback, doc='10 : Feedback (0.0,0.949999988079)')

	def getDryWet(self):
		return self.params[11].value

	def setDryWet(self,value):
		self.params[11].value = value

	dryWet = property(getDryWet,setDryWet, doc='11 : Dry/Wet (0.0,1.0)')

