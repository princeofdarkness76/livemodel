from LiveModel import DeviceBase

class Impulse(DeviceBase):

	def __init__(self,device):
		DeviceBase.__init__(self, device)

	def getDeviceOn(self):
		return self.params[0].value

	def setDeviceOn(self,value):
		self.params[0].value = value

	deviceOn = property(getDeviceOn,setDeviceOn, doc='0 : Device On (0.0,1.0:Q)')

	def getGlobalVolume(self):
		return self.params[1].value

	def setGlobalVolume(self,value):
		self.params[1].value = value

	globalVolume = property(getGlobalVolume,setGlobalVolume, doc='1 : Global Volume (-36.0,36.0)')

	def getGlobalTime(self):
		return self.params[2].value

	def setGlobalTime(self,value):
		self.params[2].value = value

	globalTime = property(getGlobalTime,setGlobalTime, doc='2 : Global Time (-1.0,1.0)')

	def getGlobalTranspose(self):
		return self.params[3].value

	def setGlobalTranspose(self,value):
		self.params[3].value = value

	globalTranspose = property(getGlobalTranspose,setGlobalTranspose, doc='3 : Global Transpose (-48.0,48.0)')

	def get1Start(self):
		return self.params[4].value

	def set1Start(self,value):
		self.params[4].value = value

	1Start = property(get1Start,set1Start, doc='4 : 1 Start (0.0,100.0)')

	def get1Transpose(self):
		return self.params[5].value

	def set1Transpose(self,value):
		self.params[5].value = value

	1Transpose = property(get1Transpose,set1Transpose, doc='5 : 1 Transpose (-48.0,48.0)')

	def get1VelToTranspose(self):
		return self.params[6].value

	def set1VelToTranspose(self,value):
		self.params[6].value = value

	1VelToTranspose = property(get1VelToTranspose,set1VelToTranspose, doc='6 : 1 Transpose <- Vel (0.0,1.0)')

	def get1RandomToTranspose(self):
		return self.params[7].value

	def set1RandomToTranspose(self,value):
		self.params[7].value = value

	1RandomToTranspose = property(get1RandomToTranspose,set1RandomToTranspose, doc='7 : 1 Transpose <- Random (0.0,1.0)')

	def get1StretchMode(self):
		return self.params[8].value

	def set1StretchMode(self,value):
		self.params[8].value = value

	1StretchMode = property(get1StretchMode,set1StretchMode, doc='8 : 1 Stretch Mode (0.0,1.0:Q)')

	def get1StretchFactor(self):
		return self.params[9].value

	def set1StretchFactor(self,value):
		self.params[9].value = value

	1StretchFactor = property(get1StretchFactor,set1StretchFactor, doc='9 : 1 Stretch Factor (-1.0,1.0)')

	def get1VelToStretch(self):
		return self.params[10].value

	def set1VelToStretch(self,value):
		self.params[10].value = value

	1VelToStretch = property(get1VelToStretch,set1VelToStretch, doc='10 : 1 Stretch <- Vel (-1.0,1.0)')

	def get1SaturatorDrive(self):
		return self.params[11].value

	def set1SaturatorDrive(self,value):
		self.params[11].value = value

	1SaturatorDrive = property(get1SaturatorDrive,set1SaturatorDrive, doc='11 : 1 Saturator Drive (0.0,36.0)')

	def get1FilterType(self):
		return self.params[12].value

	def set1FilterType(self,value):
		self.params[12].value = value

	1FilterType = property(get1FilterType,set1FilterType, doc='12 : 1 Filter Type (0.0,6.0:Q)')

	def get1FilterFreq(self):
		return self.params[13].value

	def set1FilterFreq(self,value):
		self.params[13].value = value

	1FilterFreq = property(get1FilterFreq,set1FilterFreq, doc='13 : 1 Filter Freq (0.0,1.0)')

	def get1FilterRes(self):
		return self.params[14].value

	def set1FilterRes(self,value):
		self.params[14].value = value

	1FilterRes = property(get1FilterRes,set1FilterRes, doc='14 : 1 Filter Res (0.0,1.0)')

	def get1VelToFilter(self):
		return self.params[15].value

	def set1VelToFilter(self,value):
		self.params[15].value = value

	1VelToFilter = property(get1VelToFilter,set1VelToFilter, doc='15 : 1 Filter <- Vel (0.0,1.0)')

	def get1RandomToFilter(self):
		return self.params[16].value

	def set1RandomToFilter(self,value):
		self.params[16].value = value

	1RandomToFilter = property(get1RandomToFilter,set1RandomToFilter, doc='16 : 1 Filter <- Random (0.0,1.0)')

	def get1EnvelopeType(self):
		return self.params[17].value

	def set1EnvelopeType(self,value):
		self.params[17].value = value

	1EnvelopeType = property(get1EnvelopeType,set1EnvelopeType, doc='17 : 1 Envelope Type (0.0,1.0:Q)')

	def get1EnvelopeDecay(self):
		return self.params[18].value

	def set1EnvelopeDecay(self,value):
		self.params[18].value = value

	1EnvelopeDecay = property(get1EnvelopeDecay,set1EnvelopeDecay, doc='18 : 1 Envelope Decay (0.0,1.0)')

	def get1Pan(self):
		return self.params[19].value

	def set1Pan(self,value):
		self.params[19].value = value

	1Pan = property(get1Pan,set1Pan, doc='19 : 1 Pan (-1.0,1.0)')

	def get1VelToPan(self):
		return self.params[20].value

	def set1VelToPan(self,value):
		self.params[20].value = value

	1VelToPan = property(get1VelToPan,set1VelToPan, doc='20 : 1 Pan <- Vel (0.0,1.0)')

	def get1RandomToPan(self):
		return self.params[21].value

	def set1RandomToPan(self,value):
		self.params[21].value = value

	1RandomToPan = property(get1RandomToPan,set1RandomToPan, doc='21 : 1 Pan <- Random (0.0,1.0)')

	def get1Volume(self):
		return self.params[22].value

	def set1Volume(self,value):
		self.params[22].value = value

	1Volume = property(get1Volume,set1Volume, doc='22 : 1 Volume (-36.0,36.0)')

	def get1VelToVolume(self):
		return self.params[23].value

	def set1VelToVolume(self,value):
		self.params[23].value = value

	1VelToVolume = property(get1VelToVolume,set1VelToVolume, doc='23 : 1 Volume <- Vel (0.0,1.0)')

	def get2Start(self):
		return self.params[24].value

	def set2Start(self,value):
		self.params[24].value = value

	2Start = property(get2Start,set2Start, doc='24 : 2 Start (0.0,100.0)')

	def get2Transpose(self):
		return self.params[25].value

	def set2Transpose(self,value):
		self.params[25].value = value

	2Transpose = property(get2Transpose,set2Transpose, doc='25 : 2 Transpose (-48.0,48.0)')

	def get2VelToTranspose(self):
		return self.params[26].value

	def set2VelToTranspose(self,value):
		self.params[26].value = value

	2VelToTranspose = property(get2VelToTranspose,set2VelToTranspose, doc='26 : 2 Transpose <- Vel (0.0,1.0)')

	def get2RandomToTranspose(self):
		return self.params[27].value

	def set2RandomToTranspose(self,value):
		self.params[27].value = value

	2RandomToTranspose = property(get2RandomToTranspose,set2RandomToTranspose, doc='27 : 2 Transpose <- Random (0.0,1.0)')

	def get2StretchMode(self):
		return self.params[28].value

	def set2StretchMode(self,value):
		self.params[28].value = value

	2StretchMode = property(get2StretchMode,set2StretchMode, doc='28 : 2 Stretch Mode (0.0,1.0:Q)')

	def get2StretchFactor(self):
		return self.params[29].value

	def set2StretchFactor(self,value):
		self.params[29].value = value

	2StretchFactor = property(get2StretchFactor,set2StretchFactor, doc='29 : 2 Stretch Factor (-1.0,1.0)')

	def get2VelToStretch(self):
		return self.params[30].value

	def set2VelToStretch(self,value):
		self.params[30].value = value

	2VelToStretch = property(get2VelToStretch,set2VelToStretch, doc='30 : 2 Stretch <- Vel (-1.0,1.0)')

	def get2SaturatorDrive(self):
		return self.params[31].value

	def set2SaturatorDrive(self,value):
		self.params[31].value = value

	2SaturatorDrive = property(get2SaturatorDrive,set2SaturatorDrive, doc='31 : 2 Saturator Drive (0.0,36.0)')

	def get2FilterType(self):
		return self.params[32].value

	def set2FilterType(self,value):
		self.params[32].value = value

	2FilterType = property(get2FilterType,set2FilterType, doc='32 : 2 Filter Type (0.0,6.0:Q)')

	def get2FilterFreq(self):
		return self.params[33].value

	def set2FilterFreq(self,value):
		self.params[33].value = value

	2FilterFreq = property(get2FilterFreq,set2FilterFreq, doc='33 : 2 Filter Freq (0.0,1.0)')

	def get2FilterRes(self):
		return self.params[34].value

	def set2FilterRes(self,value):
		self.params[34].value = value

	2FilterRes = property(get2FilterRes,set2FilterRes, doc='34 : 2 Filter Res (0.0,1.0)')

	def get2VelToFilter(self):
		return self.params[35].value

	def set2VelToFilter(self,value):
		self.params[35].value = value

	2VelToFilter = property(get2VelToFilter,set2VelToFilter, doc='35 : 2 Filter <- Vel (0.0,1.0)')

	def get2RandomToFilter(self):
		return self.params[36].value

	def set2RandomToFilter(self,value):
		self.params[36].value = value

	2RandomToFilter = property(get2RandomToFilter,set2RandomToFilter, doc='36 : 2 Filter <- Random (0.0,1.0)')

	def get2EnvelopeType(self):
		return self.params[37].value

	def set2EnvelopeType(self,value):
		self.params[37].value = value

	2EnvelopeType = property(get2EnvelopeType,set2EnvelopeType, doc='37 : 2 Envelope Type (0.0,1.0:Q)')

	def get2EnvelopeDecay(self):
		return self.params[38].value

	def set2EnvelopeDecay(self,value):
		self.params[38].value = value

	2EnvelopeDecay = property(get2EnvelopeDecay,set2EnvelopeDecay, doc='38 : 2 Envelope Decay (0.0,1.0)')

	def get2Pan(self):
		return self.params[39].value

	def set2Pan(self,value):
		self.params[39].value = value

	2Pan = property(get2Pan,set2Pan, doc='39 : 2 Pan (-1.0,1.0)')

	def get2VelToPan(self):
		return self.params[40].value

	def set2VelToPan(self,value):
		self.params[40].value = value

	2VelToPan = property(get2VelToPan,set2VelToPan, doc='40 : 2 Pan <- Vel (0.0,1.0)')

	def get2RandomToPan(self):
		return self.params[41].value

	def set2RandomToPan(self,value):
		self.params[41].value = value

	2RandomToPan = property(get2RandomToPan,set2RandomToPan, doc='41 : 2 Pan <- Random (0.0,1.0)')

	def get2Volume(self):
		return self.params[42].value

	def set2Volume(self,value):
		self.params[42].value = value

	2Volume = property(get2Volume,set2Volume, doc='42 : 2 Volume (-36.0,36.0)')

	def get2VelToVolume(self):
		return self.params[43].value

	def set2VelToVolume(self,value):
		self.params[43].value = value

	2VelToVolume = property(get2VelToVolume,set2VelToVolume, doc='43 : 2 Volume <- Vel (0.0,1.0)')

	def get3Start(self):
		return self.params[44].value

	def set3Start(self,value):
		self.params[44].value = value

	3Start = property(get3Start,set3Start, doc='44 : 3 Start (0.0,100.0)')

	def get3Transpose(self):
		return self.params[45].value

	def set3Transpose(self,value):
		self.params[45].value = value

	3Transpose = property(get3Transpose,set3Transpose, doc='45 : 3 Transpose (-48.0,48.0)')

	def get3VelToTranspose(self):
		return self.params[46].value

	def set3VelToTranspose(self,value):
		self.params[46].value = value

	3VelToTranspose = property(get3VelToTranspose,set3VelToTranspose, doc='46 : 3 Transpose <- Vel (0.0,1.0)')

	def get3RandomToTranspose(self):
		return self.params[47].value

	def set3RandomToTranspose(self,value):
		self.params[47].value = value

	3RandomToTranspose = property(get3RandomToTranspose,set3RandomToTranspose, doc='47 : 3 Transpose <- Random (0.0,1.0)')

	def get3StretchMode(self):
		return self.params[48].value

	def set3StretchMode(self,value):
		self.params[48].value = value

	3StretchMode = property(get3StretchMode,set3StretchMode, doc='48 : 3 Stretch Mode (0.0,1.0:Q)')

	def get3StretchFactor(self):
		return self.params[49].value

	def set3StretchFactor(self,value):
		self.params[49].value = value

	3StretchFactor = property(get3StretchFactor,set3StretchFactor, doc='49 : 3 Stretch Factor (-1.0,1.0)')

	def get3VelToStretch(self):
		return self.params[50].value

	def set3VelToStretch(self,value):
		self.params[50].value = value

	3VelToStretch = property(get3VelToStretch,set3VelToStretch, doc='50 : 3 Stretch <- Vel (-1.0,1.0)')

	def get3SaturatorDrive(self):
		return self.params[51].value

	def set3SaturatorDrive(self,value):
		self.params[51].value = value

	3SaturatorDrive = property(get3SaturatorDrive,set3SaturatorDrive, doc='51 : 3 Saturator Drive (0.0,36.0)')

	def get3FilterType(self):
		return self.params[52].value

	def set3FilterType(self,value):
		self.params[52].value = value

	3FilterType = property(get3FilterType,set3FilterType, doc='52 : 3 Filter Type (0.0,6.0:Q)')

	def get3FilterFreq(self):
		return self.params[53].value

	def set3FilterFreq(self,value):
		self.params[53].value = value

	3FilterFreq = property(get3FilterFreq,set3FilterFreq, doc='53 : 3 Filter Freq (0.0,1.0)')

	def get3FilterRes(self):
		return self.params[54].value

	def set3FilterRes(self,value):
		self.params[54].value = value

	3FilterRes = property(get3FilterRes,set3FilterRes, doc='54 : 3 Filter Res (0.0,1.0)')

	def get3VelToFilter(self):
		return self.params[55].value

	def set3VelToFilter(self,value):
		self.params[55].value = value

	3VelToFilter = property(get3VelToFilter,set3VelToFilter, doc='55 : 3 Filter <- Vel (0.0,1.0)')

	def get3RandomToFilter(self):
		return self.params[56].value

	def set3RandomToFilter(self,value):
		self.params[56].value = value

	3RandomToFilter = property(get3RandomToFilter,set3RandomToFilter, doc='56 : 3 Filter <- Random (0.0,1.0)')

	def get3EnvelopeType(self):
		return self.params[57].value

	def set3EnvelopeType(self,value):
		self.params[57].value = value

	3EnvelopeType = property(get3EnvelopeType,set3EnvelopeType, doc='57 : 3 Envelope Type (0.0,1.0:Q)')

	def get3EnvelopeDecay(self):
		return self.params[58].value

	def set3EnvelopeDecay(self,value):
		self.params[58].value = value

	3EnvelopeDecay = property(get3EnvelopeDecay,set3EnvelopeDecay, doc='58 : 3 Envelope Decay (0.0,1.0)')

	def get3Pan(self):
		return self.params[59].value

	def set3Pan(self,value):
		self.params[59].value = value

	3Pan = property(get3Pan,set3Pan, doc='59 : 3 Pan (-1.0,1.0)')

	def get3VelToPan(self):
		return self.params[60].value

	def set3VelToPan(self,value):
		self.params[60].value = value

	3VelToPan = property(get3VelToPan,set3VelToPan, doc='60 : 3 Pan <- Vel (0.0,1.0)')

	def get3RandomToPan(self):
		return self.params[61].value

	def set3RandomToPan(self,value):
		self.params[61].value = value

	3RandomToPan = property(get3RandomToPan,set3RandomToPan, doc='61 : 3 Pan <- Random (0.0,1.0)')

	def get3Volume(self):
		return self.params[62].value

	def set3Volume(self,value):
		self.params[62].value = value

	3Volume = property(get3Volume,set3Volume, doc='62 : 3 Volume (-36.0,36.0)')

	def get3VelToVolume(self):
		return self.params[63].value

	def set3VelToVolume(self,value):
		self.params[63].value = value

	3VelToVolume = property(get3VelToVolume,set3VelToVolume, doc='63 : 3 Volume <- Vel (0.0,1.0)')

	def get4Start(self):
		return self.params[64].value

	def set4Start(self,value):
		self.params[64].value = value

	4Start = property(get4Start,set4Start, doc='64 : 4 Start (0.0,100.0)')

	def get4Transpose(self):
		return self.params[65].value

	def set4Transpose(self,value):
		self.params[65].value = value

	4Transpose = property(get4Transpose,set4Transpose, doc='65 : 4 Transpose (-48.0,48.0)')

	def get4VelToTranspose(self):
		return self.params[66].value

	def set4VelToTranspose(self,value):
		self.params[66].value = value

	4VelToTranspose = property(get4VelToTranspose,set4VelToTranspose, doc='66 : 4 Transpose <- Vel (0.0,1.0)')

	def get4RandomToTranspose(self):
		return self.params[67].value

	def set4RandomToTranspose(self,value):
		self.params[67].value = value

	4RandomToTranspose = property(get4RandomToTranspose,set4RandomToTranspose, doc='67 : 4 Transpose <- Random (0.0,1.0)')

	def get4StretchMode(self):
		return self.params[68].value

	def set4StretchMode(self,value):
		self.params[68].value = value

	4StretchMode = property(get4StretchMode,set4StretchMode, doc='68 : 4 Stretch Mode (0.0,1.0:Q)')

	def get4StretchFactor(self):
		return self.params[69].value

	def set4StretchFactor(self,value):
		self.params[69].value = value

	4StretchFactor = property(get4StretchFactor,set4StretchFactor, doc='69 : 4 Stretch Factor (-1.0,1.0)')

	def get4VelToStretch(self):
		return self.params[70].value

	def set4VelToStretch(self,value):
		self.params[70].value = value

	4VelToStretch = property(get4VelToStretch,set4VelToStretch, doc='70 : 4 Stretch <- Vel (-1.0,1.0)')

	def get4SaturatorDrive(self):
		return self.params[71].value

	def set4SaturatorDrive(self,value):
		self.params[71].value = value

	4SaturatorDrive = property(get4SaturatorDrive,set4SaturatorDrive, doc='71 : 4 Saturator Drive (0.0,36.0)')

	def get4FilterType(self):
		return self.params[72].value

	def set4FilterType(self,value):
		self.params[72].value = value

	4FilterType = property(get4FilterType,set4FilterType, doc='72 : 4 Filter Type (0.0,6.0:Q)')

	def get4FilterFreq(self):
		return self.params[73].value

	def set4FilterFreq(self,value):
		self.params[73].value = value

	4FilterFreq = property(get4FilterFreq,set4FilterFreq, doc='73 : 4 Filter Freq (0.0,1.0)')

	def get4FilterRes(self):
		return self.params[74].value

	def set4FilterRes(self,value):
		self.params[74].value = value

	4FilterRes = property(get4FilterRes,set4FilterRes, doc='74 : 4 Filter Res (0.0,1.0)')

	def get4VelToFilter(self):
		return self.params[75].value

	def set4VelToFilter(self,value):
		self.params[75].value = value

	4VelToFilter = property(get4VelToFilter,set4VelToFilter, doc='75 : 4 Filter <- Vel (0.0,1.0)')

	def get4RandomToFilter(self):
		return self.params[76].value

	def set4RandomToFilter(self,value):
		self.params[76].value = value

	4RandomToFilter = property(get4RandomToFilter,set4RandomToFilter, doc='76 : 4 Filter <- Random (0.0,1.0)')

	def get4EnvelopeType(self):
		return self.params[77].value

	def set4EnvelopeType(self,value):
		self.params[77].value = value

	4EnvelopeType = property(get4EnvelopeType,set4EnvelopeType, doc='77 : 4 Envelope Type (0.0,1.0:Q)')

	def get4EnvelopeDecay(self):
		return self.params[78].value

	def set4EnvelopeDecay(self,value):
		self.params[78].value = value

	4EnvelopeDecay = property(get4EnvelopeDecay,set4EnvelopeDecay, doc='78 : 4 Envelope Decay (0.0,1.0)')

	def get4Pan(self):
		return self.params[79].value

	def set4Pan(self,value):
		self.params[79].value = value

	4Pan = property(get4Pan,set4Pan, doc='79 : 4 Pan (-1.0,1.0)')

	def get4VelToPan(self):
		return self.params[80].value

	def set4VelToPan(self,value):
		self.params[80].value = value

	4VelToPan = property(get4VelToPan,set4VelToPan, doc='80 : 4 Pan <- Vel (0.0,1.0)')

	def get4RandomToPan(self):
		return self.params[81].value

	def set4RandomToPan(self,value):
		self.params[81].value = value

	4RandomToPan = property(get4RandomToPan,set4RandomToPan, doc='81 : 4 Pan <- Random (0.0,1.0)')

	def get4Volume(self):
		return self.params[82].value

	def set4Volume(self,value):
		self.params[82].value = value

	4Volume = property(get4Volume,set4Volume, doc='82 : 4 Volume (-36.0,36.0)')

	def get4VelToVolume(self):
		return self.params[83].value

	def set4VelToVolume(self,value):
		self.params[83].value = value

	4VelToVolume = property(get4VelToVolume,set4VelToVolume, doc='83 : 4 Volume <- Vel (0.0,1.0)')

	def get5Start(self):
		return self.params[84].value

	def set5Start(self,value):
		self.params[84].value = value

	5Start = property(get5Start,set5Start, doc='84 : 5 Start (0.0,100.0)')

	def get5Transpose(self):
		return self.params[85].value

	def set5Transpose(self,value):
		self.params[85].value = value

	5Transpose = property(get5Transpose,set5Transpose, doc='85 : 5 Transpose (-48.0,48.0)')

	def get5VelToTranspose(self):
		return self.params[86].value

	def set5VelToTranspose(self,value):
		self.params[86].value = value

	5VelToTranspose = property(get5VelToTranspose,set5VelToTranspose, doc='86 : 5 Transpose <- Vel (0.0,1.0)')

	def get5RandomToTranspose(self):
		return self.params[87].value

	def set5RandomToTranspose(self,value):
		self.params[87].value = value

	5RandomToTranspose = property(get5RandomToTranspose,set5RandomToTranspose, doc='87 : 5 Transpose <- Random (0.0,1.0)')

	def get5StretchMode(self):
		return self.params[88].value

	def set5StretchMode(self,value):
		self.params[88].value = value

	5StretchMode = property(get5StretchMode,set5StretchMode, doc='88 : 5 Stretch Mode (0.0,1.0:Q)')

	def get5StretchFactor(self):
		return self.params[89].value

	def set5StretchFactor(self,value):
		self.params[89].value = value

	5StretchFactor = property(get5StretchFactor,set5StretchFactor, doc='89 : 5 Stretch Factor (-1.0,1.0)')

	def get5VelToStretch(self):
		return self.params[90].value

	def set5VelToStretch(self,value):
		self.params[90].value = value

	5VelToStretch = property(get5VelToStretch,set5VelToStretch, doc='90 : 5 Stretch <- Vel (-1.0,1.0)')

	def get5SaturatorDrive(self):
		return self.params[91].value

	def set5SaturatorDrive(self,value):
		self.params[91].value = value

	5SaturatorDrive = property(get5SaturatorDrive,set5SaturatorDrive, doc='91 : 5 Saturator Drive (0.0,36.0)')

	def get5FilterType(self):
		return self.params[92].value

	def set5FilterType(self,value):
		self.params[92].value = value

	5FilterType = property(get5FilterType,set5FilterType, doc='92 : 5 Filter Type (0.0,6.0:Q)')

	def get5FilterFreq(self):
		return self.params[93].value

	def set5FilterFreq(self,value):
		self.params[93].value = value

	5FilterFreq = property(get5FilterFreq,set5FilterFreq, doc='93 : 5 Filter Freq (0.0,1.0)')

	def get5FilterRes(self):
		return self.params[94].value

	def set5FilterRes(self,value):
		self.params[94].value = value

	5FilterRes = property(get5FilterRes,set5FilterRes, doc='94 : 5 Filter Res (0.0,1.0)')

	def get5VelToFilter(self):
		return self.params[95].value

	def set5VelToFilter(self,value):
		self.params[95].value = value

	5VelToFilter = property(get5VelToFilter,set5VelToFilter, doc='95 : 5 Filter <- Vel (0.0,1.0)')

	def get5RandomToFilter(self):
		return self.params[96].value

	def set5RandomToFilter(self,value):
		self.params[96].value = value

	5RandomToFilter = property(get5RandomToFilter,set5RandomToFilter, doc='96 : 5 Filter <- Random (0.0,1.0)')

	def get5EnvelopeType(self):
		return self.params[97].value

	def set5EnvelopeType(self,value):
		self.params[97].value = value

	5EnvelopeType = property(get5EnvelopeType,set5EnvelopeType, doc='97 : 5 Envelope Type (0.0,1.0:Q)')

	def get5EnvelopeDecay(self):
		return self.params[98].value

	def set5EnvelopeDecay(self,value):
		self.params[98].value = value

	5EnvelopeDecay = property(get5EnvelopeDecay,set5EnvelopeDecay, doc='98 : 5 Envelope Decay (0.0,1.0)')

	def get5Pan(self):
		return self.params[99].value

	def set5Pan(self,value):
		self.params[99].value = value

	5Pan = property(get5Pan,set5Pan, doc='99 : 5 Pan (-1.0,1.0)')

	def get5VelToPan(self):
		return self.params[100].value

	def set5VelToPan(self,value):
		self.params[100].value = value

	5VelToPan = property(get5VelToPan,set5VelToPan, doc='100 : 5 Pan <- Vel (0.0,1.0)')

	def get5RandomToPan(self):
		return self.params[101].value

	def set5RandomToPan(self,value):
		self.params[101].value = value

	5RandomToPan = property(get5RandomToPan,set5RandomToPan, doc='101 : 5 Pan <- Random (0.0,1.0)')

	def get5Volume(self):
		return self.params[102].value

	def set5Volume(self,value):
		self.params[102].value = value

	5Volume = property(get5Volume,set5Volume, doc='102 : 5 Volume (-36.0,36.0)')

	def get5VelToVolume(self):
		return self.params[103].value

	def set5VelToVolume(self,value):
		self.params[103].value = value

	5VelToVolume = property(get5VelToVolume,set5VelToVolume, doc='103 : 5 Volume <- Vel (0.0,1.0)')

	def get6Start(self):
		return self.params[104].value

	def set6Start(self,value):
		self.params[104].value = value

	6Start = property(get6Start,set6Start, doc='104 : 6 Start (0.0,100.0)')

	def get6Transpose(self):
		return self.params[105].value

	def set6Transpose(self,value):
		self.params[105].value = value

	6Transpose = property(get6Transpose,set6Transpose, doc='105 : 6 Transpose (-48.0,48.0)')

	def get6VelToTranspose(self):
		return self.params[106].value

	def set6VelToTranspose(self,value):
		self.params[106].value = value

	6VelToTranspose = property(get6VelToTranspose,set6VelToTranspose, doc='106 : 6 Transpose <- Vel (0.0,1.0)')

	def get6RandomToTranspose(self):
		return self.params[107].value

	def set6RandomToTranspose(self,value):
		self.params[107].value = value

	6RandomToTranspose = property(get6RandomToTranspose,set6RandomToTranspose, doc='107 : 6 Transpose <- Random (0.0,1.0)')

	def get6StretchMode(self):
		return self.params[108].value

	def set6StretchMode(self,value):
		self.params[108].value = value

	6StretchMode = property(get6StretchMode,set6StretchMode, doc='108 : 6 Stretch Mode (0.0,1.0:Q)')

	def get6StretchFactor(self):
		return self.params[109].value

	def set6StretchFactor(self,value):
		self.params[109].value = value

	6StretchFactor = property(get6StretchFactor,set6StretchFactor, doc='109 : 6 Stretch Factor (-1.0,1.0)')

	def get6VelToStretch(self):
		return self.params[110].value

	def set6VelToStretch(self,value):
		self.params[110].value = value

	6VelToStretch = property(get6VelToStretch,set6VelToStretch, doc='110 : 6 Stretch <- Vel (-1.0,1.0)')

	def get6SaturatorDrive(self):
		return self.params[111].value

	def set6SaturatorDrive(self,value):
		self.params[111].value = value

	6SaturatorDrive = property(get6SaturatorDrive,set6SaturatorDrive, doc='111 : 6 Saturator Drive (0.0,36.0)')

	def get6FilterType(self):
		return self.params[112].value

	def set6FilterType(self,value):
		self.params[112].value = value

	6FilterType = property(get6FilterType,set6FilterType, doc='112 : 6 Filter Type (0.0,6.0:Q)')

	def get6FilterFreq(self):
		return self.params[113].value

	def set6FilterFreq(self,value):
		self.params[113].value = value

	6FilterFreq = property(get6FilterFreq,set6FilterFreq, doc='113 : 6 Filter Freq (0.0,1.0)')

	def get6FilterRes(self):
		return self.params[114].value

	def set6FilterRes(self,value):
		self.params[114].value = value

	6FilterRes = property(get6FilterRes,set6FilterRes, doc='114 : 6 Filter Res (0.0,1.0)')

	def get6VelToFilter(self):
		return self.params[115].value

	def set6VelToFilter(self,value):
		self.params[115].value = value

	6VelToFilter = property(get6VelToFilter,set6VelToFilter, doc='115 : 6 Filter <- Vel (0.0,1.0)')

	def get6RandomToFilter(self):
		return self.params[116].value

	def set6RandomToFilter(self,value):
		self.params[116].value = value

	6RandomToFilter = property(get6RandomToFilter,set6RandomToFilter, doc='116 : 6 Filter <- Random (0.0,1.0)')

	def get6EnvelopeType(self):
		return self.params[117].value

	def set6EnvelopeType(self,value):
		self.params[117].value = value

	6EnvelopeType = property(get6EnvelopeType,set6EnvelopeType, doc='117 : 6 Envelope Type (0.0,1.0:Q)')

	def get6EnvelopeDecay(self):
		return self.params[118].value

	def set6EnvelopeDecay(self,value):
		self.params[118].value = value

	6EnvelopeDecay = property(get6EnvelopeDecay,set6EnvelopeDecay, doc='118 : 6 Envelope Decay (0.0,1.0)')

	def get6Pan(self):
		return self.params[119].value

	def set6Pan(self,value):
		self.params[119].value = value

	6Pan = property(get6Pan,set6Pan, doc='119 : 6 Pan (-1.0,1.0)')

	def get6VelToPan(self):
		return self.params[120].value

	def set6VelToPan(self,value):
		self.params[120].value = value

	6VelToPan = property(get6VelToPan,set6VelToPan, doc='120 : 6 Pan <- Vel (0.0,1.0)')

	def get6RandomToPan(self):
		return self.params[121].value

	def set6RandomToPan(self,value):
		self.params[121].value = value

	6RandomToPan = property(get6RandomToPan,set6RandomToPan, doc='121 : 6 Pan <- Random (0.0,1.0)')

	def get6Volume(self):
		return self.params[122].value

	def set6Volume(self,value):
		self.params[122].value = value

	6Volume = property(get6Volume,set6Volume, doc='122 : 6 Volume (-36.0,36.0)')

	def get6VelToVolume(self):
		return self.params[123].value

	def set6VelToVolume(self,value):
		self.params[123].value = value

	6VelToVolume = property(get6VelToVolume,set6VelToVolume, doc='123 : 6 Volume <- Vel (0.0,1.0)')

	def get7Start(self):
		return self.params[124].value

	def set7Start(self,value):
		self.params[124].value = value

	7Start = property(get7Start,set7Start, doc='124 : 7 Start (0.0,100.0)')

	def get7Transpose(self):
		return self.params[125].value

	def set7Transpose(self,value):
		self.params[125].value = value

	7Transpose = property(get7Transpose,set7Transpose, doc='125 : 7 Transpose (-48.0,48.0)')

	def get7VelToTranspose(self):
		return self.params[126].value

	def set7VelToTranspose(self,value):
		self.params[126].value = value

	7VelToTranspose = property(get7VelToTranspose,set7VelToTranspose, doc='126 : 7 Transpose <- Vel (0.0,1.0)')

	def get7RandomToTranspose(self):
		return self.params[127].value

	def set7RandomToTranspose(self,value):
		self.params[127].value = value

	7RandomToTranspose = property(get7RandomToTranspose,set7RandomToTranspose, doc='127 : 7 Transpose <- Random (0.0,1.0)')

	def get7StretchMode(self):
		return self.params[128].value

	def set7StretchMode(self,value):
		self.params[128].value = value

	7StretchMode = property(get7StretchMode,set7StretchMode, doc='128 : 7 Stretch Mode (0.0,1.0:Q)')

	def get7StretchFactor(self):
		return self.params[129].value

	def set7StretchFactor(self,value):
		self.params[129].value = value

	7StretchFactor = property(get7StretchFactor,set7StretchFactor, doc='129 : 7 Stretch Factor (-1.0,1.0)')

	def get7VelToStretch(self):
		return self.params[130].value

	def set7VelToStretch(self,value):
		self.params[130].value = value

	7VelToStretch = property(get7VelToStretch,set7VelToStretch, doc='130 : 7 Stretch <- Vel (-1.0,1.0)')

	def get7SaturatorDrive(self):
		return self.params[131].value

	def set7SaturatorDrive(self,value):
		self.params[131].value = value

	7SaturatorDrive = property(get7SaturatorDrive,set7SaturatorDrive, doc='131 : 7 Saturator Drive (0.0,36.0)')

	def get7FilterType(self):
		return self.params[132].value

	def set7FilterType(self,value):
		self.params[132].value = value

	7FilterType = property(get7FilterType,set7FilterType, doc='132 : 7 Filter Type (0.0,6.0:Q)')

	def get7FilterFreq(self):
		return self.params[133].value

	def set7FilterFreq(self,value):
		self.params[133].value = value

	7FilterFreq = property(get7FilterFreq,set7FilterFreq, doc='133 : 7 Filter Freq (0.0,1.0)')

	def get7FilterRes(self):
		return self.params[134].value

	def set7FilterRes(self,value):
		self.params[134].value = value

	7FilterRes = property(get7FilterRes,set7FilterRes, doc='134 : 7 Filter Res (0.0,1.0)')

	def get7VelToFilter(self):
		return self.params[135].value

	def set7VelToFilter(self,value):
		self.params[135].value = value

	7VelToFilter = property(get7VelToFilter,set7VelToFilter, doc='135 : 7 Filter <- Vel (0.0,1.0)')

	def get7RandomToFilter(self):
		return self.params[136].value

	def set7RandomToFilter(self,value):
		self.params[136].value = value

	7RandomToFilter = property(get7RandomToFilter,set7RandomToFilter, doc='136 : 7 Filter <- Random (0.0,1.0)')

	def get7EnvelopeType(self):
		return self.params[137].value

	def set7EnvelopeType(self,value):
		self.params[137].value = value

	7EnvelopeType = property(get7EnvelopeType,set7EnvelopeType, doc='137 : 7 Envelope Type (0.0,1.0:Q)')

	def get7EnvelopeDecay(self):
		return self.params[138].value

	def set7EnvelopeDecay(self,value):
		self.params[138].value = value

	7EnvelopeDecay = property(get7EnvelopeDecay,set7EnvelopeDecay, doc='138 : 7 Envelope Decay (0.0,1.0)')

	def get7Pan(self):
		return self.params[139].value

	def set7Pan(self,value):
		self.params[139].value = value

	7Pan = property(get7Pan,set7Pan, doc='139 : 7 Pan (-1.0,1.0)')

	def get7VelToPan(self):
		return self.params[140].value

	def set7VelToPan(self,value):
		self.params[140].value = value

	7VelToPan = property(get7VelToPan,set7VelToPan, doc='140 : 7 Pan <- Vel (0.0,1.0)')

	def get7RandomToPan(self):
		return self.params[141].value

	def set7RandomToPan(self,value):
		self.params[141].value = value

	7RandomToPan = property(get7RandomToPan,set7RandomToPan, doc='141 : 7 Pan <- Random (0.0,1.0)')

	def get7Volume(self):
		return self.params[142].value

	def set7Volume(self,value):
		self.params[142].value = value

	7Volume = property(get7Volume,set7Volume, doc='142 : 7 Volume (-36.0,36.0)')

	def get7VelToVolume(self):
		return self.params[143].value

	def set7VelToVolume(self,value):
		self.params[143].value = value

	7VelToVolume = property(get7VelToVolume,set7VelToVolume, doc='143 : 7 Volume <- Vel (0.0,1.0)')

	def get8Start(self):
		return self.params[144].value

	def set8Start(self,value):
		self.params[144].value = value

	8Start = property(get8Start,set8Start, doc='144 : 8 Start (0.0,100.0)')

	def get8Transpose(self):
		return self.params[145].value

	def set8Transpose(self,value):
		self.params[145].value = value

	8Transpose = property(get8Transpose,set8Transpose, doc='145 : 8 Transpose (-48.0,48.0)')

	def get8VelToTranspose(self):
		return self.params[146].value

	def set8VelToTranspose(self,value):
		self.params[146].value = value

	8VelToTranspose = property(get8VelToTranspose,set8VelToTranspose, doc='146 : 8 Transpose <- Vel (0.0,1.0)')

	def get8RandomToTranspose(self):
		return self.params[147].value

	def set8RandomToTranspose(self,value):
		self.params[147].value = value

	8RandomToTranspose = property(get8RandomToTranspose,set8RandomToTranspose, doc='147 : 8 Transpose <- Random (0.0,1.0)')

	def get8StretchMode(self):
		return self.params[148].value

	def set8StretchMode(self,value):
		self.params[148].value = value

	8StretchMode = property(get8StretchMode,set8StretchMode, doc='148 : 8 Stretch Mode (0.0,1.0:Q)')

	def get8StretchFactor(self):
		return self.params[149].value

	def set8StretchFactor(self,value):
		self.params[149].value = value

	8StretchFactor = property(get8StretchFactor,set8StretchFactor, doc='149 : 8 Stretch Factor (-1.0,1.0)')

	def get8VelToStretch(self):
		return self.params[150].value

	def set8VelToStretch(self,value):
		self.params[150].value = value

	8VelToStretch = property(get8VelToStretch,set8VelToStretch, doc='150 : 8 Stretch <- Vel (-1.0,1.0)')

	def get8SaturatorDrive(self):
		return self.params[151].value

	def set8SaturatorDrive(self,value):
		self.params[151].value = value

	8SaturatorDrive = property(get8SaturatorDrive,set8SaturatorDrive, doc='151 : 8 Saturator Drive (0.0,36.0)')

	def get8FilterType(self):
		return self.params[152].value

	def set8FilterType(self,value):
		self.params[152].value = value

	8FilterType = property(get8FilterType,set8FilterType, doc='152 : 8 Filter Type (0.0,6.0:Q)')

	def get8FilterFreq(self):
		return self.params[153].value

	def set8FilterFreq(self,value):
		self.params[153].value = value

	8FilterFreq = property(get8FilterFreq,set8FilterFreq, doc='153 : 8 Filter Freq (0.0,1.0)')

	def get8FilterRes(self):
		return self.params[154].value

	def set8FilterRes(self,value):
		self.params[154].value = value

	8FilterRes = property(get8FilterRes,set8FilterRes, doc='154 : 8 Filter Res (0.0,1.0)')

	def get8VelToFilter(self):
		return self.params[155].value

	def set8VelToFilter(self,value):
		self.params[155].value = value

	8VelToFilter = property(get8VelToFilter,set8VelToFilter, doc='155 : 8 Filter <- Vel (0.0,1.0)')

	def get8RandomToFilter(self):
		return self.params[156].value

	def set8RandomToFilter(self,value):
		self.params[156].value = value

	8RandomToFilter = property(get8RandomToFilter,set8RandomToFilter, doc='156 : 8 Filter <- Random (0.0,1.0)')

	def get8EnvelopeType(self):
		return self.params[157].value

	def set8EnvelopeType(self,value):
		self.params[157].value = value

	8EnvelopeType = property(get8EnvelopeType,set8EnvelopeType, doc='157 : 8 Envelope Type (0.0,1.0:Q)')

	def get8EnvelopeDecay(self):
		return self.params[158].value

	def set8EnvelopeDecay(self,value):
		self.params[158].value = value

	8EnvelopeDecay = property(get8EnvelopeDecay,set8EnvelopeDecay, doc='158 : 8 Envelope Decay (0.0,1.0)')

	def get8Pan(self):
		return self.params[159].value

	def set8Pan(self,value):
		self.params[159].value = value

	8Pan = property(get8Pan,set8Pan, doc='159 : 8 Pan (-1.0,1.0)')

	def get8VelToPan(self):
		return self.params[160].value

	def set8VelToPan(self,value):
		self.params[160].value = value

	8VelToPan = property(get8VelToPan,set8VelToPan, doc='160 : 8 Pan <- Vel (0.0,1.0)')

	def get8RandomToPan(self):
		return self.params[161].value

	def set8RandomToPan(self,value):
		self.params[161].value = value

	8RandomToPan = property(get8RandomToPan,set8RandomToPan, doc='161 : 8 Pan <- Random (0.0,1.0)')

	def get8Volume(self):
		return self.params[162].value

	def set8Volume(self,value):
		self.params[162].value = value

	8Volume = property(get8Volume,set8Volume, doc='162 : 8 Volume (-36.0,36.0)')

	def get8VelToVolume(self):
		return self.params[163].value

	def set8VelToVolume(self,value):
		self.params[163].value = value

	8VelToVolume = property(get8VelToVolume,set8VelToVolume, doc='163 : 8 Volume <- Vel (0.0,1.0)')

