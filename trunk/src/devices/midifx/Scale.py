class Scale:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value):
		self.params[0].value = value

	def base(self,value):
		self.params[1].value = value

	def transpose(self,value):
		self.params[2].value = value

	def fold(self,value):
		self.params[3].value = value

	def lowest(self,value):
		self.params[4].value = value

	def range(self,value):
		self.params[5].value = value

	def map0(self,value):
		self.params[6].value = value

	def map1(self,value):
		self.params[7].value = value

	def map2(self,value):
		self.params[8].value = value

	def map3(self,value):
		self.params[9].value = value

	def map4(self,value):
		self.params[10].value = value

	def map5(self,value):
		self.params[11].value = value

	def map6(self,value):
		self.params[12].value = value

	def map7(self,value):
		self.params[13].value = value

	def map8(self,value):
		self.params[14].value = value

	def map9(self,value):
		self.params[15].value = value

	def map10(self,value):
		self.params[16].value = value

	def map11(self,value):
		self.params[17].value = value

