class VinylDistortion:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def getDeviceOn(self):
		return self.params[0].value

	def setDeviceOn(self,value):
		self.params[0].value = value

	deviceOn = property(getDeviceOn,setDeviceOn, doc='0 : Device On (0.0,1.0:Q)')

	def getTracingOn(self):
		return self.params[1].value

	def setTracingOn(self,value):
		self.params[1].value = value

	tracingOn = property(getTracingOn,setTracingOn, doc='1 : Tracing On (0.0,1.0:Q)')

	def getTracingDrive(self):
		return self.params[2].value

	def setTracingDrive(self,value):
		self.params[2].value = value

	tracingDrive = property(getTracingDrive,setTracingDrive, doc='2 : Tracing Drive (0.0,1.0)')

	def getTracingFreq(self):
		return self.params[3].value

	def setTracingFreq(self,value):
		self.params[3].value = value

	tracingFreq = property(getTracingFreq,setTracingFreq, doc='3 : Tracing Freq. (0.0,1.0)')

	def getTracingWidth(self):
		return self.params[4].value

	def setTracingWidth(self,value):
		self.params[4].value = value

	tracingWidth = property(getTracingWidth,setTracingWidth, doc='4 : Tracing Width (0.0,1.0)')

	def getPinchOn(self):
		return self.params[5].value

	def setPinchOn(self,value):
		self.params[5].value = value

	pinchOn = property(getPinchOn,setPinchOn, doc='5 : Pinch On (0.0,1.0:Q)')

	def getPinchDrive(self):
		return self.params[6].value

	def setPinchDrive(self,value):
		self.params[6].value = value

	pinchDrive = property(getPinchDrive,setPinchDrive, doc='6 : Pinch Drive (0.0,1.0)')

	def getPinchFreq(self):
		return self.params[7].value

	def setPinchFreq(self,value):
		self.params[7].value = value

	pinchFreq = property(getPinchFreq,setPinchFreq, doc='7 : Pinch Freq. (0.0,1.0)')

	def getPinchWidth(self):
		return self.params[8].value

	def setPinchWidth(self,value):
		self.params[8].value = value

	pinchWidth = property(getPinchWidth,setPinchWidth, doc='8 : Pinch Width (0.0,1.0)')

	def getGlobalDrive(self):
		return self.params[9].value

	def setGlobalDrive(self,value):
		self.params[9].value = value

	globalDrive = property(getGlobalDrive,setGlobalDrive, doc='9 : Global Drive (0.0,1.0)')

	def getPinchSoftOn(self):
		return self.params[10].value

	def setPinchSoftOn(self,value):
		self.params[10].value = value

	pinchSoftOn = property(getPinchSoftOn,setPinchSoftOn, doc='10 : Pinch Soft On (0.0,1.0:Q)')

	def getPinchMonoOn(self):
		return self.params[11].value

	def setPinchMonoOn(self,value):
		self.params[11].value = value

	pinchMonoOn = property(getPinchMonoOn,setPinchMonoOn, doc='11 : Pinch Mono On (0.0,1.0:Q)')

	def getCrackleDensity(self):
		return self.params[12].value

	def setCrackleDensity(self,value):
		self.params[12].value = value

	crackleDensity = property(getCrackleDensity,setCrackleDensity, doc='12 : Crackle Density (0.0,50.0)')

	def getCrackleVolume(self):
		return self.params[13].value

	def setCrackleVolume(self,value):
		self.params[13].value = value

	crackleVolume = property(getCrackleVolume,setCrackleVolume, doc='13 : Crackle Volume (0.0,1.0)')

