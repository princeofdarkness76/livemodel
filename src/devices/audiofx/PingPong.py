class PingPong:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value=None):
		if value != None:
			self.params[0].value = value
		return self.params[0].value

	def eqFreq(self,value=None):
		if value != None:
			self.params[1].value = value
		return self.params[1].value

	def eqWidth(self,value=None):
		if value != None:
			self.params[2].value = value
		return self.params[2].value

	def delayMode(self,value=None):
		if value != None:
			self.params[3].value = value
		return self.params[3].value

	def beatDelay(self,value=None):
		if value != None:
			self.params[4].value = value
		return self.params[4].value

	def beatSwing(self,value=None):
		if value != None:
			self.params[5].value = value
		return self.params[5].value

	def timeDelay(self,value=None):
		if value != None:
			self.params[6].value = value
		return self.params[6].value

	def feedback(self,value=None):
		if value != None:
			self.params[7].value = value
		return self.params[7].value

	def dryWet(self,value=None):
		if value != None:
			self.params[8].value = value
		return self.params[8].value

	def freeze(self,value=None):
		if value != None:
			self.params[9].value = value
		return self.params[9].value

