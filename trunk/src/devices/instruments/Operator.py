class Operator:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value):
		self.params[0].value = value

	def algorithm(self,value):
		self.params[1].value = value

	def hiq(self,value):
		self.params[2].value = value

	def transpose(self,value):
		self.params[3].value = value

	def pbRange(self,value):
		self.params[4].value = value

	def volume(self,value):
		self.params[5].value = value

	def panorama(self,value):
		self.params[6].value = value

	def panToKey(self,value):
		self.params[7].value = value

	def panToRnd(self,value):
		self.params[8].value = value

	def dFeedback(self,value):
		self.params[9].value = value

	def tone(self,value):
		self.params[10].value = value

	def spread(self,value):
		self.params[11].value = value

	def glideOn(self,value):
		self.params[12].value = value

	def glideTime(self,value):
		self.params[13].value = value

	def aOn(self,value):
		self.params[14].value = value

	def aCoarse(self,value):
		self.params[15].value = value

	def aFine(self,value):
		self.params[16].value = value

	def aFreqToVel(self,value):
		self.params[17].value = value

	def aQuantize(self,value):
		self.params[18].value = value

	def aFixOn(self,value):
		self.params[19].value = value

	def aFixFreq(self,value):
		self.params[20].value = value

	def aFixFreqMul(self,value):
		self.params[21].value = value

	def aLevel(self,value):
		self.params[22].value = value

	def aPhase(self,value):
		self.params[23].value = value

	def peToOscA(self,value):
		self.params[24].value = value

	def aLevToVel(self,value):
		self.params[25].value = value

	def aLevToKey(self,value):
		self.params[26].value = value

	def aWave(self,value):
		self.params[27].value = value

	def lfoToOscA(self,value):
		self.params[28].value = value

	def aeAttack(self,value):
		self.params[29].value = value

	def aeInit(self,value):
		self.params[30].value = value

	def aeDecay(self,value):
		self.params[31].value = value

	def aePeak(self,value):
		self.params[32].value = value

	def aeSustain(self,value):
		self.params[33].value = value

	def aeRelease(self,value):
		self.params[34].value = value

	def aeMode(self,value):
		self.params[35].value = value

	def aeLoop(self,value):
		self.params[36].value = value

	def aeRetrig(self,value):
		self.params[37].value = value

	def aeRToVel(self,value):
		self.params[38].value = value

	def bOn(self,value):
		self.params[39].value = value

	def bCoarse(self,value):
		self.params[40].value = value

	def bFine(self,value):
		self.params[41].value = value

	def bFreqToVel(self,value):
		self.params[42].value = value

	def bQuantize(self,value):
		self.params[43].value = value

	def bFixOn(self,value):
		self.params[44].value = value

	def bFixFreq(self,value):
		self.params[45].value = value

	def bFixFreqMul(self,value):
		self.params[46].value = value

	def bLevel(self,value):
		self.params[47].value = value

	def bPhase(self,value):
		self.params[48].value = value

	def peToOscB(self,value):
		self.params[49].value = value

	def bLevToVel(self,value):
		self.params[50].value = value

	def bLevToKey(self,value):
		self.params[51].value = value

	def bWave(self,value):
		self.params[52].value = value

	def lfoToOscB(self,value):
		self.params[53].value = value

	def beAttack(self,value):
		self.params[54].value = value

	def beInit(self,value):
		self.params[55].value = value

	def beDecay(self,value):
		self.params[56].value = value

	def bePeak(self,value):
		self.params[57].value = value

	def beSustain(self,value):
		self.params[58].value = value

	def beRelease(self,value):
		self.params[59].value = value

	def beMode(self,value):
		self.params[60].value = value

	def beLoop(self,value):
		self.params[61].value = value

	def beRetrig(self,value):
		self.params[62].value = value

	def beRToVel(self,value):
		self.params[63].value = value

	def cOn(self,value):
		self.params[64].value = value

	def cCoarse(self,value):
		self.params[65].value = value

	def cFine(self,value):
		self.params[66].value = value

	def cFreqToVel(self,value):
		self.params[67].value = value

	def cQuantize(self,value):
		self.params[68].value = value

	def cFixOn(self,value):
		self.params[69].value = value

	def cFixFreq(self,value):
		self.params[70].value = value

	def cFixFreqMul(self,value):
		self.params[71].value = value

	def cLevel(self,value):
		self.params[72].value = value

	def cPhase(self,value):
		self.params[73].value = value

	def peToOscC(self,value):
		self.params[74].value = value

	def cLevToVel(self,value):
		self.params[75].value = value

	def cLevToKey(self,value):
		self.params[76].value = value

	def cWave(self,value):
		self.params[77].value = value

	def lfoToOscC(self,value):
		self.params[78].value = value

	def ceAttack(self,value):
		self.params[79].value = value

	def ceInit(self,value):
		self.params[80].value = value

	def ceDecay(self,value):
		self.params[81].value = value

	def cePeak(self,value):
		self.params[82].value = value

	def ceSustain(self,value):
		self.params[83].value = value

	def ceRelease(self,value):
		self.params[84].value = value

	def ceMode(self,value):
		self.params[85].value = value

	def ceLoop(self,value):
		self.params[86].value = value

	def ceRetrig(self,value):
		self.params[87].value = value

	def ceRToVel(self,value):
		self.params[88].value = value

	def dOn(self,value):
		self.params[89].value = value

	def dCoarse(self,value):
		self.params[90].value = value

	def dFine(self,value):
		self.params[91].value = value

	def dFreqToVel(self,value):
		self.params[92].value = value

	def dQuantize(self,value):
		self.params[93].value = value

	def dFixOn(self,value):
		self.params[94].value = value

	def dFixFreq(self,value):
		self.params[95].value = value

	def dFixFreqMul(self,value):
		self.params[96].value = value

	def dLevel(self,value):
		self.params[97].value = value

	def dPhase(self,value):
		self.params[98].value = value

	def peToOscD(self,value):
		self.params[99].value = value

	def dLevToVel(self,value):
		self.params[100].value = value

	def dLevToKey(self,value):
		self.params[101].value = value

	def dWave(self,value):
		self.params[102].value = value

	def lfoToOscD(self,value):
		self.params[103].value = value

	def deAttack(self,value):
		self.params[104].value = value

	def deInit(self,value):
		self.params[105].value = value

	def deDecay(self,value):
		self.params[106].value = value

	def dePeak(self,value):
		self.params[107].value = value

	def deSustain(self,value):
		self.params[108].value = value

	def deRelease(self,value):
		self.params[109].value = value

	def deMode(self,value):
		self.params[110].value = value

	def deLoop(self,value):
		self.params[111].value = value

	def deRetrig(self,value):
		self.params[112].value = value

	def deRToVel(self,value):
		self.params[113].value = value

	def time(self,value):
		self.params[114].value = value

	def timeToKey(self,value):
		self.params[115].value = value

	def peOn(self,value):
		self.params[116].value = value

	def peAttack(self,value):
		self.params[117].value = value

	def peInit(self,value):
		self.params[118].value = value

	def peDecay(self,value):
		self.params[119].value = value

	def pePeak(self,value):
		self.params[120].value = value

	def peSustain(self,value):
		self.params[121].value = value

	def peRelease(self,value):
		self.params[122].value = value

	def peMode(self,value):
		self.params[123].value = value

	def peLoop(self,value):
		self.params[124].value = value

	def peRetrig(self,value):
		self.params[125].value = value

	def peRToVel(self,value):
		self.params[126].value = value

	def peAmount(self,value):
		self.params[127].value = value

	def lfoOn(self,value):
		self.params[128].value = value

	def lfoType(self,value):
		self.params[129].value = value

	def lfoRange(self,value):
		self.params[130].value = value

	def lfoRate(self,value):
		self.params[131].value = value

	def lfoSync(self,value):
		self.params[132].value = value

	def lfoRToK(self,value):
		self.params[133].value = value

	def lfoMod(self,value):
		self.params[134].value = value

	def lfoToVel(self,value):
		self.params[135].value = value

	def peToLfo(self,value):
		self.params[136].value = value

	def leAttack(self,value):
		self.params[137].value = value

	def leInit(self,value):
		self.params[138].value = value

	def leDecay(self,value):
		self.params[139].value = value

	def lePeak(self,value):
		self.params[140].value = value

	def leSustain(self,value):
		self.params[141].value = value

	def leRelease(self,value):
		self.params[142].value = value

	def leMode(self,value):
		self.params[143].value = value

	def leLoop(self,value):
		self.params[144].value = value

	def leRetrig(self,value):
		self.params[145].value = value

	def leRToVel(self,value):
		self.params[146].value = value

	def filterOn(self,value):
		self.params[147].value = value

	def filterType(self,value):
		self.params[148].value = value

	def filterFreq(self,value):
		self.params[149].value = value

	def filterRes(self,value):
		self.params[150].value = value

	def filtToVel(self,value):
		self.params[151].value = value

	def filtToKey(self,value):
		self.params[152].value = value

	def feAmount(self,value):
		self.params[153].value = value

	def filtToLfo(self,value):
		self.params[154].value = value

	def feAttack(self,value):
		self.params[155].value = value

	def feInit(self,value):
		self.params[156].value = value

	def feDecay(self,value):
		self.params[157].value = value

	def fePeak(self,value):
		self.params[158].value = value

	def feSustain(self,value):
		self.params[159].value = value

	def feRelease(self,value):
		self.params[160].value = value

	def feMode(self,value):
		self.params[161].value = value

	def feLoop(self,value):
		self.params[162].value = value

	def feRetrig(self,value):
		self.params[163].value = value

	def feRToVel(self,value):
		self.params[164].value = value

