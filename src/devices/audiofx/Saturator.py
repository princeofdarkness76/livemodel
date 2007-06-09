class Saturator:

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

	def type(self,value):
		self.params[4].value = value

	def base(self,value):
		self.params[5].value = value

	def color(self,value):
		self.params[6].value = value

	def frequency(self,value):
		self.params[7].value = value

	def width(self,value):
		self.params[8].value = value

	def depth(self,value):
		self.params[9].value = value

	def softClip(self,value):
		self.params[10].value = value

	def wsDrive(self,value):
		self.params[11].value = value

	def wsLin(self,value):
		self.params[12].value = value

	def wsCurve(self,value):
		self.params[13].value = value

	def wsDamp(self,value):
		self.params[14].value = value

	def wsPeriod(self,value):
		self.params[15].value = value

	def wsDepth(self,value):
		self.params[16].value = value

