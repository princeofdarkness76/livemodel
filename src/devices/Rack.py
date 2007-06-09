class Rack:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value=None):
		if value != None:
			self.params[0].value = value
		return self.params[0].value

	def macro1(self,value=None):
		if value != None:
			self.params[1].value = value
		return self.params[1].value

	def macro2(self,value=None):
		if value != None:
			self.params[2].value = value
		return self.params[2].value

	def macro3(self,value=None):
		if value != None:
			self.params[3].value = value
		return self.params[3].value

	def macro4(self,value=None):
		if value != None:
			self.params[4].value = value
		return self.params[4].value

	def macro5(self,value=None):
		if value != None:
			self.params[5].value = value
		return self.params[5].value

	def macro6(self,value=None):
		if value != None:
			self.params[6].value = value
		return self.params[6].value

	def macro7(self,value=None):
		if value != None:
			self.params[7].value = value
		return self.params[7].value

	def macro8(self,value=None):
		if value != None:
			self.params[8].value = value
		return self.params[8].value

	def chainSelector(self,value=None):
		if value != None:
			self.params[9].value = value
		return self.params[9].value

