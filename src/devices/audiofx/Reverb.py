class Reverb:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value=None):
		if value != None:
			self.params[0].value = value
		return self.params[0].value

	def predelay(self,value=None):
		if value != None:
			self.params[1].value = value
		return self.params[1].value

	def inLowcutOn(self,value=None):
		if value != None:
			self.params[2].value = value
		return self.params[2].value

	def inHighcutOn(self,value=None):
		if value != None:
			self.params[3].value = value
		return self.params[3].value

	def inFreqency(self,value=None):
		if value != None:
			self.params[4].value = value
		return self.params[4].value

	def inWidth(self,value=None):
		if value != None:
			self.params[5].value = value
		return self.params[5].value

	def erSpinOn(self,value=None):
		if value != None:
			self.params[6].value = value
		return self.params[6].value

	def erSpinRate(self,value=None):
		if value != None:
			self.params[7].value = value
		return self.params[7].value

	def erSpinAmount(self,value=None):
		if value != None:
			self.params[8].value = value
		return self.params[8].value

	def erShape(self,value=None):
		if value != None:
			self.params[9].value = value
		return self.params[9].value

	def hishelfOn(self,value=None):
		if value != None:
			self.params[10].value = value
		return self.params[10].value

	def hishelfFreq(self,value=None):
		if value != None:
			self.params[11].value = value
		return self.params[11].value

	def hishelfGain(self,value=None):
		if value != None:
			self.params[12].value = value
		return self.params[12].value

	def lowshelfOn(self,value=None):
		if value != None:
			self.params[13].value = value
		return self.params[13].value

	def lowshelfFreq(self,value=None):
		if value != None:
			self.params[14].value = value
		return self.params[14].value

	def lowshelfGain(self,value=None):
		if value != None:
			self.params[15].value = value
		return self.params[15].value

	def chorusOn(self,value=None):
		if value != None:
			self.params[16].value = value
		return self.params[16].value

	def chorusRate(self,value=None):
		if value != None:
			self.params[17].value = value
		return self.params[17].value

	def chorusAmount(self,value=None):
		if value != None:
			self.params[18].value = value
		return self.params[18].value

	def decaytime(self,value=None):
		if value != None:
			self.params[19].value = value
		return self.params[19].value

	def density(self,value=None):
		if value != None:
			self.params[20].value = value
		return self.params[20].value

	def scale(self,value=None):
		if value != None:
			self.params[21].value = value
		return self.params[21].value

	def freezeOn(self,value=None):
		if value != None:
			self.params[22].value = value
		return self.params[22].value

	def flatOn(self,value=None):
		if value != None:
			self.params[23].value = value
		return self.params[23].value

	def cutOn(self,value=None):
		if value != None:
			self.params[24].value = value
		return self.params[24].value

	def roomSize(self,value=None):
		if value != None:
			self.params[25].value = value
		return self.params[25].value

	def stereoImage(self,value=None):
		if value != None:
			self.params[26].value = value
		return self.params[26].value

	def quality(self,value=None):
		if value != None:
			self.params[27].value = value
		return self.params[27].value

	def erLevel(self,value=None):
		if value != None:
			self.params[28].value = value
		return self.params[28].value

	def diffuseLevel(self,value=None):
		if value != None:
			self.params[29].value = value
		return self.params[29].value

	def dryWet(self,value=None):
		if value != None:
			self.params[30].value = value
		return self.params[30].value

