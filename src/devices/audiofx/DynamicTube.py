class DynamicTube:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value):
		self.params[0].value = value

	def dryWet(self,value):
		self.params[1].value = value

	def drive(self,value):
		self.params[2].value = value

	def output(self,value):
		self.params[3].value = value

	def bias(self,value):
		self.params[4].value = value

	def envelope(self,value):
		self.params[5].value = value

	def attack(self,value):
		self.params[6].value = value

	def release(self,value):
		self.params[7].value = value

	def tone(self,value):
		self.params[8].value = value

	def tubeType(self,value):
		self.params[9].value = value

