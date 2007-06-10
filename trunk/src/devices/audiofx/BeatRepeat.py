class BeatRepeat:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def getDeviceOn(self):
		return self.params[0].value

	def setDeviceOn(self,value):
		self.params[0].value = value

	deviceOn = property(getDeviceOn,setDeviceOn, doc='0 : Device On (0.0,1.0:Q)')

	def getChance(self):
		return self.params[1].value

	def setChance(self,value):
		self.params[1].value = value

	chance = property(getChance,setChance, doc='1 : Chance (0.0,1.0)')

	def getInterval(self):
		return self.params[2].value

	def setInterval(self,value):
		self.params[2].value = value

	interval = property(getInterval,setInterval, doc='2 : Interval (0.0,7.0)')

	def getOffset(self):
		return self.params[3].value

	def setOffset(self,value):
		self.params[3].value = value

	offset = property(getOffset,setOffset, doc='3 : Offset (0.0,15.0)')

	def getGrid(self):
		return self.params[4].value

	def setGrid(self,value):
		self.params[4].value = value

	grid = property(getGrid,setGrid, doc='4 : Grid (0.0,15.0)')

	def getBlockTriplets(self):
		return self.params[5].value

	def setBlockTriplets(self,value):
		self.params[5].value = value

	blockTriplets = property(getBlockTriplets,setBlockTriplets, doc='5 : Block Triplets (0.0,1.0:Q)')

	def getVariation(self):
		return self.params[6].value

	def setVariation(self,value):
		self.params[6].value = value

	variation = property(getVariation,setVariation, doc='6 : Variation (0.0,10.0)')

	def getVariationType(self):
		return self.params[7].value

	def setVariationType(self,value):
		self.params[7].value = value

	variationType = property(getVariationType,setVariationType, doc='7 : Variation Type (0.0,4.0:Q)')

	def getGate(self):
		return self.params[8].value

	def setGate(self,value):
		self.params[8].value = value

	gate = property(getGate,setGate, doc='8 : Gate (0.0,18.0)')

	def getDecay(self):
		return self.params[9].value

	def setDecay(self,value):
		self.params[9].value = value

	decay = property(getDecay,setDecay, doc='9 : Decay (0.0,1.0)')

	def getPitchDecay(self):
		return self.params[10].value

	def setPitchDecay(self,value):
		self.params[10].value = value

	pitchDecay = property(getPitchDecay,setPitchDecay, doc='10 : Pitch Decay (0.0,1.0)')

	def getPitch(self):
		return self.params[11].value

	def setPitch(self,value):
		self.params[11].value = value

	pitch = property(getPitch,setPitch, doc='11 : Pitch (0.0,12.0)')

	def getMixType(self):
		return self.params[12].value

	def setMixType(self,value):
		self.params[12].value = value

	mixType = property(getMixType,setMixType, doc='12 : Mix Type (0.0,2.0:Q)')

	def getVolume(self):
		return self.params[13].value

	def setVolume(self,value):
		self.params[13].value = value

	volume = property(getVolume,setVolume, doc='13 : Volume (0.0,1.0)')

	def getFilterOn(self):
		return self.params[14].value

	def setFilterOn(self,value):
		self.params[14].value = value

	filterOn = property(getFilterOn,setFilterOn, doc='14 : Filter On (0.0,1.0:Q)')

	def getMidFreq(self):
		return self.params[15].value

	def setMidFreq(self,value):
		self.params[15].value = value

	midFreq = property(getMidFreq,setMidFreq, doc='15 : Mid Freq (0.0,1.0)')

	def getEqWidth(self):
		return self.params[16].value

	def setEqWidth(self,value):
		self.params[16].value = value

	eqWidth = property(getEqWidth,setEqWidth, doc='16 : EQ Width (0.5,9.0)')

	def getRepeat(self):
		return self.params[17].value

	def setRepeat(self,value):
		self.params[17].value = value

	repeat = property(getRepeat,setRepeat, doc='17 : Repeat (0.0,1.0:Q)')

