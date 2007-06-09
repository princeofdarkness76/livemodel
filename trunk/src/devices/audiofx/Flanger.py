class Flanger:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value=None):
		if value != None:
			self.params[0].value = value
		return self.params[0].value

	def dryWet(self,value=None):
		if value != None:
			self.params[1].value = value
		return self.params[1].value

	def delayTime(self,value=None):
		if value != None:
			self.params[2].value = value
		return self.params[2].value

	def feedback(self,value=None):
		if value != None:
			self.params[3].value = value
		return self.params[3].value

	def polarity(self,value=None):
		if value != None:
			self.params[4].value = value
		return self.params[4].value

	def lfoAmount(self,value=None):
		if value != None:
			self.params[5].value = value
		return self.params[5].value

	def hiPass(self,value=None):
		if value != None:
			self.params[6].value = value
		return self.params[6].value

	def envModulation(self,value=None):
		if value != None:
			self.params[7].value = value
		return self.params[7].value

	def envAttack(self,value=None):
		if value != None:
			self.params[8].value = value
		return self.params[8].value

	def envRelease(self,value=None):
		if value != None:
			self.params[9].value = value
		return self.params[9].value

	def lfoWaveform(self,value=None):
		if value != None:
			self.params[10].value = value
		return self.params[10].value

	def frequency(self,value=None):
		if value != None:
			self.params[11].value = value
		return self.params[11].value

	def sync(self,value=None):
		if value != None:
			self.params[12].value = value
		return self.params[12].value

	def syncRate(self,value=None):
		if value != None:
			self.params[13].value = value
		return self.params[13].value

	def lfoStereoMode(self,value=None):
		if value != None:
			self.params[14].value = value
		return self.params[14].value

	def lfoSpin(self,value=None):
		if value != None:
			self.params[15].value = value
		return self.params[15].value

	def lfoPhase(self,value=None):
		if value != None:
			self.params[16].value = value
		return self.params[16].value

	def lfoOffset(self,value=None):
		if value != None:
			self.params[17].value = value
		return self.params[17].value

	def lfoWidthRandom(self,value=None):
		if value != None:
			self.params[18].value = value
		return self.params[18].value

