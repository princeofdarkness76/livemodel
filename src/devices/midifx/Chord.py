class Chord:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value):
		self.params[0].value = value

	def shift1(self,value):
		self.params[1].value = value

	def velocity1(self,value):
		self.params[2].value = value

	def shift2(self,value):
		self.params[3].value = value

	def velocity2(self,value):
		self.params[4].value = value

	def shift3(self,value):
		self.params[5].value = value

	def velocity3(self,value):
		self.params[6].value = value

	def shift4(self,value):
		self.params[7].value = value

	def velocity4(self,value):
		self.params[8].value = value

	def shift5(self,value):
		self.params[9].value = value

	def velocity5(self,value):
		self.params[10].value = value

	def shift6(self,value):
		self.params[11].value = value

	def velocity6(self,value):
		self.params[12].value = value

