class SimpleDelay:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value=None):
		if value != None:
			self.params[0].value = value
		return self.params[0].value

	def linkOn(self,value=None):
		if value != None:
			self.params[1].value = value
		return self.params[1].value

	def lDelayMode(self,value=None):
		if value != None:
			self.params[2].value = value
		return self.params[2].value

	def lBeatDelay(self,value=None):
		if value != None:
			self.params[3].value = value
		return self.params[3].value

	def lBeatSwing(self,value=None):
		if value != None:
			self.params[4].value = value
		return self.params[4].value

	def lTimeDelay(self,value=None):
		if value != None:
			self.params[5].value = value
		return self.params[5].value

	def rDelayMode(self,value=None):
		if value != None:
			self.params[6].value = value
		return self.params[6].value

	def rBeatDelay(self,value=None):
		if value != None:
			self.params[7].value = value
		return self.params[7].value

	def rBeatSwing(self,value=None):
		if value != None:
			self.params[8].value = value
		return self.params[8].value

	def rTimeDelay(self,value=None):
		if value != None:
			self.params[9].value = value
		return self.params[9].value

	def feedback(self,value=None):
		if value != None:
			self.params[10].value = value
		return self.params[10].value

	def dryWet(self,value=None):
		if value != None:
			self.params[11].value = value
		return self.params[11].value

