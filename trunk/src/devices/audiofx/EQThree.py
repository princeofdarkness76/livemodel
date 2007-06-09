class EQThree:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value):
		self.params[0].value = value

	def gainlo(self,value):
		self.params[1].value = value

	def gainmid(self,value):
		self.params[2].value = value

	def gainhi(self,value):
		self.params[3].value = value

	def freqlo(self,value):
		self.params[4].value = value

	def freqhi(self,value):
		self.params[5].value = value

	def lowon(self,value):
		self.params[6].value = value

	def midon(self,value):
		self.params[7].value = value

	def highon(self,value):
		self.params[8].value = value

	def slope(self,value):
		self.params[9].value = value

