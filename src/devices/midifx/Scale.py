class Scale:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value=None):
		if value != None:
			self.params[0].value = value
		return self.params[0].value

	def base(self,value=None):
		if value != None:
			self.params[1].value = value
		return self.params[1].value

	def transpose(self,value=None):
		if value != None:
			self.params[2].value = value
		return self.params[2].value

	def fold(self,value=None):
		if value != None:
			self.params[3].value = value
		return self.params[3].value

	def lowest(self,value=None):
		if value != None:
			self.params[4].value = value
		return self.params[4].value

	def range(self,value=None):
		if value != None:
			self.params[5].value = value
		return self.params[5].value

	def map0(self,value=None):
		if value != None:
			self.params[6].value = value
		return self.params[6].value

	def map1(self,value=None):
		if value != None:
			self.params[7].value = value
		return self.params[7].value

	def map2(self,value=None):
		if value != None:
			self.params[8].value = value
		return self.params[8].value

	def map3(self,value=None):
		if value != None:
			self.params[9].value = value
		return self.params[9].value

	def map4(self,value=None):
		if value != None:
			self.params[10].value = value
		return self.params[10].value

	def map5(self,value=None):
		if value != None:
			self.params[11].value = value
		return self.params[11].value

	def map6(self,value=None):
		if value != None:
			self.params[12].value = value
		return self.params[12].value

	def map7(self,value=None):
		if value != None:
			self.params[13].value = value
		return self.params[13].value

	def map8(self,value=None):
		if value != None:
			self.params[14].value = value
		return self.params[14].value

	def map9(self,value=None):
		if value != None:
			self.params[15].value = value
		return self.params[15].value

	def map10(self,value=None):
		if value != None:
			self.params[16].value = value
		return self.params[16].value

	def map11(self,value=None):
		if value != None:
			self.params[17].value = value
		return self.params[17].value

