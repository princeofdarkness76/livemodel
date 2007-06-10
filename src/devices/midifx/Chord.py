from LiveModel import DeviceBase

class Chord(DeviceBase):

	def __init__(self,device):
		DeviceBase.__init__(self, device)

	def getDeviceOn(self):
		return self.params[0].value

	def setDeviceOn(self,value):
		self.params[0].value = value

	deviceOn = property(getDeviceOn,setDeviceOn, doc='0 : Device On (0.0,1.0:Q)')

	def getShift1(self):
		return self.params[1].value

	def setShift1(self,value):
		self.params[1].value = value

	shift1 = property(getShift1,setShift1, doc='1 : Shift1 (-36.0,36.0)')

	def getVelocity1(self):
		return self.params[2].value

	def setVelocity1(self,value):
		self.params[2].value = value

	velocity1 = property(getVelocity1,setVelocity1, doc='2 : Velocity1 (0.00999999977648,2.0)')

	def getShift2(self):
		return self.params[3].value

	def setShift2(self,value):
		self.params[3].value = value

	shift2 = property(getShift2,setShift2, doc='3 : Shift2 (-36.0,36.0)')

	def getVelocity2(self):
		return self.params[4].value

	def setVelocity2(self,value):
		self.params[4].value = value

	velocity2 = property(getVelocity2,setVelocity2, doc='4 : Velocity2 (0.00999999977648,2.0)')

	def getShift3(self):
		return self.params[5].value

	def setShift3(self,value):
		self.params[5].value = value

	shift3 = property(getShift3,setShift3, doc='5 : Shift3 (-36.0,36.0)')

	def getVelocity3(self):
		return self.params[6].value

	def setVelocity3(self,value):
		self.params[6].value = value

	velocity3 = property(getVelocity3,setVelocity3, doc='6 : Velocity3 (0.00999999977648,2.0)')

	def getShift4(self):
		return self.params[7].value

	def setShift4(self,value):
		self.params[7].value = value

	shift4 = property(getShift4,setShift4, doc='7 : Shift4 (-36.0,36.0)')

	def getVelocity4(self):
		return self.params[8].value

	def setVelocity4(self,value):
		self.params[8].value = value

	velocity4 = property(getVelocity4,setVelocity4, doc='8 : Velocity4 (0.00999999977648,2.0)')

	def getShift5(self):
		return self.params[9].value

	def setShift5(self,value):
		self.params[9].value = value

	shift5 = property(getShift5,setShift5, doc='9 : Shift5 (-36.0,36.0)')

	def getVelocity5(self):
		return self.params[10].value

	def setVelocity5(self,value):
		self.params[10].value = value

	velocity5 = property(getVelocity5,setVelocity5, doc='10 : Velocity5 (0.00999999977648,2.0)')

	def getShift6(self):
		return self.params[11].value

	def setShift6(self,value):
		self.params[11].value = value

	shift6 = property(getShift6,setShift6, doc='11 : Shift6 (-36.0,36.0)')

	def getVelocity6(self):
		return self.params[12].value

	def setVelocity6(self,value):
		self.params[12].value = value

	velocity6 = property(getVelocity6,setVelocity6, doc='12 : Velocity6 (0.00999999977648,2.0)')

