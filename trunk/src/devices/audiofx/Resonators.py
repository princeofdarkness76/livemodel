class Resonators:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def getDeviceOn(self):
		return self.params[0].value

	def setDeviceOn(self,value):
		self.params[0].value = value

	deviceOn = property(getDeviceOn,setDeviceOn, doc='0 : Device On (0.0,1.0:Q)')

	def getFilterOn(self):
		return self.params[1].value

	def setFilterOn(self,value):
		self.params[1].value = value

	filterOn = property(getFilterOn,setFilterOn, doc='1 : Filter On (0.0,1.0:Q)')

	def getFrequency(self):
		return self.params[2].value

	def setFrequency(self,value):
		self.params[2].value = value

	frequency = property(getFrequency,setFrequency, doc='2 : Frequency (0.0,1.0)')

	def getFilterType(self):
		return self.params[3].value

	def setFilterType(self,value):
		self.params[3].value = value

	filterType = property(getFilterType,setFilterType, doc='3 : Filter Type (0.0,3.0:Q)')

	def getMode(self):
		return self.params[4].value

	def setMode(self,value):
		self.params[4].value = value

	mode = property(getMode,setMode, doc='4 : Mode (0.0,1.0:Q)')

	def getDecay(self):
		return self.params[5].value

	def setDecay(self,value):
		self.params[5].value = value

	decay = property(getDecay,setDecay, doc='5 : Decay (0.0,100.0)')

	def getConst(self):
		return self.params[6].value

	def setConst(self,value):
		self.params[6].value = value

	const = property(getConst,setConst, doc='6 : Const (0.0,1.0:Q)')

	def getColor(self):
		return self.params[7].value

	def setColor(self,value):
		self.params[7].value = value

	color = property(getColor,setColor, doc='7 : Color (0.0,100.0)')

	def getWidth(self):
		return self.params[8].value

	def setWidth(self,value):
		self.params[8].value = value

	width = property(getWidth,setWidth, doc='8 : Width (0.0,1.0)')

	def getDryWet(self):
		return self.params[9].value

	def setDryWet(self,value):
		self.params[9].value = value

	dryWet = property(getDryWet,setDryWet, doc='9 : Dry/Wet (0.0,1.0)')

	def getGlobalGain(self):
		return self.params[10].value

	def setGlobalGain(self,value):
		self.params[10].value = value

	globalGain = property(getGlobalGain,setGlobalGain, doc='10 : Global Gain (-15.0,15.0)')

	def getIOn(self):
		return self.params[11].value

	def setIOn(self,value):
		self.params[11].value = value

	iOn = property(getIOn,setIOn, doc='11 : I On (0.0,1.0:Q)')

	def getINote(self):
		return self.params[12].value

	def setINote(self,value):
		self.params[12].value = value

	iNote = property(getINote,setINote, doc='12 : I Note (12.0,84.0)')

	def getITune(self):
		return self.params[13].value

	def setITune(self,value):
		self.params[13].value = value

	iTune = property(getITune,setITune, doc='13 : I Tune (-50.0,50.0)')

	def getIGain(self):
		return self.params[14].value

	def setIGain(self,value):
		self.params[14].value = value

	iGain = property(getIGain,setIGain, doc='14 : I Gain (0.0,1.0)')

	def getIiOn(self):
		return self.params[15].value

	def setIiOn(self,value):
		self.params[15].value = value

	iiOn = property(getIiOn,setIiOn, doc='15 : II On (0.0,1.0:Q)')

	def getIiPitch(self):
		return self.params[16].value

	def setIiPitch(self,value):
		self.params[16].value = value

	iiPitch = property(getIiPitch,setIiPitch, doc='16 : II Pitch (-24.0,24.0)')

	def getIiTune(self):
		return self.params[17].value

	def setIiTune(self,value):
		self.params[17].value = value

	iiTune = property(getIiTune,setIiTune, doc='17 : II Tune (-50.0,50.0)')

	def getIiGain(self):
		return self.params[18].value

	def setIiGain(self,value):
		self.params[18].value = value

	iiGain = property(getIiGain,setIiGain, doc='18 : II Gain (0.0,1.0)')

	def getIiiOn(self):
		return self.params[19].value

	def setIiiOn(self,value):
		self.params[19].value = value

	iiiOn = property(getIiiOn,setIiiOn, doc='19 : III On (0.0,1.0:Q)')

	def getIiiPitch(self):
		return self.params[20].value

	def setIiiPitch(self,value):
		self.params[20].value = value

	iiiPitch = property(getIiiPitch,setIiiPitch, doc='20 : III Pitch (-24.0,24.0)')

	def getIiiTune(self):
		return self.params[21].value

	def setIiiTune(self,value):
		self.params[21].value = value

	iiiTune = property(getIiiTune,setIiiTune, doc='21 : III Tune (-50.0,50.0)')

	def getIiiGain(self):
		return self.params[22].value

	def setIiiGain(self,value):
		self.params[22].value = value

	iiiGain = property(getIiiGain,setIiiGain, doc='22 : III Gain (0.0,1.0)')

	def getIvOn(self):
		return self.params[23].value

	def setIvOn(self,value):
		self.params[23].value = value

	ivOn = property(getIvOn,setIvOn, doc='23 : IV On (0.0,1.0:Q)')

	def getIvPitch(self):
		return self.params[24].value

	def setIvPitch(self,value):
		self.params[24].value = value

	ivPitch = property(getIvPitch,setIvPitch, doc='24 : IV Pitch (-24.0,24.0)')

	def getIvTune(self):
		return self.params[25].value

	def setIvTune(self,value):
		self.params[25].value = value

	ivTune = property(getIvTune,setIvTune, doc='25 : IV Tune (-50.0,50.0)')

	def getIvGain(self):
		return self.params[26].value

	def setIvGain(self,value):
		self.params[26].value = value

	ivGain = property(getIvGain,setIvGain, doc='26 : IV Gain (0.0,1.0)')

	def getVOn(self):
		return self.params[27].value

	def setVOn(self,value):
		self.params[27].value = value

	vOn = property(getVOn,setVOn, doc='27 : V On (0.0,1.0:Q)')

	def getVPitch(self):
		return self.params[28].value

	def setVPitch(self,value):
		self.params[28].value = value

	vPitch = property(getVPitch,setVPitch, doc='28 : V Pitch (-24.0,24.0)')

	def getVTune(self):
		return self.params[29].value

	def setVTune(self,value):
		self.params[29].value = value

	vTune = property(getVTune,setVTune, doc='29 : V Tune (-50.0,50.0)')

	def getVGain(self):
		return self.params[30].value

	def setVGain(self,value):
		self.params[30].value = value

	vGain = property(getVGain,setVGain, doc='30 : V Gain (0.0,1.0)')

