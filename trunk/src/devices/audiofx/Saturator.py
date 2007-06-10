from LiveModel import DeviceBase

class Saturator(DeviceBase):

	def __init__(self,device):
		DeviceBase.__init__(self, device)

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

	def getDrive(self):
		return self.params[2].value

	def setDrive(self,value):
		self.params[2].value = value

	drive = property(getDrive,setDrive, doc='2 : Drive (-36.0,36.0)')

	def getOutput(self):
		return self.params[3].value

	def setOutput(self,value):
		self.params[3].value = value

	output = property(getOutput,setOutput, doc='3 : Output (-36.0,0.0)')

	def getType(self):
		return self.params[4].value

	def setType(self,value):
		self.params[4].value = value

	type = property(getType,setType, doc='4 : Type (0.0,6.0:Q)')

	def getBase(self):
		return self.params[5].value

	def setBase(self,value):
		self.params[5].value = value

	base = property(getBase,setBase, doc='5 : Base (-36.0,36.0)')

	def getColor(self):
		return self.params[6].value

	def setColor(self,value):
		self.params[6].value = value

	color = property(getColor,setColor, doc='6 : Color (0.0,1.0:Q)')

	def getFrequency(self):
		return self.params[7].value

	def setFrequency(self,value):
		self.params[7].value = value

	frequency = property(getFrequency,setFrequency, doc='7 : Frequency (0.0,1.0)')

	def getWidth(self):
		return self.params[8].value

	def setWidth(self,value):
		self.params[8].value = value

	width = property(getWidth,setWidth, doc='8 : Width (0.0,1.0)')

	def getDepth(self):
		return self.params[9].value

	def setDepth(self,value):
		self.params[9].value = value

	depth = property(getDepth,setDepth, doc='9 : Depth (-24.0,24.0)')

	def getSoftClip(self):
		return self.params[10].value

	def setSoftClip(self,value):
		self.params[10].value = value

	softClip = property(getSoftClip,setSoftClip, doc='10 : Soft Clip (0.0,1.0:Q)')

	def getWsDrive(self):
		return self.params[11].value

	def setWsDrive(self,value):
		self.params[11].value = value

	wsDrive = property(getWsDrive,setWsDrive, doc='11 : WS Drive (0.0,1.0)')

	def getWsLin(self):
		return self.params[12].value

	def setWsLin(self,value):
		self.params[12].value = value

	wsLin = property(getWsLin,setWsLin, doc='12 : WS Lin (0.0,1.0)')

	def getWsCurve(self):
		return self.params[13].value

	def setWsCurve(self,value):
		self.params[13].value = value

	wsCurve = property(getWsCurve,setWsCurve, doc='13 : WS Curve (0.0,1.0)')

	def getWsDamp(self):
		return self.params[14].value

	def setWsDamp(self,value):
		self.params[14].value = value

	wsDamp = property(getWsDamp,setWsDamp, doc='14 : WS Damp (0.0,1.0)')

	def getWsPeriod(self):
		return self.params[15].value

	def setWsPeriod(self,value):
		self.params[15].value = value

	wsPeriod = property(getWsPeriod,setWsPeriod, doc='15 : WS Period (0.0,1.0)')

	def getWsDepth(self):
		return self.params[16].value

	def setWsDepth(self,value):
		self.params[16].value = value

	wsDepth = property(getWsDepth,setWsDepth, doc='16 : WS Depth (0.0,1.0)')

