class Resonators:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value=None):
		if value != None:
			self.params[0].value = value
		return self.params[0].value

	def filterOn(self,value=None):
		if value != None:
			self.params[1].value = value
		return self.params[1].value

	def frequency(self,value=None):
		if value != None:
			self.params[2].value = value
		return self.params[2].value

	def filterType(self,value=None):
		if value != None:
			self.params[3].value = value
		return self.params[3].value

	def mode(self,value=None):
		if value != None:
			self.params[4].value = value
		return self.params[4].value

	def decay(self,value=None):
		if value != None:
			self.params[5].value = value
		return self.params[5].value

	def const(self,value=None):
		if value != None:
			self.params[6].value = value
		return self.params[6].value

	def color(self,value=None):
		if value != None:
			self.params[7].value = value
		return self.params[7].value

	def width(self,value=None):
		if value != None:
			self.params[8].value = value
		return self.params[8].value

	def dryWet(self,value=None):
		if value != None:
			self.params[9].value = value
		return self.params[9].value

	def globalGain(self,value=None):
		if value != None:
			self.params[10].value = value
		return self.params[10].value

	def iOn(self,value=None):
		if value != None:
			self.params[11].value = value
		return self.params[11].value

	def iNote(self,value=None):
		if value != None:
			self.params[12].value = value
		return self.params[12].value

	def iTune(self,value=None):
		if value != None:
			self.params[13].value = value
		return self.params[13].value

	def iGain(self,value=None):
		if value != None:
			self.params[14].value = value
		return self.params[14].value

	def iiOn(self,value=None):
		if value != None:
			self.params[15].value = value
		return self.params[15].value

	def iiPitch(self,value=None):
		if value != None:
			self.params[16].value = value
		return self.params[16].value

	def iiTune(self,value=None):
		if value != None:
			self.params[17].value = value
		return self.params[17].value

	def iiGain(self,value=None):
		if value != None:
			self.params[18].value = value
		return self.params[18].value

	def iiiOn(self,value=None):
		if value != None:
			self.params[19].value = value
		return self.params[19].value

	def iiiPitch(self,value=None):
		if value != None:
			self.params[20].value = value
		return self.params[20].value

	def iiiTune(self,value=None):
		if value != None:
			self.params[21].value = value
		return self.params[21].value

	def iiiGain(self,value=None):
		if value != None:
			self.params[22].value = value
		return self.params[22].value

	def ivOn(self,value=None):
		if value != None:
			self.params[23].value = value
		return self.params[23].value

	def ivPitch(self,value=None):
		if value != None:
			self.params[24].value = value
		return self.params[24].value

	def ivTune(self,value=None):
		if value != None:
			self.params[25].value = value
		return self.params[25].value

	def ivGain(self,value=None):
		if value != None:
			self.params[26].value = value
		return self.params[26].value

	def vOn(self,value=None):
		if value != None:
			self.params[27].value = value
		return self.params[27].value

	def vPitch(self,value=None):
		if value != None:
			self.params[28].value = value
		return self.params[28].value

	def vTune(self,value=None):
		if value != None:
			self.params[29].value = value
		return self.params[29].value

	def vGain(self,value=None):
		if value != None:
			self.params[30].value = value
		return self.params[30].value

