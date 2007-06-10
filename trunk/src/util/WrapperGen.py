import os
import Live

genDir = "D:/tmp/"

def generateAll():
    """
    Scan all the tracks in the current document and generate code for each device found
    """
    global genDir
    tracks = Live.Application.get_application().get_document().tracks
    for track in tracks:
        print "Generate devices from track " + track.name
        for device in track.devices:
            generate(os.path.join(genDir, track.name), device)
        
def generate(outDir, dev):
    """
    Generate a python class for controlling the supplied device
    """
    className = generateClassName(dev.name)
    
    if not os.path.exists(outDir):
        os.mkdir(outDir)
    
    outFile = os.path.join(outDir, className + ".py") 

    fout = open(outFile, "w")
    
    fout.write(createClassHeader(className))
    
    for index in range(len(dev.parameters)):
        param = dev.parameters[index]
        fout.write(createProperty(param,index))
        
    fout.close()
    print "wrote " + dev.name

def createClassHeader(className):
    """Create class header and constructor function"""
    
    header = createLine(0,"from LiveModel import DeviceBase",1)
    header += createLine(0,"class " + className + "(DeviceBase):",1)
    header += createLine(1,"def __init__(self,device):")
    header += createLine(2,"DeviceBase.__init__(self, device)",1)

    return header

def createProperty(param, index):
    """Create getter method, setter method and property declaration"""
    
    paramName = param.name
    
    methodNamePart = generateCamelCase(paramName)
    
    getterName = "get" + methodNamePart
    setterName = "set" + methodNamePart
    
    getMethod = createLine(1,"def " + getterName + "(self):")
    getMethod += createLine(2,"return self.params[" + str(index) + "].value",1)
    
    setMethod = createLine(1,"def " + setterName + "(self,value):")
    setMethod += createLine(2,"self.params[" + str(index) + "].value = value",1)
    
    docString = str(index) + " : " + paramName
    
    if param.is_quantized:
        docString += " (" + str(param.min) + "," + str(param.max) + ":Q)"
    else:
        docString += " (" + str(param.min) + "," + str(param.max) + ")"
        
    property = createLine(1,generatePropertyName(paramName) + " = property(" + getterName + "," + setterName + ", doc='" + docString + "')" ,1)

    return getMethod + setMethod + property

def createLine(numTabs,code,extraNewline = 0):
    """
    Create a line of python code with the required number of leading tabs.
    Adds one newline by default, or two if you request the extraNewline
    """
        
    out = ""
    while numTabs > 0:
        out += "\t"
        numTabs -= 1
    
    out += code + "\n"
    
    if extraNewline:
        out += "\n"
        
    return out

def generateClassName(name):
    """Create a suitable class name from the name of a device"""
    return "".join(name.split(" "))
    
def generateCamelCase(name):
    """Create a santized camel case string"""
    words = getWords(name)
    
    out = ""
    for word in words:
        out += sanitize(word).capitalize()
            
    return out

def generatePropertyName(name):
    """try to create a valid property name from the supplied parameter name"""
    words = getWords(name)
    
    out = sanitize(words[0]).lower()
    if(len(words) > 1):
        rest = words[1:]
        for word in rest:
            out += sanitize(word).capitalize()
            
    return out
    
def getWords(name):
    """convert a parameter name into a list of words"""
    
    words = fixMappingOrder(name.replace("/"," ").split(" "))
    return words

def sanitize(word):
    """Strip out chars that arent valid method / property names"""
    
    return word.replace("(","").replace(")","").replace(".","").replace("-","")

def fixMappingOrder(words):
    """
    For parameter names that show modulation mappings such as 'Lev < Vel' or 'Filter <- Vel' 
    swap the word order and insert a 'To'. e.g. Lev < Vel becomes VelToLev 
    and Filter <- Vel becomes VelToFilter
    """
    
    out = []
    
    i = 0
    while i < len(words):
        word = words[i]
        if(word == "<-" or word == "<"):
            tmp = out[i - 1]
            out[i - 1] = words[i + 1]
            out.append("To")
            out.append(tmp)
            i = i + 1
        elif word.find("<") != -1:
            pos = word.find("<")
            left = word[:pos]
            right = word[pos+1:]
            out.append(right)
            out.append("To")
            out.append(left)
        elif word.find("<-") != -1:
            pos = word.find("<") != -1
            left = word[:pos]
            right = word[pos+2:]
            out.append(right)
            out.append("To")
            out.append(left)
        else:
            out.append(word)
            
        i = i + 1
        
    return out
