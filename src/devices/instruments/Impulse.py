class Impulse:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters
		self.createSlots()
		
	def createSlots(self):
		self.slots = [Slot(params,4),Slot(params,24),Slot(params,44),Slot(params,64)]

	def getSlot(self,index):
		return self.slots[index]
		
	def on(self):
		self.params[0].value = 1
	
	def off(self):
		self.params[0].value = 0
		
	def volume(self,value):
		if value != None:
			self.params[1].value = value
		return self.params[1].value

	def time(self,value):
		if value != None:
			self.params[2].value = value
		return self.params[2].value

	def transpose(self,value):
		if value != None:
			self.params[3].value = value
		return self.params[3].value
	
class Slot:
	
	def __init__(self,params,offset):
		self.params = params
		self.offset = offset
		
	def start(self,value):
		if value != None:
			self.params[self.offset].value = value
		return self.params[self.offset].value

	def transpose(self,value):
		if value != None:
			self.params[self.offset + 1].value = value
		return self.params[self.offset + 1].value

	def velocityToTranspose(self,value):
		if value != None:
			self.params[self.offset + 2].value = value
		return self.params[self.offset + 2].value

	def randomTranspose(self,value):
		if value != None:
			self.params[self.offset + 3].value = value
		return self.params[self.offset + 3].value

	def stretchMode(self,value):
		if value != None:
			self.params[self.offset + 4].value = value
		return self.params[self.offset + 4].value

	def stretchFactor(self,value):
		if value != None:
			self.params[self.offset + 5].value = value
		return self.params[self.offset + 5].value

	def velocityToStretch(self,value):
		if value != None:
			self.params[self.offset + 6].value = value
		return self.params[self.offset + 6].value

	def saturatorDrive(self,value):
		if value != None:
			self.params[self.offset + 7].value = value
		return self.params[self.offset + 7].value

	def filterType(self,value):
		if value != None:
			self.params[self.offset + 8].value = value
		return self.params[self.offset + 8].value

	def filterFreq(self,value):
		if value != None:
			self.params[self.offset + 9].value = value
		return self.params[self.offset + 9].value

	def filterRes(self,value):
		if value != None:
			self.params[self.offset + 10].value = value
		return self.params[self.offset + 10].value

	def velocityToFilter(self,value):
		if value != None:
			self.params[self.offset + 11].value = value
		return self.params[self.offset + 11].value

	def randomFilter(self,value):
		if value != None:
			self.params[self.offset + 12].value = value
		return self.params[self.offset + 12].value

	def envelopeType(self,value):
		if value != None:
			self.params[self.offset + 13].value = value
		return self.params[self.offset + 13].value

	def envelopeDecay(self,value):
		if value != None:
			self.params[self.offset + 14].value = value
		return self.params[self.offset + 14].value

	def pan(self,value):
		if value != None:
			self.params[self.offset + 15].value = value
		return self.params[self.offset + 15].value

	def velocityToPan(self,value):
		if value != None:
			self.params[self.offset + 16].value = value
		return self.params[self.offset + 16].value

	def randomPan(self,value):
		if value != None:
			self.params[self.offset + 17].value = value
		return self.params[self.offset + 17].value

	def volume(self,value):
		if value != None:
			self.params[self.offset + 18].value = value
		return self.params[self.offset + 18].value

	def velocityAmount(self,value):
		if value != None:
			self.params[self.offset + 19].value = value
		return self.params[self.offset + 19].value
	