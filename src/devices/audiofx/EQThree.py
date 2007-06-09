class EQThree:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value=None):
		if value != None:
			self.params[0].value = value
		return self.params[0].value

	def gainlo(self,value=None):
		if value != None:
			self.params[1].value = value
		return self.params[1].value

	def gainmid(self,value=None):
		if value != None:
			self.params[2].value = value
		return self.params[2].value

	def gainhi(self,value=None):
		if value != None:
			self.params[3].value = value
		return self.params[3].value

	def freqlo(self,value=None):
		if value != None:
			self.params[4].value = value
		return self.params[4].value

	def freqhi(self,value=None):
		if value != None:
			self.params[5].value = value
		return self.params[5].value

	def lowon(self,value=None):
		if value != None:
			self.params[6].value = value
		return self.params[6].value

	def midon(self,value=None):
		if value != None:
			self.params[7].value = value
		return self.params[7].value

	def highon(self,value=None):
		if value != None:
			self.params[8].value = value
		return self.params[8].value

	def slope(self,value=None):
		if value != None:
			self.params[9].value = value
		return self.params[9].value

