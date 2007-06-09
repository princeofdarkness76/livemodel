class AutoFilter:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value):
		self.params[0].value = value

	def filterType(self,value):
		self.params[1].value = value

	def frequency(self,value):
		self.params[2].value = value

	def resonance(self,value):
		self.params[3].value = value

	def envModulation(self,value):
		self.params[4].value = value

	def envAttack(self,value):
		self.params[5].value = value

	def envRelease(self,value):
		self.params[6].value = value

	def lfoAmount(self,value):
		self.params[7].value = value

	def lfoWaveform(self,value):
		self.params[8].value = value

	def lfoFrequency(self,value):
		self.params[9].value = value

	def lfoSync(self,value):
		self.params[10].value = value

	def lfoSyncRate(self,value):
		self.params[11].value = value

	def lfoStereoMode(self,value):
		self.params[12].value = value

	def lfoSpin(self,value):
		self.params[13].value = value

	def lfoPhase(self,value):
		self.params[14].value = value

	def lfoOffset(self,value):
		self.params[15].value = value

	def lfoQuantizeOn(self,value):
		self.params[16].value = value

	def lfoQuantizeRate(self,value):
		self.params[17].value = value

