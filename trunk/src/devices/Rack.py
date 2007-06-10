class Rack:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def getDeviceOn(self):
		return self.params[0].value

	def setDeviceOn(self,value):
		self.params[0].value = value

	deviceOn = property(getDeviceOn,setDeviceOn, doc='0 : Device On (0.0,1.0:Q)')

	def getMacro1(self):
		return self.params[1].value

	def setMacro1(self,value):
		self.params[1].value = value

	macro1 = property(getMacro1,setMacro1, doc='1 : Macro 1 (0.0,127.0)')

	def getMacro2(self):
		return self.params[2].value

	def setMacro2(self,value):
		self.params[2].value = value

	macro2 = property(getMacro2,setMacro2, doc='2 : Macro 2 (0.0,127.0)')

	def getMacro3(self):
		return self.params[3].value

	def setMacro3(self,value):
		self.params[3].value = value

	macro3 = property(getMacro3,setMacro3, doc='3 : Macro 3 (0.0,127.0)')

	def getMacro4(self):
		return self.params[4].value

	def setMacro4(self,value):
		self.params[4].value = value

	macro4 = property(getMacro4,setMacro4, doc='4 : Macro 4 (0.0,127.0)')

	def getMacro5(self):
		return self.params[5].value

	def setMacro5(self,value):
		self.params[5].value = value

	macro5 = property(getMacro5,setMacro5, doc='5 : Macro 5 (0.0,127.0)')

	def getMacro6(self):
		return self.params[6].value

	def setMacro6(self,value):
		self.params[6].value = value

	macro6 = property(getMacro6,setMacro6, doc='6 : Macro 6 (0.0,127.0)')

	def getMacro7(self):
		return self.params[7].value

	def setMacro7(self,value):
		self.params[7].value = value

	macro7 = property(getMacro7,setMacro7, doc='7 : Macro 7 (0.0,127.0)')

	def getMacro8(self):
		return self.params[8].value

	def setMacro8(self,value):
		self.params[8].value = value

	macro8 = property(getMacro8,setMacro8, doc='8 : Macro 8 (0.0,127.0)')

	def getChainSelector(self):
		return self.params[9].value

	def setChainSelector(self,value):
		self.params[9].value = value

	chainSelector = property(getChainSelector,setChainSelector, doc='9 : Chain Selector (0.0,127.0)')

