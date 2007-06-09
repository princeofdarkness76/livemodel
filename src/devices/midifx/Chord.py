class Chord:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value=None):
		if value != None:
			self.params[0].value = value
		return self.params[0].value

	def shift1(self,value=None):
		if value != None:
			self.params[1].value = value
		return self.params[1].value

	def velocity1(self,value=None):
		if value != None:
			self.params[2].value = value
		return self.params[2].value

	def shift2(self,value=None):
		if value != None:
			self.params[3].value = value
		return self.params[3].value

	def velocity2(self,value=None):
		if value != None:
			self.params[4].value = value
		return self.params[4].value

	def shift3(self,value=None):
		if value != None:
			self.params[5].value = value
		return self.params[5].value

	def velocity3(self,value=None):
		if value != None:
			self.params[6].value = value
		return self.params[6].value

	def shift4(self,value=None):
		if value != None:
			self.params[7].value = value
		return self.params[7].value

	def velocity4(self,value=None):
		if value != None:
			self.params[8].value = value
		return self.params[8].value

	def shift5(self,value=None):
		if value != None:
			self.params[9].value = value
		return self.params[9].value

	def velocity5(self,value=None):
		if value != None:
			self.params[10].value = value
		return self.params[10].value

	def shift6(self,value=None):
		if value != None:
			self.params[11].value = value
		return self.params[11].value

	def velocity6(self,value=None):
		if value != None:
			self.params[12].value = value
		return self.params[12].value

