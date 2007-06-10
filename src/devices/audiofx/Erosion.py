class Erosion:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def getDeviceOn(self):
		return self.params[0].value

	def setDeviceOn(self,value):
		self.params[0].value = value

	deviceOn = property(getDeviceOn,setDeviceOn, doc='0 : Device On (0.0,1.0:Q)')

	def getMode(self):
		return self.params[1].value

	def setMode(self,value):
		self.params[1].value = value

	mode = property(getMode,setMode, doc='1 : Mode (0.0,2.0:Q)')

	def getFrequency(self):
		return self.params[2].value

	def setFrequency(self,value):
		self.params[2].value = value

	frequency = property(getFrequency,setFrequency, doc='2 : Frequency (0.0,1.0)')

	def getAmount(self):
		return self.params[3].value

	def setAmount(self,value):
		self.params[3].value = value

	amount = property(getAmount,setAmount, doc='3 : Amount (0.0,1.0)')

	def getWidth(self):
		return self.params[4].value

	def setWidth(self,value):
		self.params[4].value = value

	width = property(getWidth,setWidth, doc='4 : Width (0.0,1.0)')

