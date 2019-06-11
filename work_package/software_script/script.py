
import hashlib
import os,sys,shutil,codecs
import gzip
import time
from ctypes import *
import json
from pyzip import *

def ZipFile(srcfilepath):
    localfile = file(srcfilepath, "rb")
    filecontent = localfile.read()
    localfile.close()

    destfilepath = srcfilepath + ".gz"
    gf = gzip.open(destfilepath, "wb")
    gf.write(filecontent)
    gf.close()
 
def GetFileMd5(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = file(filename,'rb')
    while True:
        b = f.read(8096)
        if not b :
            break
        myhash.update(b)
    f.close()
    md5value = myhash.hexdigest()
    return md5value[8:-8]

def makeFile(filepath, isDeleteSrc):
    if not os.path.exists(filepath):
        return
    filename = os.path.basename(filepath)
    rootdir = os.path.dirname(filepath)
    (shotname, extension) = os.path.splitext(filename)
    strmd5 = GetFileMd5(filepath)
    newname = shotname + '-' + strmd5 + extension
    newfilepath = os.path.join(rootdir, newname)
    shutil.copy(filepath, newfilepath)
    ZipFile(newfilepath);
    zipFilePath = newfilepath + ".gz"
    strmd5 = GetFileMd5(zipFilePath)
    newname = shotname + '-' + strmd5 + extension + ".gz"
    newzipfilepath = os.path.join(rootdir, newname)
    os.rename(zipFilePath, newzipfilepath)
    filename = os.path.basename(newzipfilepath)
    filesize = os.path.getsize(newzipfilepath)
    strout = str(filesize) + ' ' + filename
    print strout

def updateETClientNsisScript(version) :
    scriptfilepath = 'D:/wamp/www/AppPack/ETClientinstall.nsi'
    if not os.path.exists(scriptfilepath) :
        print 'error1'
        return False, None
    
    fp = codecs.open(scriptfilepath, 'rb')
    filecontent = fp.read()
    fp.close()
    
    index = filecontent.find('PRODUCT_VERSION')
    if index < 0 :
        print 'error2'
        return False, None
    start = filecontent.find('\"', index)
    end = filecontent.find('\"', start + 1)
    newversion = version.replace('.', ',')
    substr = filecontent[start + 1: end]
    filecontent = filecontent.replace(substr, newversion)

    index = filecontent.find('FileVersion')
    if index < 0 :
        print 'error3'
        return False, None
    
    index = filecontent.find('\"', index + 1)
    start = filecontent.find('\"', index + 1)
    end = filecontent.find('\"', start + 1)
    substr = filecontent[start + 1: end]
    filecontent = filecontent.replace(substr, version, 2)
    
    start = version.rfind('.')
    filename = 'easyclientv' + version[start + 1 :] + '.exe'

    index = filecontent.find('OutFile')
    if index < 0 :
        print 'error4'
        return False, None
    start = filecontent.find('\"', index)
    end = filecontent.find('\"', start + 1)
    newversion = version.replace('.', ',')
    substr = filecontent[start + 1: end]
    filecontent = filecontent.replace(substr, filename)
    
    fp = codecs.open(scriptfilepath, 'wb')
    filecontent = fp.write(filecontent)
    fp.close()
    
    cmd = '"C:/Program Files (x86)/NSIS/makensis.exe" ' + scriptfilepath
    os.system(cmd)
    filepath = os.path.join(os.path.dirname(scriptfilepath), filename)
    if not os.path.exists(filepath) :
        return False, None

    return True, filepath
    
def makepackfile(srcfilepath) :
    dir = os.path.dirname(srcfilepath)
    myzip = ZFile(srcfilepath)
    myzip.extract_to(dir)
    myzip.close()
    index = srcfilepath.rfind('.')
    if index < 0 :
        return False

    basedir = srcfilepath[0:index]
    if not os.path.exists(dir):
        return False

    version = basedir[len(dir) + 1:]
    packfiledir = 'D:/wamp/www/AppPack/ETClientPack/'
    for filename in os.listdir(basedir):
        if filename == '.' or filename == '..' :
            continue
        filepath = os.path.join(basedir, filename)
        newfilepath = os.path.join(packfiledir, filename)
        if os.path.isfile(filepath):
            if (filename.rfind('.exe') > 0 or filename.rfind('.dll') > 0):
                os.system('D:/DigiSign/sign-with-pwd.bat ' + filepath)
            shutil.copy(filepath, newfilepath)
        elif not os.path.exists(filepath):
            os.mkdir(filepath)
            
    ret, packfilepath = updateETClientNsisScript(version)
    if not ret :
        return False
    
    os.system('D:/DigiSign/sign-with-pwd.bat ' + packfilepath)
    newfilepath = os.path.join(basedir, os.path.basename(packfilepath));
    shutil.move(packfilepath, newfilepath)
    
    for filename in os.listdir(basedir):
        if filename == '.' or filename == '..' :
            continue
        filepath = os.path.join(basedir, filename)
        if os.path.isfile(filepath):
            makeFile(filepath, True)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('not enough args')
        quit()
    if len(sys.argv) == 3:
        if sys.argv[2] == 'packfile' :
            makepackfile(sys.argv[1])
    else :
        makeFile(sys.argv[1], False)


