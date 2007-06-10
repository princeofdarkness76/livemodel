from LiveModel import DeviceBase

class CompressorI(DeviceBase):

	def __init__(self,device):
		DeviceBase.__init__(self, device)

	def getDeviceOn(self):
		return self.params[0].value

	def setDeviceOn(self,value):
		self.params[0].value = value

	deviceOn = property(getDeviceOn,setDeviceOn, doc='0 : Device On (0.0,1.0:Q)')

	def getThreshold(self):
		return self.params[1].value

	def setThreshold(self,value):
		self.params[1].value = value

	threshold = property(getThreshold,setThreshold, doc='1 : Threshold (-60.0,0.0)')

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

	outputGain = property(getOutputGain,setOutputGain, doc='5 : Output Gain (-5.0,35.0)')

