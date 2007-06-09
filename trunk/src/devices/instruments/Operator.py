class Operator:

	def __init__(self,device):
		self.device = device
		self.params = device.parameters
		self.oscillators = [Oscillator(self.params,14),Oscillator(self.params,39),Oscillator(self.params,64),Oscillator(self.params,89)]
		self.pitchEnv = Envelope(self.params, 117)
		self.lfo = LFO(self.params,128)
		self.filter = Filter(self.params,147)
		
	def getOscillator(self,index):
		return self.oscillators[index]
	
	def on(self):
		self.params[0].value = 1
	
	def off(self):
		self.params[0].value = 0

	def algorithm(self,value=None):
		if value != None:
			self.params[1].value = value
		return self.params[1].value

	def hiq(self,value=None):
		if value != None:
			self.params[2].value = value
		return self.params[2].value
		
	def transpose(self,value=None):
		if value != None:
			self.params[3].value = value
		return self.params[3].value
	
	def pitchBendRange(self,value=None):
		if value != None:
			self.params[4].value = value
		return self.params[4].value

	def volume(self,value=None):
		if value != None:
			self.params[5].value = value
		return self.params[5].value
	
	def panorama(self,value=None):
		if value != None:
			self.params[6].value = value
		return self.params[6].value
	
	def keyToPan(self,value=None):
		if value != None:
			self.params[7].value = value
		return self.params[7].value
			
	def randomPan(self,value=None):
		if value != None:
			self.params[8].value = value
		return self.params[8].value

	def opFeedback(self,value=None):
		if value != None:
			self.params[9].value = value
		return self.params[9].value

	def tone(self,value=None):
		if value != None:
			self.params[10].value = value
		return self.params[10].value

	def spread(self,value=None):
		if value != None:
			self.params[11].value = value
		return self.params[11].value

	def glideOn(self,value=None):
		if value != None:
			self.params[12].value = value
		return self.params[12].value

	def glideTime(self,value=None):
		if value != None:
			self.params[13].value = value
		return self.params[13].value

	def time(self,value=None):
		if value != None:
			self.params[114].value = value
		return self.params[114].value

	def keyToTime(self,value=None):
		if value != None:
			self.params[115].value = value
		return self.params[115].value

	def pitchEnvOn(self,value=None):
		if value != None:
			self.params[116].value = value
		return self.params[116].value

	def pitchEnvAmount(self,value=None):
		if value != None:
			self.params[127].value = value
		return self.params[127].value


class Oscillator:
	
	def __init__(self,params,offset):
		self.params = params
		self.offset = offset
		self.envelope = Envelope(self.params,15)
		
	def on(self,value=None):
		if value != None:
			self.params[self.offset].value = value
		return self.params[self.offset].value

	def coarse(self,value=None):
		if value != None:
			self.params[self.offset + 1].value = value
		return self.params[self.offset + 1].value

	def fine(self,value=None):
		if value != None:
			self.params[self.offset + 2].value = value
		return self.params[self.offset + 2].value

	def velocityToFreq(self,value=None):
		if value != None:
			self.params[self.offset + 3].value = value
		return self.params[self.offset + 3].value

	def quantize(self,value=None):
		if value != None:
			self.params[self.offset + 4].value = value
		return self.params[self.offset + 4].value

	def fixOn(self,value=None):
		if value != None:
			self.params[self.offset + 5].value = value
		return self.params[self.offset + 5].value

	def fixFreq(self,value=None):
		if value != None:
			self.params[self.offset + 6].value = value
		return self.params[self.offset + 6].value

	def fixFreqMul(self,value=None):
		if value != None:
			self.params[self.offset + 7].value = value
		return self.params[self.offset + 7].value

	def level(self,value=None):
		if value != None:
			self.params[self.offset + 8].value = value
		return self.params[self.offset + 8].value

	def phase(self,value=None):
		if value != None:
			self.params[self.offset + 9].value = value
		return self.params[self.offset + 9].value

	def pitchEnvAmount(self,value=None):
		if value != None:
			self.params[self.offset + 10].value = value
		return self.params[self.offset + 10].value

	def velocityToLevel(self,value=None):
		if value != None:
			self.params[self.offset + 11].value = value
		return self.params[self.offset + 11].value

	def keyToLevel(self,value=None):
		if value != None:
			self.params[self.offset + 12].value = value
		return self.params[self.offset + 12].value

	def wave(self,value=None):
		if value != None:
			self.params[self.offset + 13].value = value
		return self.params[self.offset + 13].value

	def lfoAmount(self,value=None):
		if value != None:
			self.params[self.offset + 14].value = value
		return self.params[self.offset + 14].value

