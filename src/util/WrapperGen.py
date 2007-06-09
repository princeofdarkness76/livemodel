import os
import Live

genDir = "D:/tmp/"

def generateAll():
    tracks = Live.Application.get_application().get_document().tracks
    for track in tracks:
        for device in track.devices:
            generate(track.name, device)
        
def generate(folder, dev):
    global genDir
    className = generateClassName(dev.name)
    outDir = os.path.join(genDir,folder)
    
    if not os.path.exists(outDir):
        os.mkdir(outDir)
    
    outFile = os.path.join(outDir, className + ".py") 

    fout = open(outFile, "w")
    
    fout.write("class " + className + ":\n\n")
    fout.write("\tdef __init__(self,device):\n")
    fout.write("\t\tself.device = device\n")
    fout.write("\t\tself.params = device.parameters\n\n")
    
    for index in range(len(dev.parameters)):
        param = dev.parameters[index]
        methodName = generateMethodName(param.name)
        if not methodName.isalnum():
            print methodName + " of " + className + " isnt alphanumeric"
        fout.write("\tdef " + generateMethodName(param.name) + "(self,value):\n")
        fout.write("\t\tself.params[" + str(index) + "].value = value\n\n")

    fout.close()
    print "wrote " + dev.name
    
def generateClassName(name):
    return "".join(name.split(" "))
    
def generateMethodName(name):
    name = sanitize(name)
    words = name.split(" ")
    
    out = words[0].lower()
    
    if(len(words) > 1):
        rest = words[1:]
        for word in rest:
            out += word.capitalize()
            
    return out

def sanitize(word):
    return word.replace("<-"," To ").replace("<"," To ").replace("/"," ").replace("(","").replace(")","").replace(".","").replace("-"," ")

def test():
    cname = "Auto Filter"
    mname = "LFO<-Env < (Random) Test."
    
    print generateClassName(cname)
    print generateMethodName(mname)
    
if __name__ == "__main__":
    test()