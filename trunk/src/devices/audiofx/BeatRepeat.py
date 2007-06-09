class BeatRepeat:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value=None):
		if value != None:
			self.params[0].value = value
		return self.params[0].value

	def chance(self,value=None):
		if value != None:
			self.params[1].value = value
		return self.params[1].value

	def interval(self,value=None):
		if value != None:
			self.params[2].value = value
		return self.params[2].value

	def offset(self,value=None):
		if value != None:
			self.params[3].value = value
		return self.params[3].value

	def grid(self,value=None):
		if value != None:
			self.params[4].value = value
		return self.params[4].value

	def blockTriplets(self,value=None):
		if value != None:
			self.params[5].value = value
		return self.params[5].value

	def variation(self,value=None):
		if value != None:
			self.params[6].value = value
		return self.params[6].value

	def variationType(self,value=None):
		if value != None:
			self.params[7].value = value
		return self.params[7].value

	def gate(self,value=None):
		if value != None:
			self.params[8].value = value
		return self.params[8].value

	def decay(self,value=None):
		if value != None:
			self.params[9].value = value
		return self.params[9].value

	def pitchDecay(self,value=None):
		if value != None:
			self.params[10].value = value
		return self.params[10].value

	def pitch(self,value=None):
		if value != None:
			self.params[11].value = value
		return self.params[11].value

	def mixType(self,value=None):
		if value != None:
			self.params[12].value = value
		return self.params[12].value

	def volume(self,value=None):
		if value != None:
			self.params[13].value = value
		return self.params[13].value

	def filterOn(self,value=None):
		if value != None:
			self.params[14].value = value
		return self.params[14].value

	def midFreq(self,value=None):
		if value != None:
			self.params[15].value = value
		return self.params[15].value

	def eqWidth(self,value=None):
		if value != None:
			self.params[16].value = value
		return self.params[16].value

	def repeat(self,value=None):
		if value != None:
			self.params[17].value = value
		return self.params[17].value

