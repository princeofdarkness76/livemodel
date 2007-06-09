class Resonators:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value):
		self.params[0].value = value

	def filterOn(self,value):
		self.params[1].value = value

	def frequency(self,value):
		self.params[2].value = value

	def filterType(self,value):
		self.params[3].value = value

	def mode(self,value):
		self.params[4].value = value

	def decay(self,value):
		self.params[5].value = value

	def const(self,value):
		self.params[6].value = value

	def color(self,value):
		self.params[7].value = value

	def width(self,value):
		self.params[8].value = value

	def dryWet(self,value):
		self.params[9].value = value

	def globalGain(self,value):
		self.params[10].value = value

	def iOn(self,value):
		self.params[11].value = value

	def iNote(self,value):
		self.params[12].value = value

	def iTune(self,value):
		self.params[13].value = value

	def iGain(self,value):
		self.params[14].value = value

	def iiOn(self,value):
		self.params[15].value = value

	def iiPitch(self,value):
		self.params[16].value = value

	def iiTune(self,value):
		self.params[17].value = value

	def iiGain(self,value):
		self.params[18].value = value

	def iiiOn(self,value):
		self.params[19].value = value

	def iiiPitch(self,value):
		self.params[20].value = value

	def iiiTune(self,value):
		self.params[21].value = value

	def iiiGain(self,value):
		self.params[22].value = value

	def ivOn(self,value):
		self.params[23].value = value

	def ivPitch(self,value):
		self.params[24].value = value

	def ivTune(self,value):
		self.params[25].value = value

	def ivGain(self,value):
		self.params[26].value = value

	def vOn(self,value):
		self.params[27].value = value

	def vPitch(self,value):
		self.params[28].value = value

	def vTune(self,value):
		self.params[29].value = value

	def vGain(self,value):
		self.params[30].value = value

