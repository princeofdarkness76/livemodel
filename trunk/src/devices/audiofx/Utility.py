class Utility:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value):
		self.params[0].value = value

	def gain(self,value):
		self.params[1].value = value

	def panorama(self,value):
		self.params[2].value = value

	def signalSource(self,value):
		self.params[3].value = value

	def stereoseparation(self,value):
		self.params[4].value = value

	def phaseinvertl(self,value):
		self.params[5].value = value

	def phaseinvertr(self,value):
		self.params[6].value = value

	def mute(self,value):
		self.params[7].value = value

	def blockdc(self,value):
		self.params[8].value = value

