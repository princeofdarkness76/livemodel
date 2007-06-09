class Redux:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value):
		self.params[0].value = value

	def bitOn(self,value):
		self.params[1].value = value

	def bitDepth(self,value):
		self.params[2].value = value

	def sampleMode(self,value):
		self.params[3].value = value

	def sampleHard(self,value):
		self.params[4].value = value

	def sampleSoft(self,value):
		self.params[5].value = value

