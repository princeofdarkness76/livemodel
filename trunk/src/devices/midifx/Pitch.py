class Pitch:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value=None):
		if value != None:
			self.params[0].value = value
		return self.params[0].value

	def pitch(self,value=None):
		if value != None:
			self.params[1].value = value
		return self.params[1].value

	def lowest(self,value=None):
		if value != None:
			self.params[2].value = value
		return self.params[2].value

	def range(self,value=None):
		if value != None:
			self.params[3].value = value
		return self.params[3].value

