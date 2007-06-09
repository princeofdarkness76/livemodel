class NoteLength:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def deviceOn(self,value):
		self.params[0].value = value

	def triggerMode(self,value):
		self.params[1].value = value

	def syncOn(self,value):
		self.params[2].value = value

	def syncedLength(self,value):
		self.params[3].value = value

	def timeLength(self,value):
		self.params[4].value = value

	def gate(self,value):
		self.params[5].value = value

	def onOffBalance(self,value):
		self.params[6].value = value

	def decayTime(self,value):
		self.params[7].value = value

	def decayKeyScale(self,value):
		self.params[8].value = value

