from LiveModel import DeviceBase

class Redux(DeviceBase):

	def __init__(self,device):
		DeviceBase.__init__(self, device)

	def getDeviceOn(self):
		return self.params[0].value

	def setDeviceOn(self,value):
		self.params[0].value = value

	deviceOn = property(getDeviceOn,setDeviceOn, doc='0 : Device On (0.0,1.0:Q)')

	def getBitOn(self):
		return self.params[1].value

	def setBitOn(self,value):
		self.params[1].value = value

	bitOn = property(getBitOn,setBitOn, doc='1 : Bit On (0.0,1.0:Q)')

	def getBitDepth(self):
		return self.params[2].value

	def setBitDepth(self,value):
		self.params[2].value = value

	bitDepth = property(getBitDepth,setBitDepth, doc='2 : Bit Depth (1.0,16.0)')

	def getSampleMode(self):
		return self.params[3].value

	def setSampleMode(self,value):
		self.params[3].value = value

	sampleMode = property(getSampleMode,setSampleMode, doc='3 : Sample Mode (0.0,1.0:Q)')

	def getSampleHard(self):
		return self.params[4].value

	def setSampleHard(self,value):
		self.params[4].value = value

	sampleHard = property(getSampleHard,setSampleHard, doc='4 : Sample Hard (1.0,200.0)')

	def getSampleSoft(self):
		return self.params[5].value

	def setSampleSoft(self,value):
		self.params[5].value = value

	sampleSoft = property(getSampleSoft,setSampleSoft, doc='5 : Sample Soft (1.0,20.0)')

