import sys
import Live

errorLog = open("stderr.txt", "w")
errorLog.write("Starting Error Log")
sys.stderr = errorLog
stdoutLog = open("stdout.txt", "w")
sys.stdout = stdoutLog

pythonInstallDir = 'C:\\Python22'
sys.path.append(pythonInstallDir)
defaultPythonPaths = ['\\DLLs', '\\lib', '\\lib\\lib-tk', '\\lib\\site-packages', '\\lib\\site-packages\\win32', '\\lib\\plat-win']
for dir in defaultPythonPaths:
    path = pythonInstallDir + dir
    if path not in sys.path:
        sys.path.append(path)

from LiveFlash import LiveFlash

def create_instance(c_instance):
    return LiveFlash(c_instance)
