class CompressorII:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def getDeviceOn(self):
		return self.params[0].value

	def setDeviceOn(self,value):
		self.params[0].value = value

	deviceOn = property(getDeviceOn,setDeviceOn, doc='0 : Device On (0.0,1.0:Q)')

	def getThreshold(self):
		return self.params[1].value

	def setThreshold(self,value):
		self.params[1].value = value

	threshold = property(getThreshold,setThreshold, doc='1 : Threshold (-30.0,6.0)')

	def getRatio(self):
		return self.params[2].value

	def setRatio(self,value):
		self.params[2].value = value

	ratio = property(getRatio,setRatio, doc='2 : Ratio (0.0,1.0)')

	def getAttack(self):
		return self.params[3].value

	def setAttack(self,value):
		self.params[3].value = value

	attack = property(getAttack,setAttack, doc='3 : Attack (0.0,1.0)')

	def getRelease(self):
		return self.params[4].value

	def setRelease(self,value):
		self.params[4].value = value

	release = property(getRelease,setRelease, doc='4 : Release (0.0,1.0)')

	def getOutputGain(self):
		return self.params[5].value

	def setOutputGain(self,value):
		self.params[5].value = value

	outputGain = property(getOutputGain,setOutputGain, doc='5 : Output Gain (-18.0,18.0)')

	def getFreq(self):
		return self.params[6].value

	def setFreq(self,value):
		self.params[6].value = value

	freq = property(getFreq,setFreq, doc='6 : Freq (0.0,1.0)')

	def getSidegain(self):
		return self.params[7].value

	def setSidegain(self,value):
		self.params[7].value = value

	sidegain = property(getSidegain,setSidegain, doc='7 : SideGain (-15.0,15.0)')

	def getSideon(self):
		return self.params[8].value

	def setSideon(self,value):
		self.params[8].value = value

	sideon = property(getSideon,setSideon, doc='8 : SideOn (0.0,1.0:Q)')

	def getPeakon(self):
		return self.params[9].value

	def setPeakon(self,value):
		self.params[9].value = value

	peakon = property(getPeakon,setPeakon, doc='9 : PeakOn (0.0,1.0:Q)')

	def getLookahead(self):
		return self.params[10].value

	def setLookahead(self,value):
		self.params[10].value = value

	lookahead = property(getLookahead,setLookahead, doc='10 : LookAhead (0.0,2.0:Q)')

	def getSidemode(self):
		return self.params[11].value

	def setSidemode(self,value):
		self.params[11].value = value

	sidemode = property(getSidemode,setSidemode, doc='11 : SideMode (0.0,2.0:Q)')

