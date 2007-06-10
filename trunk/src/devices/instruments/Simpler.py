from LiveModel import DeviceBase

class Simpler(DeviceBase):

	def __init__(self,device):
		DeviceBase.__init__(self, device)

	def getDeviceOn(self):
		return self.params[0].value

	def setDeviceOn(self,value):
		self.params[0].value = value

	deviceOn = property(getDeviceOn,setDeviceOn, doc='0 : Device On (0.0,1.0:Q)')

	def getSnap(self):
		return self.params[1].value

	def setSnap(self,value):
		self.params[1].value = value

	snap = property(getSnap,setSnap, doc='1 : Snap (0.0,1.0:Q)')

	def getSStart(self):
		return self.params[2].value

	def setSStart(self,value):
		self.params[2].value = value

	sStart = property(getSStart,setSStart, doc='2 : S Start (0.0,1.0)')

	def getSLength(self):
		return self.params[3].value

	def setSLength(self,value):
		self.params[3].value = value

	sLength = property(getSLength,setSLength, doc='3 : S Length (0.0,1.0)')

	def getSLoopOn(self):
		return self.params[4].value

	def setSLoopOn(self,value):
		self.params[4].value = value

	sLoopOn = property(getSLoopOn,setSLoopOn, doc='4 : S Loop On (0.0,1.0:Q)')

	def getSLoopLength(self):
		return self.params[5].value

	def setSLoopLength(self,value):
		self.params[5].value = value

	sLoopLength = property(getSLoopLength,setSLoopLength, doc='5 : S Loop Length (0.0,1.0)')

	def getSLoopFade(self):
		return self.params[6].value

	def setSLoopFade(self,value):
		self.params[6].value = value

	sLoopFade = property(getSLoopFade,setSLoopFade, doc='6 : S Loop Fade (0.0,1.0)')

	def getSpread(self):
		return self.params[7].value

	def setSpread(self,value):
		self.params[7].value = value

	spread = property(getSpread,setSpread, doc='7 : Spread (0.0,100.0)')

	def getGlideMode(self):
		return self.params[8].value

	def setGlideMode(self,value):
		self.params[8].value = value

	glideMode = property(getGlideMode,setGlideMode, doc='8 : Glide Mode (0.0,2.0:Q)')

	def getGlideTime(self):
		return self.params[9].value

	def setGlideTime(self,value):
		self.params[9].value = value

	glideTime = property(getGlideTime,setGlideTime, doc='9 : Glide Time (0.0,1.0)')

	def getTranspose(self):
		return self.params[10].value

	def setTranspose(self,value):
		self.params[10].value = value

	transpose = property(getTranspose,setTranspose, doc='10 : Transpose (-48.0,48.0)')

	def getDetune(self):
		return self.params[11].value

	def setDetune(self,value):
		self.params[11].value = value

	detune = property(getDetune,setDetune, doc='11 : Detune (-50.0,50.0)')

	def getLfoToPitch(self):
		return self.params[12].value

	def setLfoToPitch(self,value):
		self.params[12].value = value

	lfoToPitch = property(getLfoToPitch,setLfoToPitch, doc='12 : Pitch < LFO (0.0,1.0)')

	def getEnvToPe(self):
		return self.params[13].value

	def setEnvToPe(self,value):
		self.params[13].value = value

	envToPe = property(getEnvToPe,setEnvToPe, doc='13 : Pe < Env (-48.0,48.0)')

	def getPeAttack(self):
		return self.params[14].value

	def setPeAttack(self,value):
		self.params[14].value = value

	peAttack = property(getPeAttack,setPeAttack, doc='14 : Pe Attack (0.0,1.0)')

	def getPeDecay(self):
		return self.params[15].value

	def setPeDecay(self,value):
		self.params[15].value = value

	peDecay = property(getPeDecay,setPeDecay, doc='15 : Pe Decay (0.0,1.0)')

	def getPeSustain(self):
		return self.params[16].value

	def setPeSustain(self,value):
		self.params[16].value = value

	peSustain = property(getPeSustain,setPeSustain, doc='16 : Pe Sustain (-1.0,1.0)')

	def getPeRelease(self):
		return self.params[17].value

	def setPeRelease(self,value):
		self.params[17].value = value

	peRelease = property(getPeRelease,setPeRelease, doc='17 : Pe Release (0.0,1.0)')

	def getVolume(self):
		return self.params[18].value

	def setVolume(self,value):
		self.params[18].value = value

	volume = property(getVolume,setVolume, doc='18 : Volume (-36.0,36.0)')

	def getVelToVol(self):
		return self.params[19].value

	def setVelToVol(self,value):
		self.params[19].value = value

	velToVol = property(getVelToVol,setVelToVol, doc='19 : Vol < Vel (0.0,1.0)')

	def getLfoToVol(self):
		return self.params[20].value

	def setLfoToVol(self,value):
		self.params[20].value = value

	lfoToVol = property(getLfoToVol,setLfoToVol, doc='20 : Vol < LFO (0.0,1.0)')

	def getPan(self):
		return self.params[21].value

	def setPan(self,value):
		self.params[21].value = value

	pan = property(getPan,setPan, doc='21 : Pan (-1.0,1.0)')

	def getRndToPan(self):
		return self.params[22].value

	def setRndToPan(self,value):
		self.params[22].value = value

	rndToPan = property(getRndToPan,setRndToPan, doc='22 : Pan < Rnd (0.0,1.0)')

	def getLfoToPan(self):
		return self.params[23].value

	def setLfoToPan(self,value):
		self.params[23].value = value

	lfoToPan = property(getLfoToPan,setLfoToPan, doc='23 : Pan < LFO (0.0,1.0)')

	def getVeAttack(self):
		return self.params[24].value

	def setVeAttack(self,value):
		self.params[24].value = value

	veAttack = property(getVeAttack,setVeAttack, doc='24 : Ve Attack (0.0,1.0)')

	def getVeDecay(self):
		return self.params[25].value

	def setVeDecay(self,value):
		self.params[25].value = value

	veDecay = property(getVeDecay,setVeDecay, doc='25 : Ve Decay (0.0,1.0)')

	def getVeSustain(self):
		return self.params[26].value

	def setVeSustain(self,value):
		self.params[26].value = value

	veSustain = property(getVeSustain,setVeSustain, doc='26 : Ve Sustain (0.0,1.0)')

	def getVeRelease(self):
		return self.params[27].value

	def setVeRelease(self,value):
		self.params[27].value = value

	veRelease = property(getVeRelease,setVeRelease, doc='27 : Ve Release (0.0,1.0)')

	def getFilterOn(self):
		return self.params[28].value

	def setFilterOn(self,value):
		self.params[28].value = value

	filterOn = property(getFilterOn,setFilterOn, doc='28 : Filter On (0.0,1.0:Q)')

	def getFilterType(self):
		return self.params[29].value

	def setFilterType(self,value):
		self.params[29].value = value

	filterType = property(getFilterType,setFilterType, doc='29 : Filter Type (0.0,6.0:Q)')

	def getFilterFreq(self):
		return self.params[30].value

	def setFilterFreq(self,value):
		self.params[30].value = value

	filterFreq = property(getFilterFreq,setFilterFreq, doc='30 : Filter Freq (0.0,1.0)')

	def getFilterRes(self):
		return self.params[31].value

	def setFilterRes(self,value):
		self.params[31].value = value

	filterRes = property(getFilterRes,setFilterRes, doc='31 : Filter Res (0.0,1.0)')

	def getEnvToFe(self):
		return self.params[32].value

	def setEnvToFe(self,value):
		self.params[32].value = value

	envToFe = property(getEnvToFe,setEnvToFe, doc='32 : Fe < Env (-72.0,72.0)')

	def getFeAttack(self):
		return self.params[33].value

	def setFeAttack(self,value):
		self.params[33].value = value

	feAttack = property(getFeAttack,setFeAttack, doc='33 : Fe Attack (0.0,1.0)')

	def getFeDecay(self):
		return self.params[34].value

	def setFeDecay(self,value):
		self.params[34].value = value

	feDecay = property(getFeDecay,setFeDecay, doc='34 : Fe Decay (0.0,1.0)')

	def getFeSustain(self):
		return self.params[35].value

	def setFeSustain(self,value):
		self.params[35].value = value

	feSustain = property(getFeSustain,setFeSustain, doc='35 : Fe Sustain (0.0,1.0)')

	def getFeRelease(self):
		return self.params[36].value

	def setFeRelease(self,value):
		self.params[36].value = value

	feRelease = property(getFeRelease,setFeRelease, doc='36 : Fe Release (0.0,1.0)')

	def getKeyToFilt(self):
		return self.params[37].value

	def setKeyToFilt(self,value):
		self.params[37].value = value

	keyToFilt = property(getKeyToFilt,setKeyToFilt, doc='37 : Filt < Key (0.0,1.0)')

	def getVelToFilt(self):
		return self.params[38].value

	def setVelToFilt(self,value):
		self.params[38].value = value

	velToFilt = property(getVelToFilt,setVelToFilt, doc='38 : Filt < Vel (0.0,1.0)')

	def getLfoToFilt(self):
		return self.params[39].value

	def setLfoToFilt(self,value):
		self.params[39].value = value

	lfoToFilt = property(getLfoToFilt,setLfoToFilt, doc='39 : Filt < LFO (0.0,24.0)')

	def getLOn(self):
		return self.params[40].value

	def setLOn(self,value):
		self.params[40].value = value

	lOn = property(getLOn,setLOn, doc='40 : L On (0.0,1.0:Q)')

	def getLWave(self):
		return self.params[41].value

	def setLWave(self,value):
		self.params[41].value = value

	lWave = property(getLWave,setLWave, doc='41 : L Wave (0.0,5.0:Q)')

	def getLSync(self):
		return self.params[42].value

	def setLSync(self,value):
		self.params[42].value = value

	lSync = property(getLSync,setLSync, doc='42 : L Sync (0.0,1.0:Q)')

	def getLRate(self):
		return self.params[43].value

	def setLRate(self,value):
		self.params[43].value = value

	lRate = property(getLRate,setLRate, doc='43 : L Rate (0.0,1.0)')

	def getLSyncRate(self):
		return self.params[44].value

	def setLSyncRate(self,value):
		self.params[44].value = value

	lSyncRate = property(getLSyncRate,setLSyncRate, doc='44 : L Sync Rate (0.0,21.0)')

	def getLKeyToR(self):
		return self.params[45].value

	def setLKeyToR(self,value):
		self.params[45].value = value

	lKeyToR = property(getLKeyToR,setLKeyToR, doc='45 : L R < Key (0.0,1.0)')

	def getLAttack(self):
		return self.params[46].value

	def setLAttack(self,value):
		self.params[46].value = value

	lAttack = property(getLAttack,setLAttack, doc='46 : L Attack (0.0,1.0)')

	def getLRetrig(self):
		return self.params[47].value

	def setLRetrig(self,value):
		self.params[47].value = value

	lRetrig = property(getLRetrig,setLRetrig, doc='47 : L Retrig (0.0,1.0:Q)')

	def getLOffset(self):
		return self.params[48].value

	def setLOffset(self,value):
		self.params[48].value = value

	lOffset = property(getLOffset,setLOffset, doc='48 : L Offset (0.0,360.0)')

