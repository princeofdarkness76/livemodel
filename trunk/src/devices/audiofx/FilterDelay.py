class FilterDelay:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value=None):
		if value != None:
			self.params[0].value = value
		return self.params[0].value

	def 1InputOn(self,value=None):
		if value != None:
			self.params[1].value = value
		return self.params[1].value

	def 1EqOn(self,value=None):
		if value != None:
			self.params[2].value = value
		return self.params[2].value

	def 1EqFreq(self,value=None):
		if value != None:
			self.params[3].value = value
		return self.params[3].value

	def 1EqWidth(self,value=None):
		if value != None:
			self.params[4].value = value
		return self.params[4].value

	def 1DelayMode(self,value=None):
		if value != None:
			self.params[5].value = value
		return self.params[5].value

	def 1BeatDelay(self,value=None):
		if value != None:
			self.params[6].value = value
		return self.params[6].value

	def 1BeatSwing(self,value=None):
		if value != None:
			self.params[7].value = value
		return self.params[7].value

	def 1TimeDelay(self,value=None):
		if value != None:
			self.params[8].value = value
		return self.params[8].value

	def 1Feedback(self,value=None):
		if value != None:
			self.params[9].value = value
		return self.params[9].value

	def 1Pan(self,value=None):
		if value != None:
			self.params[10].value = value
		return self.params[10].value

	def 1Volume(self,value=None):
		if value != None:
			self.params[11].value = value
		return self.params[11].value

	def 2InputOn(self,value=None):
		if value != None:
			self.params[12].value = value
		return self.params[12].value

	def 2EqOn(self,value=None):
		if value != None:
			self.params[13].value = value
		return self.params[13].value

	def 2EqFreq(self,value=None):
		if value != None:
			self.params[14].value = value
		return self.params[14].value

	def 2EqWidth(self,value=None):
		if value != None:
			self.params[15].value = value
		return self.params[15].value

	def 2DelayMode(self,value=None):
		if value != None:
			self.params[16].value = value
		return self.params[16].value

	def 2BeatDelay(self,value=None):
		if value != None:
			self.params[17].value = value
		return self.params[17].value

	def 2BeatSwing(self,value=None):
		if value != None:
			self.params[18].value = value
		return self.params[18].value

	def 2TimeDelay(self,value=None):
		if value != None:
			self.params[19].value = value
		return self.params[19].value

	def 2Feedback(self,value=None):
		if value != None:
			self.params[20].value = value
		return self.params[20].value

	def 2Pan(self,value=None):
		if value != None:
			self.params[21].value = value
		return self.params[21].value

	def 2Volume(self,value=None):
		if value != None:
			self.params[22].value = value
		return self.params[22].value

	def 3InputOn(self,value=None):
		if value != None:
			self.params[23].value = value
		return self.params[23].value

	def 3EqOn(self,value=None):
		if value != None:
			self.params[24].value = value
		return self.params[24].value

	def 3EqFreq(self,value=None):
		if value != None:
			self.params[25].value = value
		return self.params[25].value

	def 3EqWidth(self,value=None):
		if value != None:
			self.params[26].value = value
		return self.params[26].value

	def 3DelayMode(self,value=None):
		if value != None:
			self.params[27].value = value
		return self.params[27].value

	def 3BeatDelay(self,value=None):
		if value != None:
			self.params[28].value = value
		return self.params[28].value

	def 3BeatSwing(self,value=None):
		if value != None:
			self.params[29].value = value
		return self.params[29].value

	def 3TimeDelay(self,value=None):
		if value != None:
			self.params[30].value = value
		return self.params[30].value

	def 3Feedback(self,value=None):
		if value != None:
			self.params[31].value = value
		return self.params[31].value

	def 3Pan(self,value=None):
		if value != None:
			self.params[32].value = value
		return self.params[32].value

	def 3Volume(self,value=None):
		if value != None:
			self.params[33].value = value
		return self.params[33].value

	def dry(self,value=None):
		if value != None:
			self.params[34].value = value
		return self.params[34].value

