class Random:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value):
		self.params[0].value = value

	def chance(self,value):
		self.params[1].value = value

	def choices(self,value):
		self.params[2].value = value

	def scale(self,value):
		self.params[3].value = value

	def sign(self,value):
		self.params[4].value = value

