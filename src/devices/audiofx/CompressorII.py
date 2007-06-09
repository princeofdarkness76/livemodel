class CompressorII:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value):
		self.params[0].value = value

	def threshold(self,value):
		self.params[1].value = value

	def ratio(self,value):
		self.params[2].value = value

	def attack(self,value):
		self.params[3].value = value

	def release(self,value):
		self.params[4].value = value

	def outputGain(self,value):
		self.params[5].value = value

	def freq(self,value):
		self.params[6].value = value

	def sidegain(self,value):
		self.params[7].value = value

	def sideon(self,value):
		self.params[8].value = value

	def peakon(self,value):
		self.params[9].value = value

	def lookahead(self,value):
		self.params[10].value = value

	def sidemode(self,value):
		self.params[11].value = value

