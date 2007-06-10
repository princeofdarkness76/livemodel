class Operator:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def getDeviceOn(self):
		return self.params[0].value

	def setDeviceOn(self,value):
		self.params[0].value = value

	deviceOn = property(getDeviceOn,setDeviceOn, doc='0 : Device On (0.0,1.0:Q)')

	def getAlgorithm(self):
		return self.params[1].value

	def setAlgorithm(self,value):
		self.params[1].value = value

	algorithm = property(getAlgorithm,setAlgorithm, doc='1 : Algorithm (0.0,10.0:Q)')

	def getHiq(self):
		return self.params[2].value

	def setHiq(self,value):
		self.params[2].value = value

	hiq = property(getHiq,setHiq, doc='2 : HiQ (0.0,1.0:Q)')

	def getTranspose(self):
		return self.params[3].value

	def setTranspose(self,value):
		self.params[3].value = value

	transpose = property(getTranspose,setTranspose, doc='3 : Transpose (-48.0,48.0)')

	def getPbRange(self):
		return self.params[4].value

	def setPbRange(self,value):
		self.params[4].value = value

	pbRange = property(getPbRange,setPbRange, doc='4 : PB Range (0.0,24.0)')

	def getVolume(self):
		return self.params[5].value

	def setVolume(self,value):
		self.params[5].value = value

	volume = property(getVolume,setVolume, doc='5 : Volume (0.0,1.0)')

	def getPanorama(self):
		return self.params[6].value

	def setPanorama(self,value):
		self.params[6].value = value

	panorama = property(getPanorama,setPanorama, doc='6 : Panorama (-1.0,1.0)')

	def getKeyToPan(self):
		return self.params[7].value

	def setKeyToPan(self,value):
		self.params[7].value = value

	keyToPan = property(getKeyToPan,setKeyToPan, doc='7 : Pan < Key (0.0,100.0)')

	def getRndToPan(self):
		return self.params[8].value

	def setRndToPan(self,value):
		self.params[8].value = value

	rndToPan = property(getRndToPan,setRndToPan, doc='8 : Pan < Rnd (0.0,100.0)')

	def getDFeedback(self):
		return self.params[9].value

	def setDFeedback(self,value):
		self.params[9].value = value

	dFeedback = property(getDFeedback,setDFeedback, doc='9 : D Feedback (0.0,100.0)')

	def getTone(self):
		return self.params[10].value

	def setTone(self,value):
		self.params[10].value = value

	tone = property(getTone,setTone, doc='10 : Tone (0.0,1.0)')

	def getSpread(self):
		return self.params[11].value

	def setSpread(self,value):
		self.params[11].value = value

	spread = property(getSpread,setSpread, doc='11 : Spread (0.0,100.0)')

	def getGlideOn(self):
		return self.params[12].value

	def setGlideOn(self,value):
		self.params[12].value = value

	glideOn = property(getGlideOn,setGlideOn, doc='12 : Glide On (0.0,1.0:Q)')

	def getGlideTime(self):
		return self.params[13].value

	def setGlideTime(self,value):
		self.params[13].value = value

	glideTime = property(getGlideTime,setGlideTime, doc='13 : Glide Time (0.0,1.0)')

	def getAOn(self):
		return self.params[14].value

	def setAOn(self,value):
		self.params[14].value = value

	aOn = property(getAOn,setAOn, doc='14 : A On (0.0,1.0:Q)')

	def getACoarse(self):
		return self.params[15].value

	def setACoarse(self,value):
		self.params[15].value = value

	aCoarse = property(getACoarse,setACoarse, doc='15 : A Coarse (0.0,48.0)')

	def getAFine(self):
		return self.params[16].value

	def setAFine(self,value):
		self.params[16].value = value

	aFine = property(getAFine,setAFine, doc='16 : A Fine (0.0,1000.0)')

	def getAVelToFreq(self):
		return self.params[17].value

	def setAVelToFreq(self,value):
		self.params[17].value = value

	aVelToFreq = property(getAVelToFreq,setAVelToFreq, doc='17 : A Freq<Vel (-100.0,100.0)')

	def getAQuantize(self):
		return self.params[18].value

	def setAQuantize(self,value):
		self.params[18].value = value

	aQuantize = property(getAQuantize,setAQuantize, doc='18 : A Quantize (0.0,1.0:Q)')

	def getAFixOn(self):
		return self.params[19].value

	def setAFixOn(self,value):
		self.params[19].value = value

	aFixOn = property(getAFixOn,setAFixOn, doc='19 : A Fix On  (0.0,1.0:Q)')

	def getAFixFreq(self):
		return self.params[20].value

	def setAFixFreq(self,value):
		self.params[20].value = value

	aFixFreq = property(getAFixFreq,setAFixFreq, doc='20 : A Fix Freq (0.0,1.0)')

	def getAFixFreqMul(self):
		return self.params[21].value

	def setAFixFreqMul(self,value):
		self.params[21].value = value

	aFixFreqMul = property(getAFixFreqMul,setAFixFreqMul, doc='21 : A Fix Freq Mul (0.0,5.0)')

	def getALevel(self):
		return self.params[22].value

	def setALevel(self,value):
		self.params[22].value = value

	aLevel = property(getALevel,setALevel, doc='22 : A Level (0.0,1.0)')

	def getAPhase(self):
		return self.params[23].value

	def setAPhase(self,value):
		self.params[23].value = value

	aPhase = property(getAPhase,setAPhase, doc='23 : A Phase (0.0,100.0)')

	def getPeToOsca(self):
		return self.params[24].value

	def setPeToOsca(self,value):
		self.params[24].value = value

	peToOsca = property(getPeToOsca,setPeToOsca, doc='24 : Pe to Osc-A (0.0,1.0:Q)')

	def getAVelToLev(self):
		return self.params[25].value

	def setAVelToLev(self,value):
		self.params[25].value = value

	aVelToLev = property(getAVelToLev,setAVelToLev, doc='25 : A Lev < Vel (-100.0,100.0)')

	def getAKeyToLev(self):
		return self.params[26].value

	def setAKeyToLev(self,value):
		self.params[26].value = value

	aKeyToLev = property(getAKeyToLev,setAKeyToLev, doc='26 : A Lev < Key (-100.0,100.0)')

	def getAWave(self):
		return self.params[27].value

	def setAWave(self,value):
		self.params[27].value = value

	aWave = property(getAWave,setAWave, doc='27 : A Wave (0.0,25.0:Q)')

	def getLfoToOsca(self):
		return self.params[28].value

	def setLfoToOsca(self,value):
		self.params[28].value = value

	lfoToOsca = property(getLfoToOsca,setLfoToOsca, doc='28 : LFO to Osc-A (0.0,1.0:Q)')

	def getAeAttack(self):
		return self.params[29].value

	def setAeAttack(self,value):
		self.params[29].value = value

	aeAttack = property(getAeAttack,setAeAttack, doc='29 : Ae Attack (0.0,1.0)')

	def getAeInit(self):
		return self.params[30].value

	def setAeInit(self,value):
		self.params[30].value = value

	aeInit = property(getAeInit,setAeInit, doc='30 : Ae Init (0.0,1.0)')

	def getAeDecay(self):
		return self.params[31].value

	def setAeDecay(self,value):
		self.params[31].value = value

	aeDecay = property(getAeDecay,setAeDecay, doc='31 : Ae Decay (0.0,1.0)')

	def getAePeak(self):
		return self.params[32].value

	def setAePeak(self,value):
		self.params[32].value = value

	aePeak = property(getAePeak,setAePeak, doc='32 : Ae Peak (0.0,1.0)')

	def getAeSustain(self):
		return self.params[33].value

	def setAeSustain(self,value):
		self.params[33].value = value

	aeSustain = property(getAeSustain,setAeSustain, doc='33 : Ae Sustain (0.0,1.0)')

	def getAeRelease(self):
		return self.params[34].value

	def setAeRelease(self,value):
		self.params[34].value = value

	aeRelease = property(getAeRelease,setAeRelease, doc='34 : Ae Release (0.0,1.0)')

	def getAeMode(self):
		return self.params[35].value

	def setAeMode(self,value):
		self.params[35].value = value

	aeMode = property(getAeMode,setAeMode, doc='35 : Ae Mode (0.0,3.0:Q)')

	def getAeLoop(self):
		return self.params[36].value

	def setAeLoop(self,value):
		self.params[36].value = value

	aeLoop = property(getAeLoop,setAeLoop, doc='36 : Ae Loop (0.0,1.0)')

	def getAeRetrig(self):
		return self.params[37].value

	def setAeRetrig(self,value):
		self.params[37].value = value

	aeRetrig = property(getAeRetrig,setAeRetrig, doc='37 : Ae Retrig (0.0,14.0)')

	def getAeVelToR(self):
		return self.params[38].value

	def setAeVelToR(self,value):
		self.params[38].value = value

	aeVelToR = property(getAeVelToR,setAeVelToR, doc='38 : Ae R < Vel (-100.0,100.0)')

	def getBOn(self):
		return self.params[39].value

	def setBOn(self,value):
		self.params[39].value = value

	bOn = property(getBOn,setBOn, doc='39 : B On (0.0,1.0:Q)')

	def getBCoarse(self):
		return self.params[40].value

	def setBCoarse(self,value):
		self.params[40].value = value

	bCoarse = property(getBCoarse,setBCoarse, doc='40 : B Coarse (0.0,48.0)')

	def getBFine(self):
		return self.params[41].value

	def setBFine(self,value):
		self.params[41].value = value

	bFine = property(getBFine,setBFine, doc='41 : B Fine (0.0,1000.0)')

	def getBVelToFreq(self):
		return self.params[42].value

	def setBVelToFreq(self,value):
		self.params[42].value = value

	bVelToFreq = property(getBVelToFreq,setBVelToFreq, doc='42 : B Freq<Vel (-100.0,100.0)')

	def getBQuantize(self):
		return self.params[43].value

	def setBQuantize(self,value):
		self.params[43].value = value

	bQuantize = property(getBQuantize,setBQuantize, doc='43 : B Quantize (0.0,1.0:Q)')

	def getBFixOn(self):
		return self.params[44].value

	def setBFixOn(self,value):
		self.params[44].value = value

	bFixOn = property(getBFixOn,setBFixOn, doc='44 : B Fix On  (0.0,1.0:Q)')

	def getBFixFreq(self):
		return self.params[45].value

	def setBFixFreq(self,value):
		self.params[45].value = value

	bFixFreq = property(getBFixFreq,setBFixFreq, doc='45 : B Fix Freq (0.0,1.0)')

	def getBFixFreqMul(self):
		return self.params[46].value

	def setBFixFreqMul(self,value):
		self.params[46].value = value

	bFixFreqMul = property(getBFixFreqMul,setBFixFreqMul, doc='46 : B Fix Freq Mul (0.0,5.0)')

	def getBLevel(self):
		return self.params[47].value

	def setBLevel(self,value):
		self.params[47].value = value

	bLevel = property(getBLevel,setBLevel, doc='47 : B Level (0.0,1.0)')

	def getBPhase(self):
		return self.params[48].value

	def setBPhase(self,value):
		self.params[48].value = value

	bPhase = property(getBPhase,setBPhase, doc='48 : B Phase (0.0,100.0)')

	def getPeToOscb(self):
		return self.params[49].value

	def setPeToOscb(self,value):
		self.params[49].value = value

	peToOscb = property(getPeToOscb,setPeToOscb, doc='49 : Pe to Osc-B (0.0,1.0:Q)')

	def getBVelToLev(self):
		return self.params[50].value

	def setBVelToLev(self,value):
		self.params[50].value = value

	bVelToLev = property(getBVelToLev,setBVelToLev, doc='50 : B Lev < Vel (-100.0,100.0)')

	def getBKeyToLev(self):
		return self.params[51].value

	def setBKeyToLev(self,value):
		self.params[51].value = value

	bKeyToLev = property(getBKeyToLev,setBKeyToLev, doc='51 : B Lev < Key (-100.0,100.0)')

	def getBWave(self):
		return self.params[52].value

	def setBWave(self,value):
		self.params[52].value = value

	bWave = property(getBWave,setBWave, doc='52 : B Wave (0.0,25.0:Q)')

	def getLfoToOscb(self):
		return self.params[53].value

	def setLfoToOscb(self,value):
		self.params[53].value = value

	lfoToOscb = property(getLfoToOscb,setLfoToOscb, doc='53 : LFO to Osc-B (0.0,1.0:Q)')

	def getBeAttack(self):
		return self.params[54].value

	def setBeAttack(self,value):
		self.params[54].value = value

	beAttack = property(getBeAttack,setBeAttack, doc='54 : Be Attack (0.0,1.0)')

	def getBeInit(self):
		return self.params[55].value

	def setBeInit(self,value):
		self.params[55].value = value

	beInit = property(getBeInit,setBeInit, doc='55 : Be Init (0.0,1.0)')

	def getBeDecay(self):
		return self.params[56].value

	def setBeDecay(self,value):
		self.params[56].value = value

	beDecay = property(getBeDecay,setBeDecay, doc='56 : Be Decay (0.0,1.0)')

	def getBePeak(self):
		return self.params[57].value

	def setBePeak(self,value):
		self.params[57].value = value

	bePeak = property(getBePeak,setBePeak, doc='57 : Be Peak (0.0,1.0)')

	def getBeSustain(self):
		return self.params[58].value

	def setBeSustain(self,value):
		self.params[58].value = value

	beSustain = property(getBeSustain,setBeSustain, doc='58 : Be Sustain (0.0,1.0)')

	def getBeRelease(self):
		return self.params[59].value

	def setBeRelease(self,value):
		self.params[59].value = value

	beRelease = property(getBeRelease,setBeRelease, doc='59 : Be Release (0.0,1.0)')

	def getBeMode(self):
		return self.params[60].value

	def setBeMode(self,value):
		self.params[60].value = value

	beMode = property(getBeMode,setBeMode, doc='60 : Be Mode (0.0,3.0:Q)')

	def getBeLoop(self):
		return self.params[61].value

	def setBeLoop(self,value):
		self.params[61].value = value

	beLoop = property(getBeLoop,setBeLoop, doc='61 : Be Loop (0.0,1.0)')

	def getBeRetrig(self):
		return self.params[62].value

	def setBeRetrig(self,value):
		self.params[62].value = value

	beRetrig = property(getBeRetrig,setBeRetrig, doc='62 : Be Retrig (0.0,14.0)')

	def getBeVelToR(self):
		return self.params[63].value

	def setBeVelToR(self,value):
		self.params[63].value = value

	beVelToR = property(getBeVelToR,setBeVelToR, doc='63 : Be R < Vel (-100.0,100.0)')

	def getCOn(self):
		return self.params[64].value

	def setCOn(self,value):
		self.params[64].value = value

	cOn = property(getCOn,setCOn, doc='64 : C On (0.0,1.0:Q)')

	def getCCoarse(self):
		return self.params[65].value

	def setCCoarse(self,value):
		self.params[65].value = value

	cCoarse = property(getCCoarse,setCCoarse, doc='65 : C Coarse (0.0,48.0)')

	def getCFine(self):
		return self.params[66].value

	def setCFine(self,value):
		self.params[66].value = value

	cFine = property(getCFine,setCFine, doc='66 : C Fine (0.0,1000.0)')

	def getCVelToFreq(self):
		return self.params[67].value

	def setCVelToFreq(self,value):
		self.params[67].value = value

	cVelToFreq = property(getCVelToFreq,setCVelToFreq, doc='67 : C Freq<Vel (-100.0,100.0)')

	def getCQuantize(self):
		return self.params[68].value

	def setCQuantize(self,value):
		self.params[68].value = value

	cQuantize = property(getCQuantize,setCQuantize, doc='68 : C Quantize (0.0,1.0:Q)')

	def getCFixOn(self):
		return self.params[69].value

	def setCFixOn(self,value):
		self.params[69].value = value

	cFixOn = property(getCFixOn,setCFixOn, doc='69 : C Fix On  (0.0,1.0:Q)')

	def getCFixFreq(self):
		return self.params[70].value

	def setCFixFreq(self,value):
		self.params[70].value = value

	cFixFreq = property(getCFixFreq,setCFixFreq, doc='70 : C Fix Freq (0.0,1.0)')

	def getCFixFreqMul(self):
		return self.params[71].value

	def setCFixFreqMul(self,value):
		self.params[71].value = value

	cFixFreqMul = property(getCFixFreqMul,setCFixFreqMul, doc='71 : C Fix Freq Mul (0.0,5.0)')

	def getCLevel(self):
		return self.params[72].value

	def setCLevel(self,value):
		self.params[72].value = value

	cLevel = property(getCLevel,setCLevel, doc='72 : C Level (0.0,1.0)')

	def getCPhase(self):
		return self.params[73].value

	def setCPhase(self,value):
		self.params[73].value = value

	cPhase = property(getCPhase,setCPhase, doc='73 : C Phase (0.0,100.0)')

	def getPeToOscc(self):
		return self.params[74].value

	def setPeToOscc(self,value):
		self.params[74].value = value

	peToOscc = property(getPeToOscc,setPeToOscc, doc='74 : Pe to Osc-C (0.0,1.0:Q)')

	def getCVelToLev(self):
		return self.params[75].value

	def setCVelToLev(self,value):
		self.params[75].value = value

	cVelToLev = property(getCVelToLev,setCVelToLev, doc='75 : C Lev < Vel (-100.0,100.0)')

	def getCKeyToLev(self):
		return self.params[76].value

	def setCKeyToLev(self,value):
		self.params[76].value = value

	cKeyToLev = property(getCKeyToLev,setCKeyToLev, doc='76 : C Lev < Key (-100.0,100.0)')

	def getCWave(self):
		return self.params[77].value

	def setCWave(self,value):
		self.params[77].value = value

	cWave = property(getCWave,setCWave, doc='77 : C Wave (0.0,25.0:Q)')

	def getLfoToOscc(self):
		return self.params[78].value

	def setLfoToOscc(self,value):
		self.params[78].value = value

	lfoToOscc = property(getLfoToOscc,setLfoToOscc, doc='78 : LFO to Osc-C (0.0,1.0:Q)')

	def getCeAttack(self):
		return self.params[79].value

	def setCeAttack(self,value):
		self.params[79].value = value

	ceAttack = property(getCeAttack,setCeAttack, doc='79 : Ce Attack (0.0,1.0)')

	def getCeInit(self):
		return self.params[80].value

	def setCeInit(self,value):
		self.params[80].value = value

	ceInit = property(getCeInit,setCeInit, doc='80 : Ce Init (0.0,1.0)')

	def getCeDecay(self):
		return self.params[81].value

	def setCeDecay(self,value):
		self.params[81].value = value

	ceDecay = property(getCeDecay,setCeDecay, doc='81 : Ce Decay (0.0,1.0)')

	def getCePeak(self):
		return self.params[82].value

	def setCePeak(self,value):
		self.params[82].value = value

	cePeak = property(getCePeak,setCePeak, doc='82 : Ce Peak (0.0,1.0)')

	def getCeSustain(self):
		return self.params[83].value

	def setCeSustain(self,value):
		self.params[83].value = value

	ceSustain = property(getCeSustain,setCeSustain, doc='83 : Ce Sustain (0.0,1.0)')

	def getCeRelease(self):
		return self.params[84].value

	def setCeRelease(self,value):
		self.params[84].value = value

	ceRelease = property(getCeRelease,setCeRelease, doc='84 : Ce Release (0.0,1.0)')

	def getCeMode(self):
		return self.params[85].value

	def setCeMode(self,value):
		self.params[85].value = value

	ceMode = property(getCeMode,setCeMode, doc='85 : Ce Mode (0.0,3.0:Q)')

	def getCeLoop(self):
		return self.params[86].value

	def setCeLoop(self,value):
		self.params[86].value = value

	ceLoop = property(getCeLoop,setCeLoop, doc='86 : Ce Loop (0.0,1.0)')

	def getCeRetrig(self):
		return self.params[87].value

	def setCeRetrig(self,value):
		self.params[87].value = value

	ceRetrig = property(getCeRetrig,setCeRetrig, doc='87 : Ce Retrig (0.0,14.0)')

	def getCeVelToR(self):
		return self.params[88].value

	def setCeVelToR(self,value):
		self.params[88].value = value

	ceVelToR = property(getCeVelToR,setCeVelToR, doc='88 : Ce R < Vel (-100.0,100.0)')

	def getDOn(self):
		return self.params[89].value

	def setDOn(self,value):
		self.params[89].value = value

	dOn = property(getDOn,setDOn, doc='89 : D On (0.0,1.0:Q)')

	def getDCoarse(self):
		return self.params[90].value

	def setDCoarse(self,value):
		self.params[90].value = value

	dCoarse = property(getDCoarse,setDCoarse, doc='90 : D Coarse (0.0,48.0)')

	def getDFine(self):
		return self.params[91].value

	def setDFine(self,value):
		self.params[91].value = value

	dFine = property(getDFine,setDFine, doc='91 : D Fine (0.0,1000.0)')

	def getDVelToFreq(self):
		return self.params[92].value

	def setDVelToFreq(self,value):
		self.params[92].value = value

	dVelToFreq = property(getDVelToFreq,setDVelToFreq, doc='92 : D Freq<Vel (-100.0,100.0)')

	def getDQuantize(self):
		return self.params[93].value

	def setDQuantize(self,value):
		self.params[93].value = value

	dQuantize = property(getDQuantize,setDQuantize, doc='93 : D Quantize (0.0,1.0:Q)')

	def getDFixOn(self):
		return self.params[94].value

	def setDFixOn(self,value):
		self.params[94].value = value

	dFixOn = property(getDFixOn,setDFixOn, doc='94 : D Fix On  (0.0,1.0:Q)')

	def getDFixFreq(self):
		return self.params[95].value

	def setDFixFreq(self,value):
		self.params[95].value = value

	dFixFreq = property(getDFixFreq,setDFixFreq, doc='95 : D Fix Freq (0.0,1.0)')

	def getDFixFreqMul(self):
		return self.params[96].value

	def setDFixFreqMul(self,value):
		self.params[96].value = value

	dFixFreqMul = property(getDFixFreqMul,setDFixFreqMul, doc='96 : D Fix Freq Mul (0.0,5.0)')

	def getDLevel(self):
		return self.params[97].value

	def setDLevel(self,value):
		self.params[97].value = value

	dLevel = property(getDLevel,setDLevel, doc='97 : D Level (0.0,1.0)')

	def getDPhase(self):
		return self.params[98].value

	def setDPhase(self,value):
		self.params[98].value = value

	dPhase = property(getDPhase,setDPhase, doc='98 : D Phase (0.0,100.0)')

	def getPeToOscd(self):
		return self.params[99].value

	def setPeToOscd(self,value):
		self.params[99].value = value

	peToOscd = property(getPeToOscd,setPeToOscd, doc='99 : Pe to Osc-D (0.0,1.0:Q)')

	def getDVelToLev(self):
		return self.params[100].value

	def setDVelToLev(self,value):
		self.params[100].value = value

	dVelToLev = property(getDVelToLev,setDVelToLev, doc='100 : D Lev < Vel (-100.0,100.0)')

	def getDKeyToLev(self):
		return self.params[101].value

	def setDKeyToLev(self,value):
		self.params[101].value = value

	dKeyToLev = property(getDKeyToLev,setDKeyToLev, doc='101 : D Lev < Key (-100.0,100.0)')

	def getDWave(self):
		return self.params[102].value

	def setDWave(self,value):
		self.params[102].value = value

	dWave = property(getDWave,setDWave, doc='102 : D Wave (0.0,25.0:Q)')

	def getLfoToOscd(self):
		return self.params[103].value

	def setLfoToOscd(self,value):
		self.params[103].value = value

	lfoToOscd = property(getLfoToOscd,setLfoToOscd, doc='103 : LFO to Osc-D (0.0,1.0:Q)')

	def getDeAttack(self):
		return self.params[104].value

	def setDeAttack(self,value):
		self.params[104].value = value

	deAttack = property(getDeAttack,setDeAttack, doc='104 : De Attack (0.0,1.0)')

	def getDeInit(self):
		return self.params[105].value

	def setDeInit(self,value):
		self.params[105].value = value

	deInit = property(getDeInit,setDeInit, doc='105 : De Init (0.0,1.0)')

	def getDeDecay(self):
		return self.params[106].value

	def setDeDecay(self,value):
		self.params[106].value = value

	deDecay = property(getDeDecay,setDeDecay, doc='106 : De Decay (0.0,1.0)')

	def getDePeak(self):
		return self.params[107].value

	def setDePeak(self,value):
		self.params[107].value = value

	dePeak = property(getDePeak,setDePeak, doc='107 : De Peak (0.0,1.0)')

	def getDeSustain(self):
		return self.params[108].value

	def setDeSustain(self,value):
		self.params[108].value = value

	deSustain = property(getDeSustain,setDeSustain, doc='108 : De Sustain (0.0,1.0)')

	def getDeRelease(self):
		return self.params[109].value

	def setDeRelease(self,value):
		self.params[109].value = value

	deRelease = property(getDeRelease,setDeRelease, doc='109 : De Release (0.0,1.0)')

	def getDeMode(self):
		return self.params[110].value

	def setDeMode(self,value):
		self.params[110].value = value

	deMode = property(getDeMode,setDeMode, doc='110 : De Mode (0.0,3.0:Q)')

	def getDeLoop(self):
		return self.params[111].value

	def setDeLoop(self,value):
		self.params[111].value = value

	deLoop = property(getDeLoop,setDeLoop, doc='111 : De Loop (0.0,1.0)')

	def getDeRetrig(self):
		return self.params[112].value

	def setDeRetrig(self,value):
		self.params[112].value = value

	deRetrig = property(getDeRetrig,setDeRetrig, doc='112 : De Retrig (0.0,14.0)')

	def getDeVelToR(self):
		return self.params[113].value

	def setDeVelToR(self,value):
		self.params[113].value = value

	deVelToR = property(getDeVelToR,setDeVelToR, doc='113 : De R < Vel (-100.0,100.0)')

	def getTime(self):
		return self.params[114].value

	def setTime(self,value):
		self.params[114].value = value

	time = property(getTime,setTime, doc='114 : Time (-100.0,100.0)')

	def getKeyToTime(self):
		return self.params[115].value

	def setKeyToTime(self,value):
		self.params[115].value = value

	keyToTime = property(getKeyToTime,setKeyToTime, doc='115 : Time < Key (-100.0,100.0)')

	def getPeOn(self):
		return self.params[116].value

	def setPeOn(self,value):
		self.params[116].value = value

	peOn = property(getPeOn,setPeOn, doc='116 : Pe On (0.0,1.0:Q)')

	def getPeAttack(self):
		return self.params[117].value

	def setPeAttack(self,value):
		self.params[117].value = value

	peAttack = property(getPeAttack,setPeAttack, doc='117 : Pe Attack (0.0,1.0)')

	def getPeInit(self):
		return self.params[118].value

	def setPeInit(self,value):
		self.params[118].value = value

	peInit = property(getPeInit,setPeInit, doc='118 : Pe Init (-48.0,48.0)')

	def getPeDecay(self):
		return self.params[119].value

	def setPeDecay(self,value):
		self.params[119].value = value

	peDecay = property(getPeDecay,setPeDecay, doc='119 : Pe Decay (0.0,1.0)')

	def getPePeak(self):
		return self.params[120].value

	def setPePeak(self,value):
		self.params[120].value = value

	pePeak = property(getPePeak,setPePeak, doc='120 : Pe Peak (-48.0,48.0)')

	def getPeSustain(self):
		return self.params[121].value

	def setPeSustain(self,value):
		self.params[121].value = value

	peSustain = property(getPeSustain,setPeSustain, doc='121 : Pe Sustain (-48.0,48.0)')

	def getPeRelease(self):
		return self.params[122].value

	def setPeRelease(self,value):
		self.params[122].value = value

	peRelease = property(getPeRelease,setPeRelease, doc='122 : Pe Release (0.0,1.0)')

	def getPeMode(self):
		return self.params[123].value

	def setPeMode(self,value):
		self.params[123].value = value

	peMode = property(getPeMode,setPeMode, doc='123 : Pe Mode (0.0,3.0:Q)')

	def getPeLoop(self):
		return self.params[124].value

	def setPeLoop(self,value):
		self.params[124].value = value

	peLoop = property(getPeLoop,setPeLoop, doc='124 : Pe Loop (0.0,1.0)')

	def getPeRetrig(self):
		return self.params[125].value

	def setPeRetrig(self,value):
		self.params[125].value = value

	peRetrig = property(getPeRetrig,setPeRetrig, doc='125 : Pe Retrig (0.0,14.0)')

	def getPeVelToR(self):
		return self.params[126].value

	def setPeVelToR(self,value):
		self.params[126].value = value

	peVelToR = property(getPeVelToR,setPeVelToR, doc='126 : Pe R < Vel (-100.0,100.0)')

	def getPeAmount(self):
		return self.params[127].value

	def setPeAmount(self,value):
		self.params[127].value = value

	peAmount = property(getPeAmount,setPeAmount, doc='127 : Pe Amount (-1.0,1.0)')

	def getLfoOn(self):
		return self.params[128].value

	def setLfoOn(self,value):
		self.params[128].value = value

	lfoOn = property(getLfoOn,setLfoOn, doc='128 : LFO On (0.0,1.0:Q)')

	def getLfoType(self):
		return self.params[129].value

	def setLfoType(self,value):
		self.params[129].value = value

	lfoType = property(getLfoType,setLfoType, doc='129 : LFO Type (0.0,6.0:Q)')

	def getLfoRange(self):
		return self.params[130].value

	def setLfoRange(self,value):
		self.params[130].value = value

	lfoRange = property(getLfoRange,setLfoRange, doc='130 : LFO Range (0.0,2.0:Q)')

	def getLfoRate(self):
		return self.params[131].value

	def setLfoRate(self,value):
		self.params[131].value = value

	lfoRate = property(getLfoRate,setLfoRate, doc='131 : LFO Rate (0.0,127.0)')

	def getLfoSync(self):
		return self.params[132].value

	def setLfoSync(self,value):
		self.params[132].value = value

	lfoSync = property(getLfoSync,setLfoSync, doc='132 : LFO Sync (0.0,14.0)')

	def getLfoKToR(self):
		return self.params[133].value

	def setLfoKToR(self,value):
		self.params[133].value = value

	lfoKToR = property(getLfoKToR,setLfoKToR, doc='133 : LFO R < K (0.0,1.0)')

	def getLfoMod(self):
		return self.params[134].value

	def setLfoMod(self,value):
		self.params[134].value = value

	lfoMod = property(getLfoMod,setLfoMod, doc='134 : LFO Mod (0.0,1.0)')

	def getVelToLfo(self):
		return self.params[135].value

	def setVelToLfo(self,value):
		self.params[135].value = value

	velToLfo = property(getVelToLfo,setVelToLfo, doc='135 : LFO < Vel (-1.0,1.0)')

	def getPeToLfo(self):
		return self.params[136].value

	def setPeToLfo(self,value):
		self.params[136].value = value

	peToLfo = property(getPeToLfo,setPeToLfo, doc='136 : Pe To LFO (0.0,1.0:Q)')

	def getLeAttack(self):
		return self.params[137].value

	def setLeAttack(self,value):
		self.params[137].value = value

	leAttack = property(getLeAttack,setLeAttack, doc='137 : Le Attack (0.0,1.0)')

	def getLeInit(self):
		return self.params[138].value

	def setLeInit(self,value):
		self.params[138].value = value

	leInit = property(getLeInit,setLeInit, doc='138 : Le Init (0.0,1.0)')

	def getLeDecay(self):
		return self.params[139].value

	def setLeDecay(self,value):
		self.params[139].value = value

	leDecay = property(getLeDecay,setLeDecay, doc='139 : Le Decay (0.0,1.0)')

	def getLePeak(self):
		return self.params[140].value

	def setLePeak(self,value):
		self.params[140].value = value

	lePeak = property(getLePeak,setLePeak, doc='140 : Le Peak (0.0,1.0)')

	def getLeSustain(self):
		return self.params[141].value

	def setLeSustain(self,value):
		self.params[141].value = value

	leSustain = property(getLeSustain,setLeSustain, doc='141 : Le Sustain (0.0,1.0)')

	def getLeRelease(self):
		return self.params[142].value

	def setLeRelease(self,value):
		self.params[142].value = value

	leRelease = property(getLeRelease,setLeRelease, doc='142 : Le Release (0.0,1.0)')

	def getLeMode(self):
		return self.params[143].value

	def setLeMode(self,value):
		self.params[143].value = value

	leMode = property(getLeMode,setLeMode, doc='143 : Le Mode (0.0,3.0:Q)')

	def getLeLoop(self):
		return self.params[144].value

	def setLeLoop(self,value):
		self.params[144].value = value

	leLoop = property(getLeLoop,setLeLoop, doc='144 : Le Loop (0.0,1.0)')

	def getLeRetrig(self):
		return self.params[145].value

	def setLeRetrig(self,value):
		self.params[145].value = value

	leRetrig = property(getLeRetrig,setLeRetrig, doc='145 : Le Retrig (0.0,14.0)')

	def getLeVelToR(self):
		return self.params[146].value

	def setLeVelToR(self,value):
		self.params[146].value = value

	leVelToR = property(getLeVelToR,setLeVelToR, doc='146 : Le R < Vel (-100.0,100.0)')

	def getFilterOn(self):
		return self.params[147].value

	def setFilterOn(self,value):
		self.params[147].value = value

	filterOn = property(getFilterOn,setFilterOn, doc='147 : Filter On (0.0,1.0:Q)')

	def getFilterType(self):
		return self.params[148].value

	def setFilterType(self,value):
		self.params[148].value = value

	filterType = property(getFilterType,setFilterType, doc='148 : Filter Type (0.0,7.0:Q)')

	def getFilterFreq(self):
		return self.params[149].value

	def setFilterFreq(self,value):
		self.params[149].value = value

	filterFreq = property(getFilterFreq,setFilterFreq, doc='149 : Filter Freq (0.0,1.0)')

	def getFilterRes(self):
		return self.params[150].value

	def setFilterRes(self,value):
		self.params[150].value = value

	filterRes = property(getFilterRes,setFilterRes, doc='150 : Filter Res (0.0,1.0)')

	def getVelToFilt(self):
		return self.params[151].value

	def setVelToFilt(self,value):
		self.params[151].value = value

	velToFilt = property(getVelToFilt,setVelToFilt, doc='151 : Filt < Vel (0.0,100.0)')

	def getKeyToFilt(self):
		return self.params[152].value

	def setKeyToFilt(self,value):
		self.params[152].value = value

	keyToFilt = property(getKeyToFilt,setKeyToFilt, doc='152 : Filt < Key (-100.0,100.0)')

	def getFeAmount(self):
		return self.params[153].value

	def setFeAmount(self,value):
		self.params[153].value = value

	feAmount = property(getFeAmount,setFeAmount, doc='153 : Fe Amount (-100.0,100.0)')

	def getLfoToFilt(self):
		return self.params[154].value

	def setLfoToFilt(self,value):
		self.params[154].value = value

	lfoToFilt = property(getLfoToFilt,setLfoToFilt, doc='154 : Filt < LFO (0.0,1.0:Q)')

	def getFeAttack(self):
		return self.params[155].value

	def setFeAttack(self,value):
		self.params[155].value = value

	feAttack = property(getFeAttack,setFeAttack, doc='155 : Fe Attack (0.0,1.0)')

	def getFeInit(self):
		return self.params[156].value

	def setFeInit(self,value):
		self.params[156].value = value

	feInit = property(getFeInit,setFeInit, doc='156 : Fe Init (0.0,1.0)')

	def getFeDecay(self):
		return self.params[157].value

	def setFeDecay(self,value):
		self.params[157].value = value

	feDecay = property(getFeDecay,setFeDecay, doc='157 : Fe Decay (0.0,1.0)')

	def getFePeak(self):
		return self.params[158].value

	def setFePeak(self,value):
		self.params[158].value = value

	fePeak = property(getFePeak,setFePeak, doc='158 : Fe Peak (0.0,1.0)')

	def getFeSustain(self):
		return self.params[159].value

	def setFeSustain(self,value):
		self.params[159].value = value

	feSustain = property(getFeSustain,setFeSustain, doc='159 : Fe Sustain (0.0,1.0)')

	def getFeRelease(self):
		return self.params[160].value

	def setFeRelease(self,value):
		self.params[160].value = value

	feRelease = property(getFeRelease,setFeRelease, doc='160 : Fe Release (0.0,1.0)')

	def getFeMode(self):
		return self.params[161].value

	def setFeMode(self,value):
		self.params[161].value = value

	feMode = property(getFeMode,setFeMode, doc='161 : Fe Mode (0.0,3.0:Q)')

	def getFeLoop(self):
		return self.params[162].value

	def setFeLoop(self,value):
		self.params[162].value = value

	feLoop = property(getFeLoop,setFeLoop, doc='162 : Fe Loop (0.0,1.0)')

	def getFeRetrig(self):
		return self.params[163].value

	def setFeRetrig(self,value):
		self.params[163].value = value

	feRetrig = property(getFeRetrig,setFeRetrig, doc='163 : Fe Retrig (0.0,14.0)')

	def getFeVelToR(self):
		return self.params[164].value

	def setFeVelToR(self,value):
		self.params[164].value = value

	feVelToR = property(getFeVelToR,setFeVelToR, doc='164 : Fe R < Vel (-100.0,100.0)')