class Filter:
	
	def __init__(self,params,offset):
		self.params = params
		self.offset = offset
		self.env = Envelope(self.params,self.offset + 8)
		
	def on(self,value=None):
		if value != None:
			self.params[self.offset].value = value
		return self.params[self.offset].value

	def type(self,value=None):
		if value != None:
			self.params[self.offset + 1].value = value
		return self.params[self.offset + 1].value

	def cutoff(self,value=None):
		if value != None:
			self.params[self.offset + 2].value = value
		return self.params[self.offset + 2].value

	def resonance(self,value=None):
		if value != None:
			self.params[self.offset + 3].value = value
		return self.params[self.offset + 3].value

	def velocityAmount(self,value=None):
		if value != None:
			self.params[self.offset + 4].value = value
		return self.params[self.offset + 4].value

	def keyAmount(self,value=None):
		if value != None:
			self.params[self.offset + 5].value = value
		return self.params[self.offset + 5].value

	def envAmount(self,value=None):
		if value != None:
			self.params[self.offset + 6].value = value
		return self.params[self.offset + 6].value

	def lfoAmount(self,value=None):
		if value != None:
			self.params[self.offset + 7].value = value
		return self.params[self.offset + 7].value
				
class LFO:
	
	def __init__(self,params,offset):
		self.params = params
		self.offset = offset
		self.env = Envelope(self.params,self.offset + 9)
		
	def on(self,value=None):
		if value != None:
			self.params[self.offset].value = value
		return self.params[self.offset].value

	def type(self,value=None):
		if value != None:
			self.params[self.offset + 1].value = value
		return self.params[self.offset + 1].value

	def range(self,value=None):
		if value != None:
			self.params[self.offset + 2].value = value
		return self.params[self.offset + 2].value

	def rate(self,value=None):
		if value != None:
			self.params[self.offset + 3].value = value
		return self.params[self.offset + 3].value

	def sync(self,value=None):
		if value != None:
			self.params[self.offset + 4].value = value
		return self.params[self.offset + 4].value

	def keyToRate(self,value=None):
		if value != None:
			self.params[self.offset + 5].value = value
		return self.params[self.offset + 5].value

	def mod(self,value=None):
		if value != None:
			self.params[self.offset + 6].value = value
		return self.params[self.offset + 6].value

	def velocity(self,value=None):
		if value != None:
			self.params[self.offset + 7].value = value
		return self.params[self.offset + 7].value

	def pitchEnvMod(self,value=None):
		if value != None:
			self.params[self.offset + 8].value = value
		return self.params[self.offset + 8].value

class Envelope:
	
	def __init__(self,params,offset):
		self.params = params
		self.offset = offset
		
	def attack(self,value=None):
		if value != None:
			self.params[self.offset].value = value
		return self.params[self.offset].value

	def init(self,value=None):
		if value != None:
			self.params[self.offset + 1].value = value
		return self.params[self.offset + 1].value

	def decay(self,value=None):
		if value != None:
			self.params[self.offset + 2].value = value
		return self.params[self.offset + 2].value

	def peak(self,value=None):
		if value != None:
			self.params[self.offset + 3].value = value
		return self.params[self.offset + 3].value

	def sustain(self,value=None):
		if value != None:
			self.params[self.offset + 4].value = value
		return self.params[self.offset + 4].value

	def release(self,value=None):
		if value != None:
			self.params[self.offset + 5].value = value
		return self.params[self.offset + 5].value

	def mode(self,value=None):
		if value != None:
			self.params[self.offset + 6].value = value
		return self.params[self.offset + 6].value

	def loop(self,value=None):
		if value != None:
			self.params[self.offset + 7].value = value
		return self.params[self.offset + 7].value

	def retrig(self,value=None):
		if value != None:
			self.params[self.offset + 8].value = value
		return self.params[self.offset + 8].value

	def velocityToRate(self,value=None):
		if value != None:
			self.params[self.offset + 9].value = value
		return self.params[self.offset + 9].value
		