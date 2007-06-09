class Arpeggiator:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value):
		self.params[0].value = value

	def style(self,value):
		self.params[1].value = value

	def offset(self,value):
		self.params[2].value = value

	def repeats(self,value):
		self.params[3].value = value

	def syncOn(self,value):
		self.params[4].value = value

	def syncedRate(self,value):
		self.params[5].value = value

	def groove(self,value):
		self.params[6].value = value

	def freeRate(self,value):
		self.params[7].value = value

	def gate(self,value):
		self.params[8].value = value

	def retriggerMode(self,value):
		self.params[9].value = value

	def retInterval(self,value):
		self.params[10].value = value

	def holdOn(self,value):
		self.params[11].value = value

	def tranposeMode(self,value):
		self.params[12].value = value

	def tranposeKey(self,value):
		self.params[13].value = value

	def transpSteps(self,value):
		self.params[14].value = value

	def transpDist(self,value):
		self.params[15].value = value

	def velocityOn(self,value):
		self.params[16].value = value

	def velRetrigger(self,value):
		self.params[17].value = value

	def velocityDecay(self,value):
		self.params[18].value = value

	def velocityTarget(self,value):
		self.params[19].value = value

