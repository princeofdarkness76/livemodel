class Reverb:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value):
		self.params[0].value = value

	def predelay(self,value):
		self.params[1].value = value

	def inLowcutOn(self,value):
		self.params[2].value = value

	def inHighcutOn(self,value):
		self.params[3].value = value

	def inFreqency(self,value):
		self.params[4].value = value

	def inWidth(self,value):
		self.params[5].value = value

	def erSpinOn(self,value):
		self.params[6].value = value

	def erSpinRate(self,value):
		self.params[7].value = value

	def erSpinAmount(self,value):
		self.params[8].value = value

	def erShape(self,value):
		self.params[9].value = value

	def hishelfOn(self,value):
		self.params[10].value = value

	def hishelfFreq(self,value):
		self.params[11].value = value

	def hishelfGain(self,value):
		self.params[12].value = value

	def lowshelfOn(self,value):
		self.params[13].value = value

	def lowshelfFreq(self,value):
		self.params[14].value = value

	def lowshelfGain(self,value):
		self.params[15].value = value

	def chorusOn(self,value):
		self.params[16].value = value

	def chorusRate(self,value):
		self.params[17].value = value

	def chorusAmount(self,value):
		self.params[18].value = value

	def decaytime(self,value):
		self.params[19].value = value

	def density(self,value):
		self.params[20].value = value

	def scale(self,value):
		self.params[21].value = value

	def freezeOn(self,value):
		self.params[22].value = value

	def flatOn(self,value):
		self.params[23].value = value

	def cutOn(self,value):
		self.params[24].value = value

	def roomSize(self,value):
		self.params[25].value = value

	def stereoImage(self,value):
		self.params[26].value = value

	def quality(self,value):
		self.params[27].value = value

	def erLevel(self,value):
		self.params[28].value = value

	def diffuseLevel(self,value):
		self.params[29].value = value

	def dryWet(self,value):
		self.params[30].value = value

