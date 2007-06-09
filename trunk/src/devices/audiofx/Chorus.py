class Chorus:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value):
		self.params[0].value = value

	def delay1Time(self,value):
		self.params[1].value = value

	def delay1Hipass(self,value):
		self.params[2].value = value

	def delay2Time(self,value):
		self.params[3].value = value

	def delay2Mode(self,value):
		self.params[4].value = value

	def linkOn(self,value):
		self.params[5].value = value

	def lfoAmount(self,value):
		self.params[6].value = value

	def lfoRate(self,value):
		self.params[7].value = value

	def lfoExtendOn(self,value):
		self.params[8].value = value

	def feedback(self,value):
		self.params[9].value = value

	def polarity(self,value):
		self.params[10].value = value

	def dryWet(self,value):
		self.params[11].value = value

