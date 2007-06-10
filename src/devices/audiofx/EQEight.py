class EQEight:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def getDeviceOn(self):
		return self.params[0].value

	def setDeviceOn(self,value):
		self.params[0].value = value

	deviceOn = property(getDeviceOn,setDeviceOn, doc='0 : Device On (0.0,1.0:Q)')

	def getOutputGain(self):
		return self.params[1].value

	def setOutputGain(self,value):
		self.params[1].value = value

	outputGain = property(getOutputGain,setOutputGain, doc='1 : Output Gain (-12.0,12.0)')

	def getScale(self):
		return self.params[2].value

	def setScale(self,value):
		self.params[2].value = value

	scale = property(getScale,setScale, doc='2 : Scale (0.0,2.0)')

	def get1FilterOnA(self):
		return self.params[3].value

	def set1FilterOnA(self,value):
		self.params[3].value = value

	1FilterOnA = property(get1FilterOnA,set1FilterOnA, doc='3 : 1 Filter On A (0.0,1.0:Q)')

	def get1FilterTypeA(self):
		return self.params[4].value

	def set1FilterTypeA(self,value):
		self.params[4].value = value

	1FilterTypeA = property(get1FilterTypeA,set1FilterTypeA, doc='4 : 1 Filter Type A (0.0,4.0:Q)')

	def get1FrequencyA(self):
		return self.params[5].value

	def set1FrequencyA(self,value):
		self.params[5].value = value

	1FrequencyA = property(get1FrequencyA,set1FrequencyA, doc='5 : 1 Frequency A (0.0,1.0)')

	def get1GainA(self):
		return self.params[6].value

	def set1GainA(self,value):
		self.params[6].value = value

	1GainA = property(get1GainA,set1GainA, doc='6 : 1 Gain A (-15.0,15.0)')

	def get1ResonanceA(self):
		return self.params[7].value

	def set1ResonanceA(self,value):
		self.params[7].value = value

	1ResonanceA = property(get1ResonanceA,set1ResonanceA, doc='7 : 1 Resonance A (0.0,1.0)')

	def get1FilterOnB(self):
		return self.params[8].value

	def set1FilterOnB(self,value):
		self.params[8].value = value

	1FilterOnB = property(get1FilterOnB,set1FilterOnB, doc='8 : 1 Filter On B (0.0,1.0:Q)')

	def get1FilterTypeB(self):
		return self.params[9].value

	def set1FilterTypeB(self,value):
		self.params[9].value = value

	1FilterTypeB = property(get1FilterTypeB,set1FilterTypeB, doc='9 : 1 Filter Type B (0.0,4.0:Q)')

	def get1FrequencyB(self):
		return self.params[10].value

	def set1FrequencyB(self,value):
		self.params[10].value = value

	1FrequencyB = property(get1FrequencyB,set1FrequencyB, doc='10 : 1 Frequency B (0.0,1.0)')

	def get1GainB(self):
		return self.params[11].value

	def set1GainB(self,value):
		self.params[11].value = value

	1GainB = property(get1GainB,set1GainB, doc='11 : 1 Gain B (-15.0,15.0)')

	def get1ResonanceB(self):
		return self.params[12].value

	def set1ResonanceB(self,value):
		self.params[12].value = value

	1ResonanceB = property(get1ResonanceB,set1ResonanceB, doc='12 : 1 Resonance B (0.0,1.0)')

	def get2FilterOnA(self):
		return self.params[13].value

	def set2FilterOnA(self,value):
		self.params[13].value = value

	2FilterOnA = property(get2FilterOnA,set2FilterOnA, doc='13 : 2 Filter On A (0.0,1.0:Q)')

	def get2FilterTypeA(self):
		return self.params[14].value

	def set2FilterTypeA(self,value):
		self.params[14].value = value

	2FilterTypeA = property(get2FilterTypeA,set2FilterTypeA, doc='14 : 2 Filter Type A (0.0,4.0:Q)')

	def get2FrequencyA(self):
		return self.params[15].value

	def set2FrequencyA(self,value):
		self.params[15].value = value

	2FrequencyA = property(get2FrequencyA,set2FrequencyA, doc='15 : 2 Frequency A (0.0,1.0)')

	def get2GainA(self):
		return self.params[16].value

	def set2GainA(self,value):
		self.params[16].value = value

	2GainA = property(get2GainA,set2GainA, doc='16 : 2 Gain A (-15.0,15.0)')

	def get2ResonanceA(self):
		return self.params[17].value

	def set2ResonanceA(self,value):
		self.params[17].value = value

	2ResonanceA = property(get2ResonanceA,set2ResonanceA, doc='17 : 2 Resonance A (0.0,1.0)')

	def get2FilterOnB(self):
		return self.params[18].value

	def set2FilterOnB(self,value):
		self.params[18].value = value

	2FilterOnB = property(get2FilterOnB,set2FilterOnB, doc='18 : 2 Filter On B (0.0,1.0:Q)')

	def get2FilterTypeB(self):
		return self.params[19].value

	def set2FilterTypeB(self,value):
		self.params[19].value = value

	2FilterTypeB = property(get2FilterTypeB,set2FilterTypeB, doc='19 : 2 Filter Type B (0.0,4.0:Q)')

	def get2FrequencyB(self):
		return self.params[20].value

	def set2FrequencyB(self,value):
		self.params[20].value = value

	2FrequencyB = property(get2FrequencyB,set2FrequencyB, doc='20 : 2 Frequency B (0.0,1.0)')

	def get2GainB(self):
		return self.params[21].value

	def set2GainB(self,value):
		self.params[21].value = value

	2GainB = property(get2GainB,set2GainB, doc='21 : 2 Gain B (-15.0,15.0)')

	def get2ResonanceB(self):
		return self.params[22].value

	def set2ResonanceB(self,value):
		self.params[22].value = value

	2ResonanceB = property(get2ResonanceB,set2ResonanceB, doc='22 : 2 Resonance B (0.0,1.0)')

	def get3FilterOnA(self):
		return self.params[23].value

	def set3FilterOnA(self,value):
		self.params[23].value = value

	3FilterOnA = property(get3FilterOnA,set3FilterOnA, doc='23 : 3 Filter On A (0.0,1.0:Q)')

	def get3FilterTypeA(self):
		return self.params[24].value

	def set3FilterTypeA(self,value):
		self.params[24].value = value

	3FilterTypeA = property(get3FilterTypeA,set3FilterTypeA, doc='24 : 3 Filter Type A (0.0,4.0:Q)')

	def get3FrequencyA(self):
		return self.params[25].value

	def set3FrequencyA(self,value):
		self.params[25].value = value

	3FrequencyA = property(get3FrequencyA,set3FrequencyA, doc='25 : 3 Frequency A (0.0,1.0)')

	def get3GainA(self):
		return self.params[26].value

	def set3GainA(self,value):
		self.params[26].value = value

	3GainA = property(get3GainA,set3GainA, doc='26 : 3 Gain A (-15.0,15.0)')

	def get3ResonanceA(self):
		return self.params[27].value

	def set3ResonanceA(self,value):
		self.params[27].value = value

	3ResonanceA = property(get3ResonanceA,set3ResonanceA, doc='27 : 3 Resonance A (0.0,1.0)')

	def get3FilterOnB(self):
		return self.params[28].value

	def set3FilterOnB(self,value):
		self.params[28].value = value

	3FilterOnB = property(get3FilterOnB,set3FilterOnB, doc='28 : 3 Filter On B (0.0,1.0:Q)')

	def get3FilterTypeB(self):
		return self.params[29].value

	def set3FilterTypeB(self,value):
		self.params[29].value = value

	3FilterTypeB = property(get3FilterTypeB,set3FilterTypeB, doc='29 : 3 Filter Type B (0.0,4.0:Q)')

	def get3FrequencyB(self):
		return self.params[30].value

	def set3FrequencyB(self,value):
		self.params[30].value = value

	3FrequencyB = property(get3FrequencyB,set3FrequencyB, doc='30 : 3 Frequency B (0.0,1.0)')

	def get3GainB(self):
		return self.params[31].value

	def set3GainB(self,value):
		self.params[31].value = value

	3GainB = property(get3GainB,set3GainB, doc='31 : 3 Gain B (-15.0,15.0)')

	def get3ResonanceB(self):
		return self.params[32].value

	def set3ResonanceB(self,value):
		self.params[32].value = value

	3ResonanceB = property(get3ResonanceB,set3ResonanceB, doc='32 : 3 Resonance B (0.0,1.0)')

	def get4FilterOnA(self):
		return self.params[33].value

	def set4FilterOnA(self,value):
		self.params[33].value = value

	4FilterOnA = property(get4FilterOnA,set4FilterOnA, doc='33 : 4 Filter On A (0.0,1.0:Q)')

	def get4FilterTypeA(self):
		return self.params[34].value

	def set4FilterTypeA(self,value):
		self.params[34].value = value

	4FilterTypeA = property(get4FilterTypeA,set4FilterTypeA, doc='34 : 4 Filter Type A (0.0,4.0:Q)')

	def get4FrequencyA(self):
		return self.params[35].value

	def set4FrequencyA(self,value):
		self.params[35].value = value

	4FrequencyA = property(get4FrequencyA,set4FrequencyA, doc='35 : 4 Frequency A (0.0,1.0)')

	def get4GainA(self):
		return self.params[36].value

	def set4GainA(self,value):
		self.params[36].value = value

	4GainA = property(get4GainA,set4GainA, doc='36 : 4 Gain A (-15.0,15.0)')

	def get4ResonanceA(self):
		return self.params[37].value

	def set4ResonanceA(self,value):
		self.params[37].value = value

	4ResonanceA = property(get4ResonanceA,set4ResonanceA, doc='37 : 4 Resonance A (0.0,1.0)')

	def get4FilterOnB(self):
		return self.params[38].value

	def set4FilterOnB(self,value):
		self.params[38].value = value

	4FilterOnB = property(get4FilterOnB,set4FilterOnB, doc='38 : 4 Filter On B (0.0,1.0:Q)')

	def get4FilterTypeB(self):
		return self.params[39].value

	def set4FilterTypeB(self,value):
		self.params[39].value = value

	4FilterTypeB = property(get4FilterTypeB,set4FilterTypeB, doc='39 : 4 Filter Type B (0.0,4.0:Q)')

	def get4FrequencyB(self):
		return self.params[40].value

	def set4FrequencyB(self,value):
		self.params[40].value = value

	4FrequencyB = property(get4FrequencyB,set4FrequencyB, doc='40 : 4 Frequency B (0.0,1.0)')

	def get4GainB(self):
		return self.params[41].value

	def set4GainB(self,value):
		self.params[41].value = value

	4GainB = property(get4GainB,set4GainB, doc='41 : 4 Gain B (-15.0,15.0)')

	def get4ResonanceB(self):
		return self.params[42].value

	def set4ResonanceB(self,value):
		self.params[42].value = value

	4ResonanceB = property(get4ResonanceB,set4ResonanceB, doc='42 : 4 Resonance B (0.0,1.0)')

	def get5FilterOnA(self):
		return self.params[43].value

	def set5FilterOnA(self,value):
		self.params[43].value = value

	5FilterOnA = property(get5FilterOnA,set5FilterOnA, doc='43 : 5 Filter On A (0.0,1.0:Q)')

	def get5FilterTypeA(self):
		return self.params[44].value

	def set5FilterTypeA(self,value):
		self.params[44].value = value

	5FilterTypeA = property(get5FilterTypeA,set5FilterTypeA, doc='44 : 5 Filter Type A (0.0,4.0:Q)')

	def get5FrequencyA(self):
		return self.params[45].value

	def set5FrequencyA(self,value):
		self.params[45].value = value

	5FrequencyA = property(get5FrequencyA,set5FrequencyA, doc='45 : 5 Frequency A (0.0,1.0)')

	def get5GainA(self):
		return self.params[46].value

	def set5GainA(self,value):
		self.params[46].value = value

	5GainA = property(get5GainA,set5GainA, doc='46 : 5 Gain A (-15.0,15.0)')

	def get5ResonanceA(self):
		return self.params[47].value

	def set5ResonanceA(self,value):
		self.params[47].value = value

	5ResonanceA = property(get5ResonanceA,set5ResonanceA, doc='47 : 5 Resonance A (0.0,1.0)')

	def get5FilterOnB(self):
		return self.params[48].value

	def set5FilterOnB(self,value):
		self.params[48].value = value

	5FilterOnB = property(get5FilterOnB,set5FilterOnB, doc='48 : 5 Filter On B (0.0,1.0:Q)')

	def get5FilterTypeB(self):
		return self.params[49].value

	def set5FilterTypeB(self,value):
		self.params[49].value = value

	5FilterTypeB = property(get5FilterTypeB,set5FilterTypeB, doc='49 : 5 Filter Type B (0.0,4.0:Q)')

	def get5FrequencyB(self):
		return self.params[50].value

	def set5FrequencyB(self,value):
		self.params[50].value = value

	5FrequencyB = property(get5FrequencyB,set5FrequencyB, doc='50 : 5 Frequency B (0.0,1.0)')

	def get5GainB(self):
		return self.params[51].value

	def set5GainB(self,value):
		self.params[51].value = value

	5GainB = property(get5GainB,set5GainB, doc='51 : 5 Gain B (-15.0,15.0)')

	def get5ResonanceB(self):
		return self.params[52].value

	def set5ResonanceB(self,value):
		self.params[52].value = value

	5ResonanceB = property(get5ResonanceB,set5ResonanceB, doc='52 : 5 Resonance B (0.0,1.0)')

	def get6FilterOnA(self):
		return self.params[53].value

	def set6FilterOnA(self,value):
		self.params[53].value = value

	6FilterOnA = property(get6FilterOnA,set6FilterOnA, doc='53 : 6 Filter On A (0.0,1.0:Q)')

	def get6FilterTypeA(self):
		return self.params[54].value

	def set6FilterTypeA(self,value):
		self.params[54].value = value

	6FilterTypeA = property(get6FilterTypeA,set6FilterTypeA, doc='54 : 6 Filter Type A (0.0,4.0:Q)')

	def get6FrequencyA(self):
		return self.params[55].value

	def set6FrequencyA(self,value):
		self.params[55].value = value

	6FrequencyA = property(get6FrequencyA,set6FrequencyA, doc='55 : 6 Frequency A (0.0,1.0)')

	def get6GainA(self):
		return self.params[56].value

	def set6GainA(self,value):
		self.params[56].value = value

	6GainA = property(get6GainA,set6GainA, doc='56 : 6 Gain A (-15.0,15.0)')

	def get6ResonanceA(self):
		return self.params[57].value

	def set6ResonanceA(self,value):
		self.params[57].value = value

	6ResonanceA = property(get6ResonanceA,set6ResonanceA, doc='57 : 6 Resonance A (0.0,1.0)')

	def get6FilterOnB(self):
		return self.params[58].value

	def set6FilterOnB(self,value):
		self.params[58].value = value

	6FilterOnB = property(get6FilterOnB,set6FilterOnB, doc='58 : 6 Filter On B (0.0,1.0:Q)')

	def get6FilterTypeB(self):
		return self.params[59].value

	def set6FilterTypeB(self,value):
		self.params[59].value = value

	6FilterTypeB = property(get6FilterTypeB,set6FilterTypeB, doc='59 : 6 Filter Type B (0.0,4.0:Q)')

	def get6FrequencyB(self):
		return self.params[60].value

	def set6FrequencyB(self,value):
		self.params[60].value = value

	6FrequencyB = property(get6FrequencyB,set6FrequencyB, doc='60 : 6 Frequency B (0.0,1.0)')

	def get6GainB(self):
		return self.params[61].value

	def set6GainB(self,value):
		self.params[61].value = value

	6GainB = property(get6GainB,set6GainB, doc='61 : 6 Gain B (-15.0,15.0)')

	def get6ResonanceB(self):
		return self.params[62].value

	def set6ResonanceB(self,value):
		self.params[62].value = value

	6ResonanceB = property(get6ResonanceB,set6ResonanceB, doc='62 : 6 Resonance B (0.0,1.0)')

	def get7FilterOnA(self):
		return self.params[63].value

	def set7FilterOnA(self,value):
		self.params[63].value = value

	7FilterOnA = property(get7FilterOnA,set7FilterOnA, doc='63 : 7 Filter On A (0.0,1.0:Q)')

	def get7FilterTypeA(self):
		return self.params[64].value

	def set7FilterTypeA(self,value):
		self.params[64].value = value

	7FilterTypeA = property(get7FilterTypeA,set7FilterTypeA, doc='64 : 7 Filter Type A (0.0,4.0:Q)')

	def get7FrequencyA(self):
		return self.params[65].value

	def set7FrequencyA(self,value):
		self.params[65].value = value

	7FrequencyA = property(get7FrequencyA,set7FrequencyA, doc='65 : 7 Frequency A (0.0,1.0)')

	def get7GainA(self):
		return self.params[66].value

	def set7GainA(self,value):
		self.params[66].value = value

	7GainA = property(get7GainA,set7GainA, doc='66 : 7 Gain A (-15.0,15.0)')

	def get7ResonanceA(self):
		return self.params[67].value

	def set7ResonanceA(self,value):
		self.params[67].value = value

	7ResonanceA = property(get7ResonanceA,set7ResonanceA, doc='67 : 7 Resonance A (0.0,1.0)')

	def get7FilterOnB(self):
		return self.params[68].value

	def set7FilterOnB(self,value):
		self.params[68].value = value

	7FilterOnB = property(get7FilterOnB,set7FilterOnB, doc='68 : 7 Filter On B (0.0,1.0:Q)')

	def get7FilterTypeB(self):
		return self.params[69].value

	def set7FilterTypeB(self,value):
		self.params[69].value = value

	7FilterTypeB = property(get7FilterTypeB,set7FilterTypeB, doc='69 : 7 Filter Type B (0.0,4.0:Q)')

	def get7FrequencyB(self):
		return self.params[70].value

	def set7FrequencyB(self,value):
		self.params[70].value = value

	7FrequencyB = property(get7FrequencyB,set7FrequencyB, doc='70 : 7 Frequency B (0.0,1.0)')

	def get7GainB(self):
		return self.params[71].value

	def set7GainB(self,value):
		self.params[71].value = value

	7GainB = property(get7GainB,set7GainB, doc='71 : 7 Gain B (-15.0,15.0)')

	def get7ResonanceB(self):
		return self.params[72].value

	def set7ResonanceB(self,value):
		self.params[72].value = value

	7ResonanceB = property(get7ResonanceB,set7ResonanceB, doc='72 : 7 Resonance B (0.0,1.0)')

	def get8FilterOnA(self):
		return self.params[73].value

	def set8FilterOnA(self,value):
		self.params[73].value = value

	8FilterOnA = property(get8FilterOnA,set8FilterOnA, doc='73 : 8 Filter On A (0.0,1.0:Q)')

	def get8FilterTypeA(self):
		return self.params[74].value

	def set8FilterTypeA(self,value):
		self.params[74].value = value

	8FilterTypeA = property(get8FilterTypeA,set8FilterTypeA, doc='74 : 8 Filter Type A (0.0,4.0:Q)')

	def get8FrequencyA(self):
		return self.params[75].value

	def set8FrequencyA(self,value):
		self.params[75].value = value

	8FrequencyA = property(get8FrequencyA,set8FrequencyA, doc='75 : 8 Frequency A (0.0,1.0)')

	def get8GainA(self):
		return self.params[76].value

	def set8GainA(self,value):
		self.params[76].value = value

	8GainA = property(get8GainA,set8GainA, doc='76 : 8 Gain A (-15.0,15.0)')

	def get8ResonanceA(self):
		return self.params[77].value

	def set8ResonanceA(self,value):
		self.params[77].value = value

	8ResonanceA = property(get8ResonanceA,set8ResonanceA, doc='77 : 8 Resonance A (0.0,1.0)')

	def get8FilterOnB(self):
		return self.params[78].value

	def set8FilterOnB(self,value):
		self.params[78].value = value

	8FilterOnB = property(get8FilterOnB,set8FilterOnB, doc='78 : 8 Filter On B (0.0,1.0:Q)')

	def get8FilterTypeB(self):
		return self.params[79].value

	def set8FilterTypeB(self,value):
		self.params[79].value = value

	8FilterTypeB = property(get8FilterTypeB,set8FilterTypeB, doc='79 : 8 Filter Type B (0.0,4.0:Q)')

	def get8FrequencyB(self):
		return self.params[80].value

	def set8FrequencyB(self,value):
		self.params[80].value = value

	8FrequencyB = property(get8FrequencyB,set8FrequencyB, doc='80 : 8 Frequency B (0.0,1.0)')

	def get8GainB(self):
		return self.params[81].value

	def set8GainB(self,value):
		self.params[81].value = value

	8GainB = property(get8GainB,set8GainB, doc='81 : 8 Gain B (-15.0,15.0)')

	def get8ResonanceB(self):
		return self.params[82].value

	def set8ResonanceB(self,value):
		self.params[82].value = value

	8ResonanceB = property(get8ResonanceB,set8ResonanceB, doc='82 : 8 Resonance B (0.0,1.0)')

