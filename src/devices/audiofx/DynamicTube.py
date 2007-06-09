class DynamicTube:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value=None):
		if value != None:
			self.params[0].value = value
		return self.params[0].value

	def dryWet(self,value=None):
		if value != None:
			self.params[1].value = value
		return self.params[1].value

	def drive(self,value=None):
		if value != None:
			self.params[2].value = value
		return self.params[2].value

	def output(self,value=None):
		if value != None:
			self.params[3].value = value
		return self.params[3].value

	def bias(self,value=None):
		if value != None:
			self.params[4].value = value
		return self.params[4].value

	def envelope(self,value=None):
		if value != None:
			self.params[5].value = value
		return self.params[5].value

	def attack(self,value=None):
		if value != None:
			self.params[6].value = value
		return self.params[6].value

	def release(self,value=None):
		if value != None:
			self.params[7].value = value
		return self.params[7].value

	def tone(self,value=None):
		if value != None:
			self.params[8].value = value
		return self.params[8].value

	def tubeType(self,value=None):
		if value != None:
			self.params[9].value = value
		return self.params[9].value

