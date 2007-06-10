class FilterDelay:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def getDeviceOn(self):
		return self.params[0].value

	def setDeviceOn(self,value):
		self.params[0].value = value

	deviceOn = property(getDeviceOn,setDeviceOn, doc='0 : Device On (0.0,1.0:Q)')

	def get1InputOn(self):
		return self.params[1].value

	def set1InputOn(self,value):
		self.params[1].value = value

	1InputOn = property(get1InputOn,set1InputOn, doc='1 : 1 Input On (0.0,1.0:Q)')

	def get1EqOn(self):
		return self.params[2].value

	def set1EqOn(self,value):
		self.params[2].value = value

	1EqOn = property(get1EqOn,set1EqOn, doc='2 : 1 EQ On (0.0,1.0:Q)')

	def get1EqFreq(self):
		return self.params[3].value

	def set1EqFreq(self,value):
		self.params[3].value = value

	1EqFreq = property(get1EqFreq,set1EqFreq, doc='3 : 1 EQ Freq (0.0,1.0)')

	def get1EqWidth(self):
		return self.params[4].value

	def set1EqWidth(self,value):
		self.params[4].value = value

	1EqWidth = property(get1EqWidth,set1EqWidth, doc='4 : 1 EQ Width (0.5,9.0)')

	def get1DelayMode(self):
		return self.params[5].value

	def set1DelayMode(self,value):
		self.params[5].value = value

	1DelayMode = property(get1DelayMode,set1DelayMode, doc='5 : 1 Delay Mode (0.0,1.0:Q)')

	def get1BeatDelay(self):
		return self.params[6].value

	def set1BeatDelay(self,value):
		self.params[6].value = value

	1BeatDelay = property(get1BeatDelay,set1BeatDelay, doc='6 : 1 Beat Delay (0.0,7.0:Q)')

	def get1BeatSwing(self):
		return self.params[7].value

	def set1BeatSwing(self,value):
		self.params[7].value = value

	1BeatSwing = property(get1BeatSwing,set1BeatSwing, doc='7 : 1 Beat Swing (-0.333000004292,0.333000004292)')

	def get1TimeDelay(self):
		return self.params[8].value

	def set1TimeDelay(self,value):
		self.params[8].value = value

	1TimeDelay = property(get1TimeDelay,set1TimeDelay, doc='8 : 1 Time Delay (1.0,127.0)')

	def get1Feedback(self):
		return self.params[9].value

	def set1Feedback(self,value):
		self.params[9].value = value

	1Feedback = property(get1Feedback,set1Feedback, doc='9 : 1 Feedback (0.0,1.0)')

	def get1Pan(self):
		return self.params[10].value

	def set1Pan(self,value):
		self.params[10].value = value

	1Pan = property(get1Pan,set1Pan, doc='10 : 1 Pan (-1.0,1.0)')

	def get1Volume(self):
		return self.params[11].value

	def set1Volume(self,value):
		self.params[11].value = value

	1Volume = property(get1Volume,set1Volume, doc='11 : 1 Volume (0.0,1.0)')

	def get2InputOn(self):
		return self.params[12].value

	def set2InputOn(self,value):
		self.params[12].value = value

	2InputOn = property(get2InputOn,set2InputOn, doc='12 : 2 Input On (0.0,1.0:Q)')

	def get2EqOn(self):
		return self.params[13].value

	def set2EqOn(self,value):
		self.params[13].value = value

	2EqOn = property(get2EqOn,set2EqOn, doc='13 : 2 EQ On (0.0,1.0:Q)')

	def get2EqFreq(self):
		return self.params[14].value

	def set2EqFreq(self,value):
		self.params[14].value = value

	2EqFreq = property(get2EqFreq,set2EqFreq, doc='14 : 2 EQ Freq (0.0,1.0)')

	def get2EqWidth(self):
		return self.params[15].value

	def set2EqWidth(self,value):
		self.params[15].value = value

	2EqWidth = property(get2EqWidth,set2EqWidth, doc='15 : 2 EQ Width (0.5,9.0)')

	def get2DelayMode(self):
		return self.params[16].value

	def set2DelayMode(self,value):
		self.params[16].value = value

	2DelayMode = property(get2DelayMode,set2DelayMode, doc='16 : 2 Delay Mode (0.0,1.0:Q)')

	def get2BeatDelay(self):
		return self.params[17].value

	def set2BeatDelay(self,value):
		self.params[17].value = value

	2BeatDelay = property(get2BeatDelay,set2BeatDelay, doc='17 : 2 Beat Delay (0.0,7.0:Q)')

	def get2BeatSwing(self):
		return self.params[18].value

	def set2BeatSwing(self,value):
		self.params[18].value = value

	2BeatSwing = property(get2BeatSwing,set2BeatSwing, doc='18 : 2 Beat Swing (-0.333000004292,0.333000004292)')

	def get2TimeDelay(self):
		return self.params[19].value

	def set2TimeDelay(self,value):
		self.params[19].value = value

	2TimeDelay = property(get2TimeDelay,set2TimeDelay, doc='19 : 2 Time Delay (1.0,127.0)')

	def get2Feedback(self):
		return self.params[20].value

	def set2Feedback(self,value):
		self.params[20].value = value

	2Feedback = property(get2Feedback,set2Feedback, doc='20 : 2 Feedback (0.0,1.0)')

	def get2Pan(self):
		return self.params[21].value

	def set2Pan(self,value):
		self.params[21].value = value

	2Pan = property(get2Pan,set2Pan, doc='21 : 2 Pan (-1.0,1.0)')

	def get2Volume(self):
		return self.params[22].value

	def set2Volume(self,value):
		self.params[22].value = value

	2Volume = property(get2Volume,set2Volume, doc='22 : 2 Volume (0.0,1.0)')

	def get3InputOn(self):
		return self.params[23].value

	def set3InputOn(self,value):
		self.params[23].value = value

	3InputOn = property(get3InputOn,set3InputOn, doc='23 : 3 Input On (0.0,1.0:Q)')

	def get3EqOn(self):
		return self.params[24].value

	def set3EqOn(self,value):
		self.params[24].value = value

	3EqOn = property(get3EqOn,set3EqOn, doc='24 : 3 EQ On (0.0,1.0:Q)')

	def get3EqFreq(self):
		return self.params[25].value

	def set3EqFreq(self,value):
		self.params[25].value = value

	3EqFreq = property(get3EqFreq,set3EqFreq, doc='25 : 3 EQ Freq (0.0,1.0)')

	def get3EqWidth(self):
		return self.params[26].value

	def set3EqWidth(self,value):
		self.params[26].value = value

	3EqWidth = property(get3EqWidth,set3EqWidth, doc='26 : 3 EQ Width (0.5,9.0)')

	def get3DelayMode(self):
		return self.params[27].value

	def set3DelayMode(self,value):
		self.params[27].value = value

	3DelayMode = property(get3DelayMode,set3DelayMode, doc='27 : 3 Delay Mode (0.0,1.0:Q)')

	def get3BeatDelay(self):
		return self.params[28].value

	def set3BeatDelay(self,value):
		self.params[28].value = value

	3BeatDelay = property(get3BeatDelay,set3BeatDelay, doc='28 : 3 Beat Delay (0.0,7.0:Q)')

	def get3BeatSwing(self):
		return self.params[29].value

	def set3BeatSwing(self,value):
		self.params[29].value = value

	3BeatSwing = property(get3BeatSwing,set3BeatSwing, doc='29 : 3 Beat Swing (-0.333000004292,0.333000004292)')

	def get3TimeDelay(self):
		return self.params[30].value

	def set3TimeDelay(self,value):
		self.params[30].value = value

	3TimeDelay = property(get3TimeDelay,set3TimeDelay, doc='30 : 3 Time Delay (1.0,127.0)')

	def get3Feedback(self):
		return self.params[31].value

	def set3Feedback(self,value):
		self.params[31].value = value

	3Feedback = property(get3Feedback,set3Feedback, doc='31 : 3 Feedback (0.0,1.0)')

	def get3Pan(self):
		return self.params[32].value

	def set3Pan(self,value):
		self.params[32].value = value

	3Pan = property(get3Pan,set3Pan, doc='32 : 3 Pan (-1.0,1.0)')

	def get3Volume(self):
		return self.params[33].value

	def set3Volume(self,value):
		self.params[33].value = value

	3Volume = property(get3Volume,set3Volume, doc='33 : 3 Volume (0.0,1.0)')

	def getDry(self):
		return self.params[34].value

	def setDry(self,value):
		self.params[34].value = value

	dry = property(getDry,setDry, doc='34 : Dry (0.0,1.0)')

