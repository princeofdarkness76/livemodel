class FilterDelay:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value):
		self.params[0].value = value

	def 1InputOn(self,value):
		self.params[1].value = value

	def 1EqOn(self,value):
		self.params[2].value = value

	def 1EqFreq(self,value):
		self.params[3].value = value

	def 1EqWidth(self,value):
		self.params[4].value = value

	def 1DelayMode(self,value):
		self.params[5].value = value

	def 1BeatDelay(self,value):
		self.params[6].value = value

	def 1BeatSwing(self,value):
		self.params[7].value = value

	def 1TimeDelay(self,value):
		self.params[8].value = value

	def 1Feedback(self,value):
		self.params[9].value = value

	def 1Pan(self,value):
		self.params[10].value = value

	def 1Volume(self,value):
		self.params[11].value = value

	def 2InputOn(self,value):
		self.params[12].value = value

	def 2EqOn(self,value):
		self.params[13].value = value

	def 2EqFreq(self,value):
		self.params[14].value = value

	def 2EqWidth(self,value):
		self.params[15].value = value

	def 2DelayMode(self,value):
		self.params[16].value = value

	def 2BeatDelay(self,value):
		self.params[17].value = value

	def 2BeatSwing(self,value):
		self.params[18].value = value

	def 2TimeDelay(self,value):
		self.params[19].value = value

	def 2Feedback(self,value):
		self.params[20].value = value

	def 2Pan(self,value):
		self.params[21].value = value

	def 2Volume(self,value):
		self.params[22].value = value

	def 3InputOn(self,value):
		self.params[23].value = value

	def 3EqOn(self,value):
		self.params[24].value = value

	def 3EqFreq(self,value):
		self.params[25].value = value

	def 3EqWidth(self,value):
		self.params[26].value = value

	def 3DelayMode(self,value):
		self.params[27].value = value

	def 3BeatDelay(self,value):
		self.params[28].value = value

	def 3BeatSwing(self,value):
		self.params[29].value = value

	def 3TimeDelay(self,value):
		self.params[30].value = value

	def 3Feedback(self,value):
		self.params[31].value = value

	def 3Pan(self,value):
		self.params[32].value = value

	def 3Volume(self,value):
		self.params[33].value = value

	def dry(self,value):
		self.params[34].value = value

