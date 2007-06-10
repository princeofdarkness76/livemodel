class OperatorDesign:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters
		self.oscillators = [Oscillator(self.params,14),Oscillator(self.params,39),Oscillator(self.params,64),Oscillator(self.params,89)]
		self.pitchEnv = Envelope(self.params, 117)
		self.lfo = LFO(self.params,128)
		self.filter = Filter(self.params,147)
		
	def getOscillator(self,index):
		return self.oscillators[index]

class Oscillator:
	
	def __init__(self,params,offset):
		self.params = params
		self.offset = offset
		self.envelope = Envelope(self.params,15)
		
class Filter:
	
	def __init__(self,params,offset):
		self.params = params
		self.offset = offset
		self.env = Envelope(self.params,self.offset + 8)
		
class LFO:
	
	def __init__(self,params,offset):
		self.params = params
		self.offset = offset
		self.env = Envelope(self.params,self.offset + 9)
		
		