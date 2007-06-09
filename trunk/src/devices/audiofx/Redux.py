class Redux:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value=None):
		if value != None:
			self.params[0].value = value
		return self.params[0].value

	def bitOn(self,value=None):
		if value != None:
			self.params[1].value = value
		return self.params[1].value

	def bitDepth(self,value=None):
		if value != None:
			self.params[2].value = value
		return self.params[2].value

	def sampleMode(self,value=None):
		if value != None:
			self.params[3].value = value
		return self.params[3].value

	def sampleHard(self,value=None):
		if value != None:
			self.params[4].value = value
		return self.params[4].value

	def sampleSoft(self,value=None):
		if value != None:
			self.params[5].value = value
		return self.params[5].value

