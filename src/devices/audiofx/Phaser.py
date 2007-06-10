class Phaser:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

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

	def getType(self):
		return self.params[2].value

	def setType(self,value):
		self.params[2].value = value

	type = property(getType,setType, doc='2 : Type (0.0,1.0:Q)')

	def getPoles(self):
		return self.params[3].value

	def setPoles(self,value):
		self.params[3].value = value

	poles = property(getPoles,setPoles, doc='3 : Poles (1.0,8.0)')

	def getColor(self):
		return self.params[4].value

	def setColor(self,value):
		self.params[4].value = value

	color = property(getColor,setColor, doc='4 : Color (0.0,1.0)')

	def getFrequency(self):
		return self.params[5].value

	def setFrequency(self,value):
		self.params[5].value = value

	frequency = property(getFrequency,setFrequency, doc='5 : Frequency (0.0,1.0)')

	def getFeedback(self):
		return self.params[6].value

	def setFeedback(self,value):
		self.params[6].value = value

	feedback = property(getFeedback,setFeedback, doc='6 : Feedback (0.0,1.0)')

	def getLfoAmount(self):
		return self.params[7].value

	def setLfoAmount(self,value):
		self.params[7].value = value

	lfoAmount = property(getLfoAmount,setLfoAmount, doc='7 : LFO Amount (0.0,1.0)')

	def getEnvModulation(self):
		return self.params[8].value

	def setEnvModulation(self,value):
		self.params[8].value = value

	envModulation = property(getEnvModulation,setEnvModulation, doc='8 : Env. Modulation (-1.0,1.0)')

	def getEnvAttack(self):
		return self.params[9].value

	def setEnvAttack(self,value):
		self.params[9].value = value

	envAttack = property(getEnvAttack,setEnvAttack, doc='9 : Env. Attack (0.10000000149,30.0)')

	def getEnvRelease(self):
		return self.params[10].value

	def setEnvRelease(self,value):
		self.params[10].value = value

	envRelease = property(getEnvRelease,setEnvRelease, doc='10 : Env. Release (0.10000000149,400.0)')

	def getLfoWaveform(self):
		return self.params[11].value

	def setLfoWaveform(self,value):
		self.params[11].value = value

	lfoWaveform = property(getLfoWaveform,setLfoWaveform, doc='11 : LFO Waveform (0.0,5.0:Q)')

	def getLfoFrequency(self):
		return self.params[12].value

	def setLfoFrequency(self,value):
		self.params[12].value = value

	lfoFrequency = property(getLfoFrequency,setLfoFrequency, doc='12 : LFO Frequency (0.0,1.0)')

	def getSync(self):
		return self.params[13].value

	def setSync(self,value):
		self.params[13].value = value

	sync = property(getSync,setSync, doc='13 : Sync (0.0,1.0:Q)')

	def getSyncRate(self):
		return self.params[14].value

	def setSyncRate(self,value):
		self.params[14].value = value

	syncRate = property(getSyncRate,setSyncRate, doc='14 : Sync Rate (0.0,21.0)')

	def getLfoStereoMode(self):
		return self.params[15].value

	def setLfoStereoMode(self,value):
		self.params[15].value = value

	lfoStereoMode = property(getLfoStereoMode,setLfoStereoMode, doc='15 : LFO Stereo Mode (0.0,1.0:Q)')

	def getLfoSpin(self):
		return self.params[16].value

	def setLfoSpin(self,value):
		self.params[16].value = value

	lfoSpin = property(getLfoSpin,setLfoSpin, doc='16 : LFO Spin (0.0,0.5)')

	def getLfoPhase(self):
		return self.params[17].value

	def setLfoPhase(self,value):
		self.params[17].value = value

	lfoPhase = property(getLfoPhase,setLfoPhase, doc='17 : LFO Phase (0.0,360.0)')

	def getLfoOffset(self):
		return self.params[18].value

	def setLfoOffset(self,value):
		self.params[18].value = value

	lfoOffset = property(getLfoOffset,setLfoOffset, doc='18 : LFO Offset (0.0,360.0)')

	def getLfoWidthRandom(self):
		return self.params[19].value

	def setLfoWidthRandom(self,value):
		self.params[19].value = value

	lfoWidthRandom = property(getLfoWidthRandom,setLfoWidthRandom, doc='19 : LFO Width (Random) (0.0,1.0)')

