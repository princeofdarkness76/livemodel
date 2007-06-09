class Velocity:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value=None):
		if value != None:
			self.params[0].value = value
		return self.params[0].value

	def drive(self,value=None):
		if value != None:
			self.params[1].value = value
		return self.params[1].value

	def compand(self,value=None):
		if value != None:
			self.params[2].value = value
		return self.params[2].value

	def random(self,value=None):
		if value != None:
			self.params[3].value = value
		return self.params[3].value

	def mode(self,value=None):
		if value != None:
			self.params[4].value = value
		return self.params[4].value

	def operation(self,value=None):
		if value != None:
			self.params[5].value = value
		return self.params[5].value

	def outHi(self,value=None):
		if value != None:
			self.params[6].value = value
		return self.params[6].value

	def outLow(self,value=None):
		if value != None:
			self.params[7].value = value
		return self.params[7].value

	def range(self,value=None):
		if value != None:
			self.params[8].value = value
		return self.params[8].value

	def lowest(self,value=None):
		if value != None:
			self.params[9].value = value
		return self.params[9].value

