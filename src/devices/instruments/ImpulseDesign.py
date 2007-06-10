class ImpulseDesign:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters
		self.createSlots()
		
	def createSlots(self):
		self.slots = [Slot(params,4),Slot(params,24),Slot(params,44),Slot(params,64)]

	def getSlot(self,index):
		return self.slots[index]

class Slot:
	
	def __init__(self,params,offset):
		self.params = params
		self.offset = offset
			