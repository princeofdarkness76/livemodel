class BeatRepeat:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value):
		self.params[0].value = value

	def chance(self,value):
		self.params[1].value = value

	def interval(self,value):
		self.params[2].value = value

	def offset(self,value):
		self.params[3].value = value

	def grid(self,value):
		self.params[4].value = value

	def blockTriplets(self,value):
		self.params[5].value = value

	def variation(self,value):
		self.params[6].value = value

	def variationType(self,value):
		self.params[7].value = value

	def gate(self,value):
		self.params[8].value = value

	def decay(self,value):
		self.params[9].value = value

	def pitchDecay(self,value):
		self.params[10].value = value

	def pitch(self,value):
		self.params[11].value = value

	def mixType(self,value):
		self.params[12].value = value

	def volume(self,value):
		self.params[13].value = value

	def filterOn(self,value):
		self.params[14].value = value

	def midFreq(self,value):
		self.params[15].value = value

	def eqWidth(self,value):
		self.params[16].value = value

	def repeat(self,value):
		self.params[17].value = value

