class VinylDistortion:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value):
		self.params[0].value = value

	def tracingOn(self,value):
		self.params[1].value = value

	def tracingDrive(self,value):
		self.params[2].value = value

	def tracingFreq(self,value):
		self.params[3].value = value

	def tracingWidth(self,value):
		self.params[4].value = value

	def pinchOn(self,value):
		self.params[5].value = value

	def pinchDrive(self,value):
		self.params[6].value = value

	def pinchFreq(self,value):
		self.params[7].value = value

	def pinchWidth(self,value):
		self.params[8].value = value

	def globalDrive(self,value):
		self.params[9].value = value

	def pinchSoftOn(self,value):
		self.params[10].value = value

	def pinchMonoOn(self,value):
		self.params[11].value = value

	def crackleDensity(self,value):
		self.params[12].value = value

	def crackleVolume(self,value):
		self.params[13].value = value

