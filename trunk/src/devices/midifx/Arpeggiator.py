class Arpeggiator:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value=None):
		if value != None:
			self.params[0].value = value
		return self.params[0].value

	def style(self,value=None):
		if value != None:
			self.params[1].value = value
		return self.params[1].value

	def offset(self,value=None):
		if value != None:
			self.params[2].value = value
		return self.params[2].value

	def repeats(self,value=None):
		if value != None:
			self.params[3].value = value
		return self.params[3].value

	def syncOn(self,value=None):
		if value != None:
			self.params[4].value = value
		return self.params[4].value

	def syncedRate(self,value=None):
		if value != None:
			self.params[5].value = value
		return self.params[5].value

	def groove(self,value=None):
		if value != None:
			self.params[6].value = value
		return self.params[6].value

	def freeRate(self,value=None):
		if value != None:
			self.params[7].value = value
		return self.params[7].value

	def gate(self,value=None):
		if value != None:
			self.params[8].value = value
		return self.params[8].value

	def retriggerMode(self,value=None):
		if value != None:
			self.params[9].value = value
		return self.params[9].value

	def retInterval(self,value=None):
		if value != None:
			self.params[10].value = value
		return self.params[10].value

	def holdOn(self,value=None):
		if value != None:
			self.params[11].value = value
		return self.params[11].value

	def tranposeMode(self,value=None):
		if value != None:
			self.params[12].value = value
		return self.params[12].value

	def tranposeKey(self,value=None):
		if value != None:
			self.params[13].value = value
		return self.params[13].value

	def transpSteps(self,value=None):
		if value != None:
			self.params[14].value = value
		return self.params[14].value

	def transpDist(self,value=None):
		if value != None:
			self.params[15].value = value
		return self.params[15].value

	def velocityOn(self,value=None):
		if value != None:
			self.params[16].value = value
		return self.params[16].value

	def velRetrigger(self,value=None):
		if value != None:
			self.params[17].value = value
		return self.params[17].value

	def velocityDecay(self,value=None):
		if value != None:
			self.params[18].value = value
		return self.params[18].value

	def velocityTarget(self,value=None):
		if value != None:
			self.params[19].value = value
		return self.params[19].value

