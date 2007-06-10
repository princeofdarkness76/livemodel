from LiveModel import DeviceBase

class EQThree(DeviceBase):

	def __init__(self,device):
		DeviceBase.__init__(self, device)

	def getDeviceOn(self):
		return self.params[0].value

	def setDeviceOn(self,value):
		self.params[0].value = value

	deviceOn = property(getDeviceOn,setDeviceOn, doc='0 : Device On (0.0,1.0:Q)')

	def getGainlo(self):
		return self.params[1].value

	def setGainlo(self,value):
		self.params[1].value = value

	gainlo = property(getGainlo,setGainlo, doc='1 : GainLo (0.0,1.0)')

	def getGainmid(self):
		return self.params[2].value

	def setGainmid(self,value):
		self.params[2].value = value

	gainmid = property(getGainmid,setGainmid, doc='2 : GainMid (0.0,1.0)')

	def getGainhi(self):
		return self.params[3].value

	def setGainhi(self,value):
		self.params[3].value = value

	gainhi = property(getGainhi,setGainhi, doc='3 : GainHi (0.0,1.0)')

	def getFreqlo(self):
		return self.params[4].value

	def setFreqlo(self,value):
		self.params[4].value = value

	freqlo = property(getFreqlo,setFreqlo, doc='4 : FreqLo (0.0,1.0)')

	def getFreqhi(self):
		return self.params[5].value

	def setFreqhi(self,value):
		self.params[5].value = value

	freqhi = property(getFreqhi,setFreqhi, doc='5 : FreqHi (0.0,1.0)')

	def getLowon(self):
		return self.params[6].value

	def setLowon(self,value):
		self.params[6].value = value

	lowon = property(getLowon,setLowon, doc='6 : LowOn (0.0,1.0:Q)')

	def getMidon(self):
		return self.params[7].value

	def setMidon(self,value):
		self.params[7].value = value

	midon = property(getMidon,setMidon, doc='7 : MidOn (0.0,1.0:Q)')

	def getHighon(self):
		return self.params[8].value

	def setHighon(self,value):
		self.params[8].value = value

	highon = property(getHighon,setHighon, doc='8 : HighOn (0.0,1.0:Q)')

	def getSlope(self):
		return self.params[9].value

	def setSlope(self,value):
		self.params[9].value = value

	slope = property(getSlope,setSlope, doc='9 : Slope (0.0,1.0:Q)')

