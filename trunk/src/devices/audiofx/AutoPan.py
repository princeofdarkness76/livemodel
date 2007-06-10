class AutoPan:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def getDeviceOn(self):
		return self.params[0].value

	def setDeviceOn(self,value):
		self.params[0].value = value

	deviceOn = property(getDeviceOn,setDeviceOn, doc='0 : Device On (0.0,1.0:Q)')

	def getLfoType(self):
		return self.params[1].value

	def setLfoType(self,value):
		self.params[1].value = value

	lfoType = property(getLfoType,setLfoType, doc='1 : LFO Type (0.0,1.0:Q)')

	def getAmount(self):
		return self.params[2].value

	def setAmount(self,value):
		self.params[2].value = value

	amount = property(getAmount,setAmount, doc='2 : Amount (0.0,1.0)')

	def getFrequency(self):
		return self.params[3].value

	def setFrequency(self,value):
		self.params[3].value = value

	frequency = property(getFrequency,setFrequency, doc='3 : Frequency (0.0,1.0)')

	def getSyncRate(self):
		return self.params[4].value

	def setSyncRate(self,value):
		self.params[4].value = value

	syncRate = property(getSyncRate,setSyncRate, doc='4 : Sync Rate (0.0,21.0)')

	def getPhase(self):
		return self.params[5].value

	def setPhase(self,value):
		self.params[5].value = value

	phase = property(getPhase,setPhase, doc='5 : Phase (0.0,360.0)')

	def getSpin(self):
		return self.params[6].value

	def setSpin(self,value):
		self.params[6].value = value

	spin = property(getSpin,setSpin, doc='6 : Spin (0.0,0.5)')

	def getStereoMode(self):
		return self.params[7].value

	def setStereoMode(self,value):
		self.params[7].value = value

	stereoMode = property(getStereoMode,setStereoMode, doc='7 : Stereo Mode (0.0,1.0:Q)')

	def getOffset(self):
		return self.params[8].value

	def setOffset(self,value):
		self.params[8].value = value

	offset = property(getOffset,setOffset, doc='8 : Offset (0.0,360.0)')

	def getWaveform(self):
		return self.params[9].value

	def setWaveform(self,value):
		self.params[9].value = value

	waveform = property(getWaveform,setWaveform, doc='9 : Waveform (0.0,3.0:Q)')

	def getShape(self):
		return self.params[10].value

	def setShape(self,value):
		self.params[10].value = value

	shape = property(getShape,setShape, doc='10 : Shape (0.0,1.0)')

	def getWidthRandom(self):
		return self.params[11].value

	def setWidthRandom(self,value):
		self.params[11].value = value

	widthRandom = property(getWidthRandom,setWidthRandom, doc='11 : Width (Random) (0.0,1.0)')

	def getInvert(self):
		return self.params[12].value

	def setInvert(self,value):
		self.params[12].value = value

	invert = property(getInvert,setInvert, doc='12 : Invert (0.0,1.0:Q)')

