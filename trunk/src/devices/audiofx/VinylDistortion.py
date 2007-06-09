class VinylDistortion:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value=None):
		if value != None:
			self.params[0].value = value
		return self.params[0].value

	def tracingOn(self,value=None):
		if value != None:
			self.params[1].value = value
		return self.params[1].value

	def tracingDrive(self,value=None):
		if value != None:
			self.params[2].value = value
		return self.params[2].value

	def tracingFreq(self,value=None):
		if value != None:
			self.params[3].value = value
		return self.params[3].value

	def tracingWidth(self,value=None):
		if value != None:
			self.params[4].value = value
		return self.params[4].value

	def pinchOn(self,value=None):
		if value != None:
			self.params[5].value = value
		return self.params[5].value

	def pinchDrive(self,value=None):
		if value != None:
			self.params[6].value = value
		return self.params[6].value

	def pinchFreq(self,value=None):
		if value != None:
			self.params[7].value = value
		return self.params[7].value

	def pinchWidth(self,value=None):
		if value != None:
			self.params[8].value = value
		return self.params[8].value

	def globalDrive(self,value=None):
		if value != None:
			self.params[9].value = value
		return self.params[9].value

	def pinchSoftOn(self,value=None):
		if value != None:
			self.params[10].value = value
		return self.params[10].value

	def pinchMonoOn(self,value=None):
		if value != None:
			self.params[11].value = value
		return self.params[11].value

	def crackleDensity(self,value=None):
		if value != None:
			self.params[12].value = value
		return self.params[12].value

	def crackleVolume(self,value=None):
		if value != None:
			self.params[13].value = value
		return self.params[13].value

