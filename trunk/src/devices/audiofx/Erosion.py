class Erosion:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value=None):
		if value != None:
			self.params[0].value = value
		return self.params[0].value

	def mode(self,value=None):
		if value != None:
			self.params[1].value = value
		return self.params[1].value

	def frequency(self,value=None):
		if value != None:
			self.params[2].value = value
		return self.params[2].value

	def amount(self,value=None):
		if value != None:
			self.params[3].value = value
		return self.params[3].value

	def width(self,value=None):
		if value != None:
			self.params[4].value = value
		return self.params[4].value

