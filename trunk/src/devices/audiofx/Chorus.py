from LiveModel import DeviceBase

class Chorus(DeviceBase):

	def __init__(self,device):
		DeviceBase.__init__(self, device)

	def getDeviceOn(self):
		return self.params[0].value

	def setDeviceOn(self,value):
		self.params[0].value = value

	deviceOn = property(getDeviceOn,setDeviceOn, doc='0 : Device On (0.0,1.0:Q)')

	def getDelay1Time(self):
		return self.params[1].value

	def setDelay1Time(self,value):
		self.params[1].value = value

	delay1Time = property(getDelay1Time,setDelay1Time, doc='1 : Delay 1 Time (0.0,1.0)')

	def getDelay1Hipass(self):
		return self.params[2].value

	def setDelay1Hipass(self,value):
		self.params[2].value = value

	delay1Hipass = property(getDelay1Hipass,setDelay1Hipass, doc='2 : Delay 1 HiPass (0.0,1.0)')

	def getDelay2Time(self):
		return self.params[3].value

	def setDelay2Time(self,value):
		self.params[3].value = value

	delay2Time = property(getDelay2Time,setDelay2Time, doc='3 : Delay 2 Time (0.0,1.0)')

	def getDelay2Mode(self):
		return self.params[4].value

	def setDelay2Mode(self,value):
		self.params[4].value = value

	delay2Mode = property(getDelay2Mode,setDelay2Mode, doc='4 : Delay 2 Mode (0.0,2.0:Q)')

	def getLinkOn(self):
		return self.params[5].value

	def setLinkOn(self,value):
		self.params[5].value = value

	linkOn = property(getLinkOn,setLinkOn, doc='5 : Link On (0.0,1.0:Q)')

	def getLfoAmount(self):
		return self.params[6].value

	def setLfoAmount(self,value):
		self.params[6].value = value

	lfoAmount = property(getLfoAmount,setLfoAmount, doc='6 : LFO Amount (0.0,1.0)')

	def getLfoRate(self):
		return self.params[7].value

	def setLfoRate(self,value):
		self.params[7].value = value

	lfoRate = property(getLfoRate,setLfoRate, doc='7 : LFO Rate (0.0,1.0)')

	def getLfoExtendOn(self):
		return self.params[8].value

	def setLfoExtendOn(self,value):
		self.params[8].value = value

	lfoExtendOn = property(getLfoExtendOn,setLfoExtendOn, doc='8 : LFO Extend On (0.0,1.0:Q)')

	def getFeedback(self):
		return self.params[9].value

	def setFeedback(self,value):
		self.params[9].value = value

	feedback = property(getFeedback,setFeedback, doc='9 : Feedback (0.0,0.949999988079)')

	def getPolarity(self):
		return self.params[10].value

	def setPolarity(self,value):
		self.params[10].value = value

	polarity = property(getPolarity,setPolarity, doc='10 : Polarity (0.0,1.0:Q)')

	def getDryWet(self):
		return self.params[11].value

	def setDryWet(self,value):
		self.params[11].value = value

	dryWet = property(getDryWet,setDryWet, doc='11 : Dry/Wet (0.0,1.0)')

