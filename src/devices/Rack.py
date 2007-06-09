class Rack:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value):
		self.params[0].value = value

	def macro1(self,value):
		self.params[1].value = value

	def macro2(self,value):
		self.params[2].value = value

	def macro3(self,value):
		self.params[3].value = value

	def macro4(self,value):
		self.params[4].value = value

	def macro5(self,value):
		self.params[5].value = value

	def macro6(self,value):
		self.params[6].value = value

	def macro7(self,value):
		self.params[7].value = value

	def macro8(self,value):
		self.params[8].value = value

	def chainSelector(self,value):
		self.params[9].value = value

