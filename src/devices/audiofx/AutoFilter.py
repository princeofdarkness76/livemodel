class AutoFilter:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def getDeviceOn(self):
		return self.params[0].value

	def setDeviceOn(self,value):
		self.params[0].value = value

	deviceOn = property(getDeviceOn,setDeviceOn, doc='0 : Device On (0.0,1.0:Q)')

	def getFilterType(self):
		return self.params[1].value

	def setFilterType(self,value):
		self.params[1].value = value

	filterType = property(getFilterType,setFilterType, doc='1 : Filter Type (0.0,3.0:Q)')

	def getFrequency(self):
		return self.params[2].value

	def setFrequency(self,value):
		self.params[2].value = value

	frequency = property(getFrequency,setFrequency, doc='2 : Frequency (20.0,135.0)')

	def getResonance(self):
		return self.params[3].value

	def setResonance(self,value):
		self.params[3].value = value

	resonance = property(getResonance,setResonance, doc='3 : Resonance (0.20000000298,3.0)')

	def getEnvModulation(self):
		return self.params[4].value

	def setEnvModulation(self,value):
		self.params[4].value = value

	envModulation = property(getEnvModulation,setEnvModulation, doc='4 : Env. Modulation (0.0,127.0)')

	def getEnvAttack(self):
		return self.params[5].value

	def setEnvAttack(self,value):
		self.params[5].value = value

	envAttack = property(getEnvAttack,setEnvAttack, doc='5 : Env. Attack (0.10000000149,30.0)')

	def getEnvRelease(self):
		return self.params[6].value

	def setEnvRelease(self,value):
		self.params[6].value = value

	envRelease = property(getEnvRelease,setEnvRelease, doc='6 : Env. Release (0.10000000149,400.0)')

	def getLfoAmount(self):
		return self.params[7].value

	def setLfoAmount(self,value):
		self.params[7].value = value

	lfoAmount = property(getLfoAmount,setLfoAmount, doc='7 : LFO Amount (0.0,30.0)')

	def getLfoWaveform(self):
		return self.params[8].value

	def setLfoWaveform(self,value):
		self.params[8].value = value

	lfoWaveform = property(getLfoWaveform,setLfoWaveform, doc='8 : LFO Waveform (0.0,6.0:Q)')

	def getLfoFrequency(self):
		return self.params[9].value

	def setLfoFrequency(self,value):
		self.params[9].value = value

	lfoFrequency = property(getLfoFrequency,setLfoFrequency, doc='9 : LFO Frequency (0.0,1.0)')

	def getLfoSync(self):
		return self.params[10].value

	def setLfoSync(self,value):
		self.params[10].value = value

	lfoSync = property(getLfoSync,setLfoSync, doc='10 : LFO Sync (0.0,1.0:Q)')

	def getLfoSyncRate(self):
		return self.params[11].value

	def setLfoSyncRate(self,value):
		self.params[11].value = value

	lfoSyncRate = property(getLfoSyncRate,setLfoSyncRate, doc='11 : LFO Sync Rate (0.0,21.0)')

	def getLfoStereoMode(self):
		return self.params[12].value

	def setLfoStereoMode(self,value):
		self.params[12].value = value

	lfoStereoMode = property(getLfoStereoMode,setLfoStereoMode, doc='12 : LFO Stereo Mode (0.0,1.0:Q)')

	def getLfoSpin(self):
		return self.params[13].value

	def setLfoSpin(self,value):
		self.params[13].value = value

	lfoSpin = property(getLfoSpin,setLfoSpin, doc='13 : LFO Spin (0.0,0.5)')

	def getLfoPhase(self):
		return self.params[14].value

	def setLfoPhase(self,value):
		self.params[14].value = value

	lfoPhase = property(getLfoPhase,setLfoPhase, doc='14 : LFO Phase (0.0,360.0)')

	def getLfoOffset(self):
		return self.params[15].value

	def setLfoOffset(self,value):
		self.params[15].value = value

	lfoOffset = property(getLfoOffset,setLfoOffset, doc='15 : LFO Offset (0.0,360.0)')

	def getLfoQuantizeOn(self):
		return self.params[16].value

	def setLfoQuantizeOn(self,value):
		self.params[16].value = value

	lfoQuantizeOn = property(getLfoQuantizeOn,setLfoQuantizeOn, doc='16 : LFO Quantize On (0.0,1.0:Q)')

	def getLfoQuantizeRate(self):
		return self.params[17].value

	def setLfoQuantizeRate(self,value):
		self.params[17].value = value

	lfoQuantizeRate = property(getLfoQuantizeRate,setLfoQuantizeRate, doc='17 : LFO Quantize Rate (0.0,9.0:Q)')

