class AutoPan:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value):
		self.params[0].value = value

	def lfoType(self,value):
		self.params[1].value = value

	def amount(self,value):
		self.params[2].value = value

	def frequency(self,value):
		self.params[3].value = value

	def syncRate(self,value):
		self.params[4].value = value

	def phase(self,value):
		self.params[5].value = value

	def spin(self,value):
		self.params[6].value = value

	def stereoMode(self,value):
		self.params[7].value = value

	def offset(self,value):
		self.params[8].value = value

	def waveform(self,value):
		self.params[9].value = value

	def shape(self,value):
		self.params[10].value = value

	def widthRandom(self,value):
		self.params[11].value = value

	def invert(self,value):
		self.params[12].value = value

