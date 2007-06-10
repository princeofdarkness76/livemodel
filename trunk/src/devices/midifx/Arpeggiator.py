from LiveModel import DeviceBase

class Arpeggiator(DeviceBase):

	def __init__(self,device):
		DeviceBase.__init__(self, device)

	def getDeviceOn(self):
		return self.params[0].value

	def setDeviceOn(self,value):
		self.params[0].value = value

	deviceOn = property(getDeviceOn,setDeviceOn, doc='0 : Device On (0.0,1.0:Q)')

	def getStyle(self):
		return self.params[1].value

	def setStyle(self,value):
		self.params[1].value = value

	style = property(getStyle,setStyle, doc='1 : Style (0.0,17.0:Q)')

	def getOffset(self):
		return self.params[2].value

	def setOffset(self,value):
		self.params[2].value = value

	offset = property(getOffset,setOffset, doc='2 : Offset (-8.0,8.0)')

	def getRepeats(self):
		return self.params[3].value

	def setRepeats(self,value):
		self.params[3].value = value

	repeats = property(getRepeats,setRepeats, doc='3 : Repeats (0.0,16.0)')

	def getSyncOn(self):
		return self.params[4].value

	def setSyncOn(self,value):
		self.params[4].value = value

	syncOn = property(getSyncOn,setSyncOn, doc='4 : Sync On (0.0,1.0:Q)')

	def getSyncedRate(self):
		return self.params[5].value

	def setSyncedRate(self,value):
		self.params[5].value = value

	syncedRate = property(getSyncedRate,setSyncedRate, doc='5 : Synced Rate (0.0,9.0)')

	def getGroove(self):
		return self.params[6].value

	def setGroove(self,value):
		self.params[6].value = value

	groove = property(getGroove,setGroove, doc='6 : Groove (0.0,3.0:Q)')

	def getFreeRate(self):
		return self.params[7].value

	def setFreeRate(self,value):
		self.params[7].value = value

	freeRate = property(getFreeRate,setFreeRate, doc='7 : Free Rate (0.0,1.0)')

	def getGate(self):
		return self.params[8].value

	def setGate(self,value):
		self.params[8].value = value

	gate = property(getGate,setGate, doc='8 : Gate (1.0,200.0)')

	def getRetriggerMode(self):
		return self.params[9].value

	def setRetriggerMode(self,value):
		self.params[9].value = value

	retriggerMode = property(getRetriggerMode,setRetriggerMode, doc='9 : Retrigger Mode (0.0,2.0:Q)')

	def getRetInterval(self):
		return self.params[10].value

	def setRetInterval(self,value):
		self.params[10].value = value

	retInterval = property(getRetInterval,setRetInterval, doc='10 : Ret. Interval (0.0,8.0)')

	def getHoldOn(self):
		return self.params[11].value

	def setHoldOn(self,value):
		self.params[11].value = value

	holdOn = property(getHoldOn,setHoldOn, doc='11 : Hold On (0.0,1.0:Q)')

	def getTranposeMode(self):
		return self.params[12].value

	def setTranposeMode(self,value):
		self.params[12].value = value

	tranposeMode = property(getTranposeMode,setTranposeMode, doc='12 : Tranpose Mode (0.0,2.0:Q)')

	def getTranposeKey(self):
		return self.params[13].value

	def setTranposeKey(self,value):
		self.params[13].value = value

	tranposeKey = property(getTranposeKey,setTranposeKey, doc='13 : Tranpose Key (0.0,11.0:Q)')

	def getTranspSteps(self):
		return self.params[14].value

	def setTranspSteps(self,value):
		self.params[14].value = value

	transpSteps = property(getTranspSteps,setTranspSteps, doc='14 : Transp. Steps (0.0,8.0)')

	def getTranspDist(self):
		return self.params[15].value

	def setTranspDist(self,value):
		self.params[15].value = value

	transpDist = property(getTranspDist,setTranspDist, doc='15 : Transp. Dist. (-24.0,24.0)')

	def getVelocityOn(self):
		return self.params[16].value

	def setVelocityOn(self,value):
		self.params[16].value = value

	velocityOn = property(getVelocityOn,setVelocityOn, doc='16 : Velocity On (0.0,1.0:Q)')

	def getVelRetrigger(self):
		return self.params[17].value

	def setVelRetrigger(self,value):
		self.params[17].value = value

	velRetrigger = property(getVelRetrigger,setVelRetrigger, doc='17 : Vel. Retrigger (0.0,1.0:Q)')

	def getVelocityDecay(self):
		return self.params[18].value

	def setVelocityDecay(self,value):
		self.params[18].value = value

	velocityDecay = property(getVelocityDecay,setVelocityDecay, doc='18 : Velocity Decay (0.0,1.0)')

	def getVelocityTarget(self):
		return self.params[19].value

	def setVelocityTarget(self,value):
		self.params[19].value = value

	velocityTarget = property(getVelocityTarget,setVelocityTarget, doc='19 : Velocity Target (0.0,127.0)')

