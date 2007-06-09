class Erosion:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value):
		self.params[0].value = value

	def mode(self,value):
		self.params[1].value = value

	def frequency(self,value):
		self.params[2].value = value

	def amount(self,value):
		self.params[3].value = value

	def width(self,value):
		self.params[4].value = value

