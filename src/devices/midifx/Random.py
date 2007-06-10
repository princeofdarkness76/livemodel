from LiveModel import DeviceBase

class Random(DeviceBase):

	def __init__(self,device):
		DeviceBase.__init__(self, device)

	def getDeviceOn(self):
		return self.params[0].value

	def setDeviceOn(self,value):
		self.params[0].value = value

	deviceOn = property(getDeviceOn,setDeviceOn, doc='0 : Device On (0.0,1.0:Q)')

	def getChance(self):
		return self.params[1].value

	def setChance(self,value):
		self.params[1].value = value

	chance = property(getChance,setChance, doc='1 : Chance (0.0,1.0)')

	def getChoices(self):
		return self.params[2].value

	def setChoices(self,value):
		self.params[2].value = value

	choices = property(getChoices,setChoices, doc='2 : Choices (1.0,24.0)')

	def getScale(self):
		return self.params[3].value

	def setScale(self,value):
		self.params[3].value = value

	scale = property(getScale,setScale, doc='3 : Scale (1.0,24.0)')

	def getSign(self):
		return self.params[4].value

	def setSign(self,value):
		self.params[4].value = value

	sign = property(getSign,setSign, doc='4 : Sign (0.0,2.0:Q)')

