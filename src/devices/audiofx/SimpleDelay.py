class SimpleDelay:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value):
		self.params[0].value = value

	def linkOn(self,value):
		self.params[1].value = value

	def lDelayMode(self,value):
		self.params[2].value = value

	def lBeatDelay(self,value):
		self.params[3].value = value

	def lBeatSwing(self,value):
		self.params[4].value = value

	def lTimeDelay(self,value):
		self.params[5].value = value

	def rDelayMode(self,value):
		self.params[6].value = value

	def rBeatDelay(self,value):
		self.params[7].value = value

	def rBeatSwing(self,value):
		self.params[8].value = value

	def rTimeDelay(self,value):
		self.params[9].value = value

	def feedback(self,value):
		self.params[10].value = value

	def dryWet(self,value):
		self.params[11].value = value

