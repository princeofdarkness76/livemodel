class Utility:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def getDeviceOn(self):
		return self.params[0].value

	def setDeviceOn(self,value):
		self.params[0].value = value

	deviceOn = property(getDeviceOn,setDeviceOn, doc='0 : Device On (0.0,1.0:Q)')

	def getGain(self):
		return self.params[1].value

	def setGain(self,value):
		self.params[1].value = value

	gain = property(getGain,setGain, doc='1 : Gain (-35.0,35.0)')

	def getPanorama(self):
		return self.params[2].value

	def setPanorama(self,value):
		self.params[2].value = value

	panorama = property(getPanorama,setPanorama, doc='2 : Panorama (-1.0,1.0)')

	def getSignalSource(self):
		return self.params[3].value

	def setSignalSource(self,value):
		self.params[3].value = value

	signalSource = property(getSignalSource,setSignalSource, doc='3 : Signal Source (0.0,3.0:Q)')

	def getStereoseparation(self):
		return self.params[4].value

	def setStereoseparation(self,value):
		self.params[4].value = value

	stereoseparation = property(getStereoseparation,setStereoseparation, doc='4 : StereoSeparation (0.0,2.0)')

	def getPhaseinvertl(self):
		return self.params[5].value

	def setPhaseinvertl(self,value):
		self.params[5].value = value

	phaseinvertl = property(getPhaseinvertl,setPhaseinvertl, doc='5 : PhaseInvertL (0.0,1.0:Q)')

	def getPhaseinvertr(self):
		return self.params[6].value

	def setPhaseinvertr(self,value):
		self.params[6].value = value

	phaseinvertr = property(getPhaseinvertr,setPhaseinvertr, doc='6 : PhaseInvertR (0.0,1.0:Q)')

	def getMute(self):
		return self.params[7].value

	def setMute(self,value):
		self.params[7].value = value

	mute = property(getMute,setMute, doc='7 : Mute (0.0,1.0:Q)')

	def getBlockdc(self):
		return self.params[8].value

	def setBlockdc(self,value):
		self.params[8].value = value

	blockdc = property(getBlockdc,setBlockdc, doc='8 : BlockDc (0.0,1.0:Q)')

