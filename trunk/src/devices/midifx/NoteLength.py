class NoteLength:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters

	def getDeviceOn(self):
		return self.params[0].value

	def setDeviceOn(self,value):
		self.params[0].value = value

	deviceOn = property(getDeviceOn,setDeviceOn, doc='0 : Device On (0.0,1.0:Q)')

	def getTriggerMode(self):
		return self.params[1].value

	def setTriggerMode(self,value):
		self.params[1].value = value

	triggerMode = property(getTriggerMode,setTriggerMode, doc='1 : Trigger Mode (0.0,1.0:Q)')

	def getSyncOn(self):
		return self.params[2].value

	def setSyncOn(self,value):
		self.params[2].value = value

	syncOn = property(getSyncOn,setSyncOn, doc='2 : Sync On (0.0,1.0:Q)')

	def getSyncedLength(self):
		return self.params[3].value

	def setSyncedLength(self,value):
		self.params[3].value = value

	syncedLength = property(getSyncedLength,setSyncedLength, doc='3 : Synced Length (0.0,9.0)')

	def getTimeLength(self):
		return self.params[4].value

	def setTimeLength(self,value):
		self.params[4].value = value

	timeLength = property(getTimeLength,setTimeLength, doc='4 : Time Length (0.0,1.0)')

	def getGate(self):
		return self.params[5].value

	def setGate(self,value):
		self.params[5].value = value

	gate = property(getGate,setGate, doc='5 : Gate (1.0,200.0)')

	def getOnOffbalance(self):
		return self.params[6].value

	def setOnOffbalance(self,value):
		self.params[6].value = value

	onOffbalance = property(getOnOffbalance,setOnOffbalance, doc='6 : On/Off-Balance (0.0,100.0)')

	def getDecayTime(self):
		return self.params[7].value

	def setDecayTime(self,value):
		self.params[7].value = value

	decayTime = property(getDecayTime,setDecayTime, doc='7 : Decay Time (0.0,1.0)')

	def getDecayKeyScale(self):
		return self.params[8].value

	def setDecayKeyScale(self,value):
		self.params[8].value = value

	decayKeyScale = property(getDecayKeyScale,setDecayKeyScale, doc='8 : Decay Key Scale (-1.0,1.0)')

