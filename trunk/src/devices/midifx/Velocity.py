class Velocity:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value):
		self.params[0].value = value

	def drive(self,value):
		self.params[1].value = value

	def compand(self,value):
		self.params[2].value = value

	def random(self,value):
		self.params[3].value = value

	def mode(self,value):
		self.params[4].value = value

	def operation(self,value):
		self.params[5].value = value

	def outHi(self,value):
		self.params[6].value = value

	def outLow(self,value):
		self.params[7].value = value

	def range(self,value):
		self.params[8].value = value

	def lowest(self,value):
		self.params[9].value = value

