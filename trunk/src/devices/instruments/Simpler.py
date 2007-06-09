class Simpler:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value):
		self.params[0].value = value

	def snap(self,value):
		self.params[1].value = value

	def sStart(self,value):
		self.params[2].value = value

	def sLength(self,value):
		self.params[3].value = value

	def sLoopOn(self,value):
		self.params[4].value = value

	def sLoopLength(self,value):
		self.params[5].value = value

	def sLoopFade(self,value):
		self.params[6].value = value

	def spread(self,value):
		self.params[7].value = value

	def glideMode(self,value):
		self.params[8].value = value

	def glideTime(self,value):
		self.params[9].value = value

	def transpose(self,value):
		self.params[10].value = value

	def detune(self,value):
		self.params[11].value = value

	def pitchToLfo(self,value):
		self.params[12].value = value

	def peToEnv(self,value):
		self.params[13].value = value

	def peAttack(self,value):
		self.params[14].value = value

	def peDecay(self,value):
		self.params[15].value = value

	def peSustain(self,value):
		self.params[16].value = value

	def peRelease(self,value):
		self.params[17].value = value

	def volume(self,value):
		self.params[18].value = value

	def volToVel(self,value):
		self.params[19].value = value

	def volToLfo(self,value):
		self.params[20].value = value

	def pan(self,value):
		self.params[21].value = value

	def panToRnd(self,value):
		self.params[22].value = value

	def panToLfo(self,value):
		self.params[23].value = value

	def veAttack(self,value):
		self.params[24].value = value

	def veDecay(self,value):
		self.params[25].value = value

	def veSustain(self,value):
		self.params[26].value = value

	def veRelease(self,value):
		self.params[27].value = value

	def filterOn(self,value):
		self.params[28].value = value

	def filterType(self,value):
		self.params[29].value = value

	def filterFreq(self,value):
		self.params[30].value = value

	def filterRes(self,value):
		self.params[31].value = value

	def feToEnv(self,value):
		self.params[32].value = value

	def feAttack(self,value):
		self.params[33].value = value

	def feDecay(self,value):
		self.params[34].value = value

	def feSustain(self,value):
		self.params[35].value = value

	def feRelease(self,value):
		self.params[36].value = value

	def filtToKey(self,value):
		self.params[37].value = value

	def filtToVel(self,value):
		self.params[38].value = value

	def filtToLfo(self,value):
		self.params[39].value = value

	def lOn(self,value):
		self.params[40].value = value

	def lWave(self,value):
		self.params[41].value = value

	def lSync(self,value):
		self.params[42].value = value

	def lRate(self,value):
		self.params[43].value = value

	def lSyncRate(self,value):
		self.params[44].value = value

	def lRToKey(self,value):
		self.params[45].value = value

	def lAttack(self,value):
		self.params[46].value = value

	def lRetrig(self,value):
		self.params[47].value = value

	def lOffset(self,value):
		self.params[48].value = value

