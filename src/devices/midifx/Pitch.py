class Pitch:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value):
		self.params[0].value = value

	def pitch(self,value):
		self.params[1].value = value

	def lowest(self,value):
		self.params[2].value = value

	def range(self,value):
		self.params[3].value = value

