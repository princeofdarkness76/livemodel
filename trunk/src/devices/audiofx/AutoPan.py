class AutoPan:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value=None):
		if value != None:
			self.params[0].value = value
		return self.params[0].value

	def lfoType(self,value=None):
		if value != None:
			self.params[1].value = value
		return self.params[1].value

	def amount(self,value=None):
		if value != None:
			self.params[2].value = value
		return self.params[2].value

	def frequency(self,value=None):
		if value != None:
			self.params[3].value = value
		return self.params[3].value

	def syncRate(self,value=None):
		if value != None:
			self.params[4].value = value
		return self.params[4].value

	def phase(self,value=None):
		if value != None:
			self.params[5].value = value
		return self.params[5].value

	def spin(self,value=None):
		if value != None:
			self.params[6].value = value
		return self.params[6].value

	def stereoMode(self,value=None):
		if value != None:
			self.params[7].value = value
		return self.params[7].value

	def offset(self,value=None):
		if value != None:
			self.params[8].value = value
		return self.params[8].value

	def waveform(self,value=None):
		if value != None:
			self.params[9].value = value
		return self.params[9].value

	def shape(self,value=None):
		if value != None:
			self.params[10].value = value
		return self.params[10].value

	def widthRandom(self,value=None):
		if value != None:
			self.params[11].value = value
		return self.params[11].value

	def invert(self,value=None):
		if value != None:
			self.params[12].value = value
		return self.params[12].value

