class GrainDelay:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value):
		self.params[0].value = value

	def spray(self,value):
		self.params[1].value = value

	def frequency(self,value):
		self.params[2].value = value

	def pitch(self,value):
		self.params[3].value = value

	def random(self,value):
		self.params[4].value = value

	def feedback(self,value):
		self.params[5].value = value

	def drywet(self,value):
		self.params[6].value = value

	def delayMode(self,value):
		self.params[7].value = value

	def beatDelay(self,value):
		self.params[8].value = value

	def beatSwing(self,value):
		self.params[9].value = value

	def timeDelay(self,value):
		self.params[10].value = value

