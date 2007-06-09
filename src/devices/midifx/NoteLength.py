class NoteLength:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value=None):
		if value != None:
			self.params[0].value = value
		return self.params[0].value

	def triggerMode(self,value=None):
		if value != None:
			self.params[1].value = value
		return self.params[1].value

	def syncOn(self,value=None):
		if value != None:
			self.params[2].value = value
		return self.params[2].value

	def syncedLength(self,value=None):
		if value != None:
			self.params[3].value = value
		return self.params[3].value

	def timeLength(self,value=None):
		if value != None:
			self.params[4].value = value
		return self.params[4].value

	def gate(self,value=None):
		if value != None:
			self.params[5].value = value
		return self.params[5].value

	def onOffBalance(self,value=None):
		if value != None:
			self.params[6].value = value
		return self.params[6].value

	def decayTime(self,value=None):
		if value != None:
			self.params[7].value = value
		return self.params[7].value

	def decayKeyScale(self,value=None):
		if value != None:
			self.params[8].value = value
		return self.params[8].value

