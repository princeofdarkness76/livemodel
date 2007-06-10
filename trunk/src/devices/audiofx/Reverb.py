from LiveModel import DeviceBase

class Reverb(DeviceBase):

	def __init__(self,device):
		DeviceBase.__init__(self, device)

	def getDeviceOn(self):
		return self.params[0].value

	def setDeviceOn(self,value):
		self.params[0].value = value

	deviceOn = property(getDeviceOn,setDeviceOn, doc='0 : Device On (0.0,1.0:Q)')

	def getPredelay(self):
		return self.params[1].value

	def setPredelay(self,value):
		self.params[1].value = value

	predelay = property(getPredelay,setPredelay, doc='1 : PreDelay (0.0,1.0)')

	def getInLowcutOn(self):
		return self.params[2].value

	def setInLowcutOn(self,value):
		self.params[2].value = value

	inLowcutOn = property(getInLowcutOn,setInLowcutOn, doc='2 : In LowCut On (0.0,1.0:Q)')

	def getInHighcutOn(self):
		return self.params[3].value

	def setInHighcutOn(self,value):
		self.params[3].value = value

	inHighcutOn = property(getInHighcutOn,setInHighcutOn, doc='3 : In HighCut On (0.0,1.0:Q)')

	def getInFreqency(self):
		return self.params[4].value

	def setInFreqency(self,value):
		self.params[4].value = value

	inFreqency = property(getInFreqency,setInFreqency, doc='4 : In Freqency (0.0,1.0)')

	def getInWidth(self):
		return self.params[5].value

	def setInWidth(self,value):
		self.params[5].value = value

	inWidth = property(getInWidth,setInWidth, doc='5 : In Width (0.5,9.0)')

	def getErSpinOn(self):
		return self.params[6].value

	def setErSpinOn(self,value):
		self.params[6].value = value

	erSpinOn = property(getErSpinOn,setErSpinOn, doc='6 : ER Spin On (0.0,1.0:Q)')

	def getErSpinRate(self):
		return self.params[7].value

	def setErSpinRate(self,value):
		self.params[7].value = value

	erSpinRate = property(getErSpinRate,setErSpinRate, doc='7 : ER Spin Rate (0.0,1.0)')

	def getErSpinAmount(self):
		return self.params[8].value

	def setErSpinAmount(self,value):
		self.params[8].value = value

	erSpinAmount = property(getErSpinAmount,setErSpinAmount, doc='8 : ER Spin Amount (0.0,1.0)')

	def getErShape(self):
		return self.params[9].value

	def setErShape(self,value):
		self.params[9].value = value

	erShape = property(getErShape,setErShape, doc='9 : ER Shape (0.0,1.0)')

	def getHishelfOn(self):
		return self.params[10].value

	def setHishelfOn(self,value):
		self.params[10].value = value

	hishelfOn = property(getHishelfOn,setHishelfOn, doc='10 : HiShelf On (0.0,1.0:Q)')

	def getHishelfFreq(self):
		return self.params[11].value

	def setHishelfFreq(self,value):
		self.params[11].value = value

	hishelfFreq = property(getHishelfFreq,setHishelfFreq, doc='11 : HiShelf Freq (0.0,1.0)')

	def getHishelfGain(self):
		return self.params[12].value

	def setHishelfGain(self,value):
		self.params[12].value = value

	hishelfGain = property(getHishelfGain,setHishelfGain, doc='12 : HiShelf Gain (0.20000000298,1.0)')

	def getLowshelfOn(self):
		return self.params[13].value

	def setLowshelfOn(self,value):
		self.params[13].value = value

	lowshelfOn = property(getLowshelfOn,setLowshelfOn, doc='13 : LowShelf On (0.0,1.0:Q)')

	def getLowshelfFreq(self):
		return self.params[14].value

	def setLowshelfFreq(self,value):
		self.params[14].value = value

	lowshelfFreq = property(getLowshelfFreq,setLowshelfFreq, doc='14 : LowShelf Freq (0.0,1.0)')

	def getLowshelfGain(self):
		return self.params[15].value

	def setLowshelfGain(self,value):
		self.params[15].value = value

	lowshelfGain = property(getLowshelfGain,setLowshelfGain, doc='15 : LowShelf Gain (0.20000000298,1.0)')

	def getChorusOn(self):
		return self.params[16].value

	def setChorusOn(self,value):
		self.params[16].value = value

	chorusOn = property(getChorusOn,setChorusOn, doc='16 : Chorus On (0.0,1.0:Q)')

	def getChorusRate(self):
		return self.params[17].value

	def setChorusRate(self,value):
		self.params[17].value = value

	chorusRate = property(getChorusRate,setChorusRate, doc='17 : Chorus Rate (0.0,1.0)')

	def getChorusAmount(self):
		return self.params[18].value

	def setChorusAmount(self,value):
		self.params[18].value = value

	chorusAmount = property(getChorusAmount,setChorusAmount, doc='18 : Chorus Amount (0.0,1.0)')

	def getDecaytime(self):
		return self.params[19].value

	def setDecaytime(self,value):
		self.params[19].value = value

	decaytime = property(getDecaytime,setDecaytime, doc='19 : DecayTime (0.0,1.0)')

	def getDensity(self):
		return self.params[20].value

	def setDensity(self,value):
		self.params[20].value = value

	density = property(getDensity,setDensity, doc='20 : Density (0.0010000000475,0.959999978542)')

	def getScale(self):
		return self.params[21].value

	def setScale(self,value):
		self.params[21].value = value

	scale = property(getScale,setScale, doc='21 : Scale (0.0500000007451,1.0)')

	def getFreezeOn(self):
		return self.params[22].value

	def setFreezeOn(self,value):
		self.params[22].value = value

	freezeOn = property(getFreezeOn,setFreezeOn, doc='22 : Freeze On (0.0,1.0:Q)')

	def getFlatOn(self):
		return self.params[23].value

	def setFlatOn(self,value):
		self.params[23].value = value

	flatOn = property(getFlatOn,setFlatOn, doc='23 : Flat On (0.0,1.0:Q)')

	def getCutOn(self):
		return self.params[24].value

	def setCutOn(self,value):
		self.params[24].value = value

	cutOn = property(getCutOn,setCutOn, doc='24 : Cut On (0.0,1.0:Q)')

	def getRoomSize(self):
		return self.params[25].value

	def setRoomSize(self,value):
		self.params[25].value = value

	roomSize = property(getRoomSize,setRoomSize, doc='25 : Room Size (0.0,1.0)')

	def getStereoImage(self):
		return self.params[26].value

	def setStereoImage(self,value):
		self.params[26].value = value

	stereoImage = property(getStereoImage,setStereoImage, doc='26 : Stereo Image (0.0,120.0)')

	def getQuality(self):
		return self.params[27].value

	def setQuality(self,value):
		self.params[27].value = value

	quality = property(getQuality,setQuality, doc='27 : Quality (0.0,2.0:Q)')

	def getErLevel(self):
		return self.params[28].value

	def setErLevel(self,value):
		self.params[28].value = value

	erLevel = property(getErLevel,setErLevel, doc='28 : ER Level (0.0299999993294,1.99530005455)')

	def getDiffuseLevel(self):
		return self.params[29].value

	def setDiffuseLevel(self,value):
		self.params[29].value = value

	diffuseLevel = property(getDiffuseLevel,setDiffuseLevel, doc='29 : Diffuse Level (0.0299999993294,1.99530005455)')

	def getDryWet(self):
		return self.params[30].value

	def setDryWet(self,value):
		self.params[30].value = value

	dryWet = property(getDryWet,setDryWet, doc='30 : Dry/Wet (0.0,1.0)')

