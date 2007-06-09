class CompressorII:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value=None):
		if value != None:
			self.params[0].value = value
		return self.params[0].value

	def threshold(self,value=None):
		if value != None:
			self.params[1].value = value
		return self.params[1].value

	def ratio(self,value=None):
		if value != None:
			self.params[2].value = value
		return self.params[2].value

	def attack(self,value=None):
		if value != None:
			self.params[3].value = value
		return self.params[3].value

	def release(self,value=None):
		if value != None:
			self.params[4].value = value
		return self.params[4].value

	def outputGain(self,value=None):
		if value != None:
			self.params[5].value = value
		return self.params[5].value

	def freq(self,value=None):
		if value != None:
			self.params[6].value = value
		return self.params[6].value

	def sidegain(self,value=None):
		if value != None:
			self.params[7].value = value
		return self.params[7].value

	def sideon(self,value=None):
		if value != None:
			self.params[8].value = value
		return self.params[8].value

	def peakon(self,value=None):
		if value != None:
			self.params[9].value = value
		return self.params[9].value

	def lookahead(self,value=None):
		if value != None:
			self.params[10].value = value
		return self.params[10].value

	def sidemode(self,value=None):
		if value != None:
			self.params[11].value = value
		return self.params[11].value

