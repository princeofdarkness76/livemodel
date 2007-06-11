# LiveModel, a device model for controlling Ableton Live
# Copyright (C) 2007 Martin Wood-Mitrovski (martin@relivethefuture.com)
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# For questions regarding this module contact
# Martin Wood-Mitrovski 
# martin@relivethefuture.com

from random import *

class DeviceBase(object):
    
    def __init__(self,device):
        object.__init__(self)
        self.device = device
        self.params = device.parameters
        self.patches = []
        
    def storePatch(self,index = None):
        """
        Save a patch at the supplied index.
        If no index is supplied then the patch is just added to the end of the list.
        If the index is above the current capacity then fill the gap with empty lists
        """
        patch = []
        for param in self.params:
            patch.append(param.value)
        
        if index == None:
            self.patches.append(patch)
        else:
            numPatches = len(self.patches)
            if index >= numPatches:
                diff = index - numPatches
                while diff >= 0:
                    self.patches.append([])
                    diff -= 1
                    
            self.patches[index] = patch
        
    def loadPatch(self,index):
        """
        Load the patch at the supplied index
        """
        if index < len(self.patches):
            patch = self.patches[index]

            setPatch(patch)
        else:
            print "Index out of range"
    
    def setPatch(self,patch):
        """
        Copy the values from the supplied patch to the parameters
        """
        for i in range(len(patch)):
            self.params[i].value = patch[i]
            
    def interp(self,a,b,amount):
        """ 
        Linear patch interpolation. a and b are patch indexes.
        If one patch is empty then the other is loaded.
        """
        
        patchA = self.patches[a]
        patchB = self.patches[b]

        lenA = len(patchA)
        lenB = len(patchB)
        
        if(lenA == 0):
            if(lenB != 0):
                setPatch(patchB)
            else:
                print "both patches empty"
                return
            
        if(lenB == 0):
            if(lenA != 0):
                setPatch(patchA)
            else:
                print "both patches empty"
                return
            
        for i in range(len(patchA)):
            diff = patchB[i] - patchA[i]
            self.params[i].value = patchA[i] + (diff * amount)
            
    def bilinearInterp(self,a,b,c,d,x,y):
        """
        Bilinear interpolation between four patches, considered to be the four corners of the parameter
        space which ranges from 0 -> along both axes.
        a,b,c and d are patch indices. x and y are the co-ordinate values in the parameter space
        """
        patchA = self.patches[a]
        patchB = self.patches[b]
        patchC = self.patches[c]
        patchD = self.patches[d]

        x1 = 1 - x
        y1 = 1 - y
        
        for i in range(len(patchA)):
            f = (patchA[i] * y1) + (patchB[i] * y)
            g = (patchC[i] * y1) + (patchD[i] * y)
            self.params[i].value = (f * x1) + (g * x)
            
    def randomize(self,includeQuantized = 0):
        for param in self.params:
            if param.is_quantized and includeQuantized:
                diff = param.max - param.min
                param.value = param.min + (random() * diff)
            elif not param.is_quantized:
                diff = param.max - param.min
                param.value = param.min + (random() * diff)