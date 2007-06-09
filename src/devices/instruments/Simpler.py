class Simpler:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value=None):
		if value != None:
			self.params[0].value = value
		return self.params[0].value

	def snap(self,value=None):
		if value != None:
			self.params[1].value = value
		return self.params[1].value

	def sStart(self,value=None):
		if value != None:
			self.params[2].value = value
		return self.params[2].value

	def sLength(self,value=None):
		if value != None:
			self.params[3].value = value
		return self.params[3].value

	def sLoopOn(self,value=None):
		if value != None:
			self.params[4].value = value
		return self.params[4].value

	def sLoopLength(self,value=None):
		if value != None:
			self.params[5].value = value
		return self.params[5].value

	def sLoopFade(self,value=None):
		if value != None:
			self.params[6].value = value
		return self.params[6].value

	def spread(self,value=None):
		if value != None:
			self.params[7].value = value
		return self.params[7].value

	def glideMode(self,value=None):
		if value != None:
			self.params[8].value = value
		return self.params[8].value

	def glideTime(self,value=None):
		if value != None:
			self.params[9].value = value
		return self.params[9].value

	def transpose(self,value=None):
		if value != None:
			self.params[10].value = value
		return self.params[10].value

	def detune(self,value=None):
		if value != None:
			self.params[11].value = value
		return self.params[11].value

	def pitchToLfo(self,value=None):
		if value != None:
			self.params[12].value = value
		return self.params[12].value

	def peToEnv(self,value=None):
		if value != None:
			self.params[13].value = value
		return self.params[13].value

	def peAttack(self,value=None):
		if value != None:
			self.params[14].value = value
		return self.params[14].value

	def peDecay(self,value=None):
		if value != None:
			self.params[15].value = value
		return self.params[15].value

	def peSustain(self,value=None):
		if value != None:
			self.params[16].value = value
		return self.params[16].value

	def peRelease(self,value=None):
		if value != None:
			self.params[17].value = value
		return self.params[17].value

	def volume(self,value=None):
		if value != None:
			self.params[18].value = value
		return self.params[18].value

	def volToVel(self,value=None):
		if value != None:
			self.params[19].value = value
		return self.params[19].value

	def volToLfo(self,value=None):
		if value != None:
			self.params[20].value = value
		return self.params[20].value

	def pan(self,value=None):
		if value != None:
			self.params[21].value = value
		return self.params[21].value

	def panToRnd(self,value=None):
		if value != None:
			self.params[22].value = value
		return self.params[22].value

	def panToLfo(self,value=None):
		if value != None:
			self.params[23].value = value
		return self.params[23].value

	def veAttack(self,value=None):
		if value != None:
			self.params[24].value = value
		return self.params[24].value

	def veDecay(self,value=None):
		if value != None:
			self.params[25].value = value
		return self.params[25].value

	def veSustain(self,value=None):
		if value != None:
			self.params[26].value = value
		return self.params[26].value

	def veRelease(self,value=None):
		if value != None:
			self.params[27].value = value
		return self.params[27].value

	def filterOn(self,value=None):
		if value != None:
			self.params[28].value = value
		return self.params[28].value

	def filterType(self,value=None):
		if value != None:
			self.params[29].value = value
		return self.params[29].value

	def filterFreq(self,value=None):
		if value != None:
			self.params[30].value = value
		return self.params[30].value

	def filterRes(self,value=None):
		if value != None:
			self.params[31].value = value
		return self.params[31].value

	def feToEnv(self,value=None):
		if value != None:
			self.params[32].value = value
		return self.params[32].value

	def feAttack(self,value=None):
		if value != None:
			self.params[33].value = value
		return self.params[33].value

	def feDecay(self,value=None):
		if value != None:
			self.params[34].value = value
		return self.params[34].value

	def feSustain(self,value=None):
		if value != None:
			self.params[35].value = value
		return self.params[35].value

	def feRelease(self,value=None):
		if value != None:
			self.params[36].value = value
		return self.params[36].value

	def filtToKey(self,value=None):
		if value != None:
			self.params[37].value = value
		return self.params[37].value

	def filtToVel(self,value=None):
		if value != None:
			self.params[38].value = value
		return self.params[38].value

	def filtToLfo(self,value=None):
		if value != None:
			self.params[39].value = value
		return self.params[39].value

	def lOn(self,value=None):
		if value != None:
			self.params[40].value = value
		return self.params[40].value

	def lWave(self,value=None):
		if value != None:
			self.params[41].value = value
		return self.params[41].value

	def lSync(self,value=None):
		if value != None:
			self.params[42].value = value
		return self.params[42].value

	def lRate(self,value=None):
		if value != None:
			self.params[43].value = value
		return self.params[43].value

	def lSyncRate(self,value=None):
		if value != None:
			self.params[44].value = value
		return self.params[44].value

	def lRToKey(self,value=None):
		if value != None:
			self.params[45].value = value
		return self.params[45].value

	def lAttack(self,value=None):
		if value != None:
			self.params[46].value = value
		return self.params[46].value

	def lRetrig(self,value=None):
		if value != None:
			self.params[47].value = value
		return self.params[47].value

	def lOffset(self,value=None):
		if value != None:
			self.params[48].value = value
		return self.params[48].value

