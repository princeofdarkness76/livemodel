class Saturator:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value=None):
		if value != None:
			self.params[0].value = value
		return self.params[0].value

	def dryWet(self,value=None):
		if value != None:
			self.params[1].value = value
		return self.params[1].value

	def drive(self,value=None):
		if value != None:
			self.params[2].value = value
		return self.params[2].value

	def output(self,value=None):
		if value != None:
			self.params[3].value = value
		return self.params[3].value

	def type(self,value=None):
		if value != None:
			self.params[4].value = value
		return self.params[4].value

	def base(self,value=None):
		if value != None:
			self.params[5].value = value
		return self.params[5].value

	def color(self,value=None):
		if value != None:
			self.params[6].value = value
		return self.params[6].value

	def frequency(self,value=None):
		if value != None:
			self.params[7].value = value
		return self.params[7].value

	def width(self,value=None):
		if value != None:
			self.params[8].value = value
		return self.params[8].value

	def depth(self,value=None):
		if value != None:
			self.params[9].value = value
		return self.params[9].value

	def softClip(self,value=None):
		if value != None:
			self.params[10].value = value
		return self.params[10].value

	def wsDrive(self,value=None):
		if value != None:
			self.params[11].value = value
		return self.params[11].value

	def wsLin(self,value=None):
		if value != None:
			self.params[12].value = value
		return self.params[12].value

	def wsCurve(self,value=None):
		if value != None:
			self.params[13].value = value
		return self.params[13].value

	def wsDamp(self,value=None):
		if value != None:
			self.params[14].value = value
		return self.params[14].value

	def wsPeriod(self,value=None):
		if value != None:
			self.params[15].value = value
		return self.params[15].value

	def wsDepth(self,value=None):
		if value != None:
			self.params[16].value = value
		return self.params[16].value

