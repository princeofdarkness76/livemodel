from LiveModel import DeviceBase

class Scale(DeviceBase):

	def __init__(self,device):
		DeviceBase.__init__(self, device)

	def getDeviceOn(self):
		return self.params[0].value

	def setDeviceOn(self,value):
		self.params[0].value = value

	deviceOn = property(getDeviceOn,setDeviceOn, doc='0 : Device On (0.0,1.0:Q)')

	def getBase(self):
		return self.params[1].value

	def setBase(self,value):
		self.params[1].value = value

	base = property(getBase,setBase, doc='1 : Base (0.0,11.0)')

	def getTranspose(self):
		return self.params[2].value

	def setTranspose(self,value):
		self.params[2].value = value

	transpose = property(getTranspose,setTranspose, doc='2 : Transpose (-36.0,36.0)')

	def getFold(self):
		return self.params[3].value

	def setFold(self,value):
		self.params[3].value = value

	fold = property(getFold,setFold, doc='3 : Fold (0.0,1.0:Q)')

	def getLowest(self):
		return self.params[4].value

	def setLowest(self,value):
		self.params[4].value = value

	lowest = property(getLowest,setLowest, doc='4 : Lowest (0.0,127.0)')

	def getRange(self):
		return self.params[5].value

	def setRange(self,value):
		self.params[5].value = value

	range = property(getRange,setRange, doc='5 : Range (0.0,128.0)')

	def getMap0(self):
		return self.params[6].value

	def setMap0(self,value):
		self.params[6].value = value

	map0 = property(getMap0,setMap0, doc='6 : Map 0 (-1.0,12.0)')

	def getMap1(self):
		return self.params[7].value

	def setMap1(self,value):
		self.params[7].value = value

	map1 = property(getMap1,setMap1, doc='7 : Map 1 (-1.0,12.0)')

	def getMap2(self):
		return self.params[8].value

	def setMap2(self,value):
		self.params[8].value = value

	map2 = property(getMap2,setMap2, doc='8 : Map 2 (-1.0,12.0)')

	def getMap3(self):
		return self.params[9].value

	def setMap3(self,value):
		self.params[9].value = value

	map3 = property(getMap3,setMap3, doc='9 : Map 3 (-1.0,12.0)')

	def getMap4(self):
		return self.params[10].value

	def setMap4(self,value):
		self.params[10].value = value

	map4 = property(getMap4,setMap4, doc='10 : Map 4 (-1.0,12.0)')

	def getMap5(self):
		return self.params[11].value

	def setMap5(self,value):
		self.params[11].value = value

	map5 = property(getMap5,setMap5, doc='11 : Map 5 (-1.0,12.0)')

	def getMap6(self):
		return self.params[12].value

	def setMap6(self,value):
		self.params[12].value = value

	map6 = property(getMap6,setMap6, doc='12 : Map 6 (-1.0,12.0)')

	def getMap7(self):
		return self.params[13].value

	def setMap7(self,value):
		self.params[13].value = value

	map7 = property(getMap7,setMap7, doc='13 : Map 7 (-1.0,12.0)')

	def getMap8(self):
		return self.params[14].value

	def setMap8(self,value):
		self.params[14].value = value

	map8 = property(getMap8,setMap8, doc='14 : Map 8 (-1.0,12.0)')

	def getMap9(self):
		return self.params[15].value

	def setMap9(self,value):
		self.params[15].value = value

	map9 = property(getMap9,setMap9, doc='15 : Map 9 (-1.0,12.0)')

	def getMap10(self):
		return self.params[16].value

	def setMap10(self,value):
		self.params[16].value = value

	map10 = property(getMap10,setMap10, doc='16 : Map 10 (-1.0,12.0)')

	def getMap11(self):
		return self.params[17].value

	def setMap11(self,value):
		self.params[17].value = value

	map11 = property(getMap11,setMap11, doc='17 : Map 11 (-1.0,12.0)')

