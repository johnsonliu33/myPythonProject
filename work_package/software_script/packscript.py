#-*- coding: utf-8 -*-
import hashlib
import os,sys,shutil,codecs
import gzip
import time
from ctypes import *
import win32api
import time
import json
from work_package.software_script.pyzip import ZFile

global gIsBeta
global gAppName
global gupdateinfo

def getAppPackDir() :
    packdir = ''
    if gAppName == 'EasyClient' :
        packdir = 'D:/wamp/www/AppPack/ETClientPack'
    elif gAppName == 'EClassStudent':
        packdir = 'D:/wamp/www/AppPack/EClassStudentPack'
    elif gAppName == 'EClassTeacher':
        packdir = 'D:/wamp/www/AppPack/EClassTeacherPack'
    elif gAppName == 'ETutorTeacher':
        packdir = 'D:/wamp/www/AppPack/ETutorTeacherPack'
    elif gAppName == 'ETutorStudent':
        packdir = 'D:/wamp/www/AppPack/ETutorStudentPack'
    elif gAppName == 'GuideClassTeacher' :
        packdir = 'D:/wamp/www/AppPack/GuideClassTeacherPack'
    elif gAppName == 'GuideClassStudent' :
        packdir = 'D:/wamp/www/AppPack/GuideClassStudentPack'
    return packdir

def getAppPackScriptFilePath() :
    packdir = ''
    if gAppName == 'EasyClient' :
        packdir = 'D:/wamp/www/AppPack/ETClientinstall.nsi'
    elif gAppName == 'EClassStudent':
        packdir = 'D:/wamp/www/AppPack/EClassStudentinstall.nsi'
    elif gAppName == 'EClassTeacher':
        packdir = 'D:/wamp/www/AppPack/EClassTeacherinstall.nsi'
    elif gAppName == 'ETutorTeacher':
        packdir = 'D:/wamp/www/AppPack/ETutorTeacherinstall.nsi'
    elif gAppName == 'ETutorStudent':
        packdir = 'D:/wamp/www/AppPack/ETutorStudentinstall.nsi'
    elif gAppName == 'GuideClassTeacher' :
        packdir = 'D:/wamp/www/AppPack/GuideClassTeacherinstall.nsi'
    elif gAppName == 'GuideClassStudent' :
        packdir = 'D:/wamp/www/AppPack/GuideClassStudentinstall.nsi'
    return packdir

def getAppVersionInfoJsonFileName() :
    filename = ''
    if gAppName == 'EasyClient' :
        filename = 'EasyClient.json'
        if gIsBeta :
            filename = 'EasyClientBeta.json'
    elif gAppName == 'EClassStudent':
        filename = 'EClassStudent.json'
    elif gAppName == 'EClassTeacher':
        filename = 'EClassTeacher.json'
    elif gAppName == 'ETutorTeacher':
        filename = 'ETutorTeacher.json'
    elif gAppName == 'ETutorStudent':
        filename = 'ETutorStudent.json'
    elif gAppName == 'GuideClassTeacher' :
        filename = 'GuideClassTeacher.json'
    elif gAppName == 'GuideClassStudent' :
        filename = 'GuideClassStudent.json'
    return filename

def getAppGitDir() :
    packdir = ''
    if gAppName == 'EasyClient' :
        packdir = 'D:/AutomaticPublish/AutomaticPublishETClient'
        if gIsBeta :
            packdir = 'D:/AutomaticPublish/AutomaticPublishETClientBeta'
    elif gAppName == 'EClassStudent':
        packdir = 'D:/AutomaticPublish/AutomaticPublishEClassStudent'
    elif gAppName == 'EClassTeacher':
        packdir = 'D:/AutomaticPublish/AutomaticPublishEClassTeacher'
    elif gAppName == 'ETutorTeacher':
        packdir = 'D:/AutomaticPublish/AutomaticPublishETutorTeacher'
    elif gAppName == 'ETutorStudent':
        packdir = 'D:/AutomaticPublish/AutomaticPublishETutorStudent'
    elif gAppName == 'GuideClassTeacher' :
        packdir = 'D:/AutomaticPublish/AutomaticPublishGuideClassTeacher'
    elif gAppName == 'GuideClassStudent' :
        packdir = 'D:/AutomaticPublish/AutomaticPublishGuideClassStudent'

    if not os.path.exists(packdir) :
        os.mkdir(packdir)
    return packdir

def getAppType() :
    type = 0
    if gAppName == 'EClassStudent':
        type = 1
    elif gAppName == 'EClassTeacher':
        type = 2
    elif gAppName == 'ETutorStudent':
        type = 3
    elif gAppName == 'ETutorTeacher':
        type = 4
    elif gAppName == 'GuideClassTeacher' :
        type = 5
    elif gAppName == 'GuideClassStudent' :
        type = 6

    return type

def getAppPublishDir() :
    packdir = ''
    if gAppName == 'EasyClient' :
        packdir = 'D:/wamp/www/AppPack/ETClientPublishFiles'
    elif gAppName == 'EClassStudent':
        packdir = 'D:/wamp/www/AppPack/EClassStudentPublishFiles'
    elif gAppName == 'EClassTeacher':
        packdir = 'D:/wamp/www/AppPack/EClassTeacherPublishFiles'
    elif gAppName == 'ETutorTeacher':
        packdir = 'D:/wamp/www/AppPack/ETutorTeacherPublishFiles'
    elif gAppName == 'ETutorStudent':
        packdir = 'D:/wamp/www/AppPack/ETutorStudentPublishFiles'
    elif gAppName == 'GuideClassTeacher' :
        packdir = 'D:/wamp/www/AppPack/GuideClassTeacherPublishFiles'
    elif gAppName == 'GuideClassStudent' :
        packdir = 'D:/wamp/www/AppPack/GuideClassStudentPublishFiles'
    
    return packdir

def ZipFile(srcfilepath):
    with open(srcfilepath, "rb")as localfile:
        filecontent = localfile.read()

    destfilepath = srcfilepath + ".gz"
    gf = gzip.open(destfilepath, "wb")
    gf.write(filecontent)
    gf.close()
 
def GetFileMd5(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    with open(filename,'rb')as f:
        while True:
            b = f.read(8096)
            if not b :
                break
            myhash.update(b)
    md5value = myhash.hexdigest()
    return md5value[8:-8]

def getFileVersion(file_name):
    try :
        info = win32api.GetFileVersionInfo(file_name, os.sep)
        ms = info['FileVersionMS']
        ls = info['FileVersionLS']
        version = '%d.%d.%d.%04d' % (win32api.HIWORD(ms), win32api.LOWORD(ms), win32api.HIWORD(ls), win32api.LOWORD(ls))
        if len(version) < 1 :
            version == '0.0.0.0'
        return version
    except Exception as error:
        return '0.0.0.0'
    

def getCurVersionInfo() :
    dll = cdll.LoadLibrary('D:/wamp/www/pyscript/PythonGetETClientVersion.dll')
    strversionlen = 0
    outstrlen = c_int(strversionlen)

    try:
        pstr = dll.GetETClientVersionInfo(getAppType(), byref(outstrlen))
        strcontent = c_char_p(pstr)
        if outstrlen.value < 50 :
            return False, strcontent.value[:outstrlen.value]

        rst = json.loads(strcontent.value[:outstrlen.value])
        return True, rst
    except Exception as error:
        return False, u'从服务端获取版本信息失败'

def updateversionModulesinfo(filelist, appversioninfo):
    if len(filelist) < 1:
        return False
    
    modules = []
    if gAppName == 'EasyClient' :
        updatebetamodules = False
        if gIsBeta and 'BetaModules' in appversioninfo :
            updatebetamodules = True
        else :
            if 'Modules' not in appversioninfo :
                print (u'当前为正式版本发布，从服务端获取的版本信息没有正式版本数据')
                return False

        if updatebetamodules :
            modules = appversioninfo['BetaModules']
        else :
            modules = appversioninfo['Modules']
    else :
        modules = appversioninfo['Modules']

    moduleslen = len(modules)
    for filepath in filelist :
        if not os.path.exists(filepath):
            continue

        fileversion = '0.0.0.0'
        if filepath.find('.dll') > 0 or filepath.find('.exe') > 0 :
            fileversion = getFileVersion(filepath)

        filename = os.path.basename(filepath)
        rootdir = os.path.dirname(filepath)
        (shotname, extension) = os.path.splitext(filename)
        ZipFile(filepath);
        zipFilePath = filepath + ".gz"
        strmd5 = GetFileMd5(zipFilePath)
        newname = shotname + '-' + strmd5 + extension + ".gz"
        newzipfilepath = os.path.join(rootdir, newname)
        os.rename(zipFilePath, newzipfilepath)
        os.remove(filepath)
        filename = os.path.basename(newzipfilepath)
        filesize = os.path.getsize(newzipfilepath)

        index = filename.rfind('-')
        shortname = filename[:index + 1]
        index = filename.rfind('.')
        modulename = filename[:index]
        isBeta = False

        if moduleslen > 0 :
            for i in range(0, len(modules)) :
                if modules[i]['name'].find(shortname) >= 0 :
                    modules[i]['name'] = modulename
                    modules[i]['MD5'] = strmd5
                    modules[i]['bytes'] = filesize
                    if fileversion == '0.0.0.0' :
                        modules[i]['mustupdate'] = 'true'

                    modules[i]['version'] = fileversion
                    break

    return True

def updateETClientNsisScript(version) :
    scriptfilepath = getAppPackScriptFilePath()
    if not os.path.exists(scriptfilepath) :
        print ('error1')
        return False, None
    
    fp = codecs.open(scriptfilepath, 'rb')
    filecontent = fp.read()
    fp.close()
    
    index = filecontent.find('PRODUCT_VERSION')
    if index < 0 :
        print ('error2')
        return False, None
    start = filecontent.find('\"', index)
    end = filecontent.find('\"', start + 1)
    substr = filecontent[start + 1: end]
    filecontent = filecontent.replace(substr, version, 3)

    if gAppName == 'EasyClient' :
        start = version.rfind('.')
        filename = 'easyclientv' + version[start + 1 :] + '.exe'
    else :
        filename = gAppName + 'Setup' + version + '.exe'

    index = filecontent.find('OutFile')
    if index < 0 :
        print ('error4')
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

def updateversioninfo(curversion, appversioninfo):
    strnewversion = '/' + curversion + '/'
    urls = []

    if gAppName == 'EasyClient':
        updatebetainfo = False
        if gIsBeta and 'BetaDownloadUrls' in appversioninfo:
            updatebetainfo = True
        if updatebetainfo :
            urls = appversioninfo['BetaDownloadUrls']
            appversioninfo['BetaMainVersion'] = curversion
            appversioninfo['Beta'] = '1'
        else :
            urls = appversioninfo['DownloadUrls']
            appversioninfo['MainVersion'] = curversion
            appversioninfo['Beta'] = '0'
    else :
        urls = appversioninfo['DownloadUrls']
        appversioninfo['MainVersion'] = curversion

    for i in range(0, len(urls)) :
        index = urls[i].rfind('/')
        suburl = urls[i][:index]
        index = suburl.rfind('/')
        newurl = suburl[:index] + strnewversion
        urls[i] = newurl

def getAppVersionInfoFromOld(versioninfo) :
    appupdatelist = versioninfo['AppUpdateList']
    appversioninfo = {}

    for info in appupdatelist:
        if info['AppName'] == gAppName :
            appversioninfo = info
            break

    return appversioninfo

def getAppVersionInfo() :
    appversioninfo = {}
    ret, versioninfo = getCurVersionInfo()
    if not ret :
        return False, versioninfo

    if 'AppUpdateList' in versioninfo :
        appversioninfo = getAppVersionInfoFromOld(versioninfo)
    else :
        appversioninfo = versioninfo

    return True, appversioninfo

def cleardir(rmdir):
    for root, dirs, files in os.walk(rmdir, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))

def makeuploadgitscriptfile(version) :
    filename = 'uploadgit' + gAppName + '.bat'
    filepath = os.path.join('D:/wamp/www/pyscript', filename)
    if os.path.exists(filepath) :
        os.remove(filepath)

    gitinfo = 'git pull && git add * && git commit -m "upload publish file ' + gAppName + ' ' + version + '" && git push -u origin master \r\n'
    filecontent = '@echo off\r\n\r\n cd /d ' + getAppGitDir() + ' \r\n' + gitinfo
    fwrite = codecs.open(filepath, 'wb')
    fwrite.write(filecontent)
    fwrite.close()
    os.system(filepath)

def clearappgitdir() :
    filename = 'cleargit' + gAppName + '.bat'
    filepath = os.path.join('D:/wamp/www/pyscript', filename)
    if os.path.exists(filepath) :
        os.remove(filepath)

    filecontent = '@echo off\r\n\r\n cd /d ' + getAppGitDir() + '\r\n git reset --hard && git pull \r\n'
    fwrite = codecs.open(filepath, 'wb')
    fwrite.write(filecontent)
    fwrite.close()
    os.system(filepath)

def writejsonfile(filepath, info) :
    fwrite = codecs.open(filepath, 'wb')
    strContent = json.dumps(info)
    fwrite.write(strContent)
    fwrite.close()

def makeupdateinfojsonfile(basedir, offlineexefilepath, appversioninfo) :
    jsonfilename = getAppVersionInfoJsonFileName()
    if len(jsonfilename) < 1 :
        return False, u'客户端类型错误'

    versioninfo = {}
    if gAppName == 'EasyClient' :
        if 'BetaModules' in appversioninfo :
            if not gIsBeta :
                if 'Modules' not in appversioninfo :
                    return False, u'当前为正式版本发布，从服务端获取的版本信息没有正式版本数据'
                else :
                    versioninfo['Modules'] = appversioninfo['Modules']
                    versioninfo['MainVersion'] = appversioninfo['MainVersion']
                    versioninfo['DownloadUrls'] = appversioninfo['DownloadUrls']
                    versioninfo['AppName'] = appversioninfo['AppName']
            else :
                if 'Modules' in appversioninfo :
                    versioninfo['BetaModules'] = appversioninfo['BetaModules']
                    versioninfo['BetaMainVersion'] = appversioninfo['BetaMainVersion']
                    versioninfo['BetaDownloadUrls'] = appversioninfo['BetaDownloadUrls']
                    versioninfo['AppName'] = appversioninfo['AppName']
                    versioninfo['Beta'] = '1'
                else :
                    versioninfo = appversioninfo
        else :
            if gIsBeta :
                versioninfo['BetaModules'] = appversioninfo['Modules']
                versioninfo['BetaMainVersion'] = appversioninfo['MainVersion']
                versioninfo['BetaDownloadUrls'] = appversioninfo['DownloadUrls']
                versioninfo['AppName'] = appversioninfo['AppName']
                versioninfo['Beta'] = '1'
            else :
                versioninfo = appversioninfo
    else :
        versioninfo = appversioninfo

    strdownloadurl = ''
    if gIsBeta :
        strdownloadurl = versioninfo['BetaDownloadUrls'][0]
    else :
        strdownloadurl = versioninfo['DownloadUrls'][0]

    zipofflinefilepath = offlineexefilepath
    if gAppName != 'EasyClient' :
        index = offlineexefilepath.rfind('.exe')
        zipofflinefilepath = offlineexefilepath[0:index] + '.zip'

    versioninfo['InstallAddr'] = strdownloadurl + os.path.basename(offlineexefilepath)
    versioninfo['OfflineInstallAddr'] = strdownloadurl + os.path.basename(zipofflinefilepath)
    versioninfo['Tip'] = gupdateinfo
    versioninfo['Size'] = str(os.path.getsize(zipofflinefilepath) / 1024 / 1024)
    versioninfo['OS'] = 'XP/Vista/Win7/Win8/Win8.1/Win10'
    versioninfo['Date'] = time.strftime('%Y-%m-%d',time.localtime(time.time()))

    jsonFilePath = os.path.join(basedir, jsonfilename)
    writejsonfile(jsonFilePath, versioninfo)
    return True, 'ok'

def updatepublishfile(publishfilesdir, modulename, updatefiledir) :
    bupdate = False
    updatefilepath = ''
    for rootdir, dirs, files in os.walk(updatefiledir) :
        for filename in files :
            if filename.rfind('.gz') > 0 :
                index = filename.rfind('-')
                name = filename[:index]
                if name == modulename :
                    shutil.copy(os.path.join(updatefiledir, filename), os.path.join(publishfilesdir, filename))
                    bupdate = True
                    updatefilepath = os.path.join(updatefiledir, filename)
                    break
        if bupdate :
            break

    return bupdate, updatefilepath

def checkpublishfiles(srcdir, bupdate, newfiles) :
    publishfilesdir = getAppPublishDir()
    if not os.path.exists(publishfilesdir) :
        return False, '历史发布文件错误'

    updatefiles = []
    updatefilepaths = []
    for rootpath, dirs, files in os.walk(publishfilesdir) :
        for filename in files :
            index = filename.rfind('-')
            name = filename[:index]
            if name in newfiles :
                ret, updatefilepath = updatepublishfile(publishfilesdir, filename[:index], srcdir)
                if ret :
                    #os.remove(os.path.join(publishfilesdir, filename))
                    updatefiles.append(name)
            elif not bupdate :
                shutil.copy(os.path.join(publishfilesdir, filename), os.path.join(srcdir, filename))
        break

    if len(updatefiles) < len(newfiles) :
        jsonfilename = getAppVersionInfoJsonFileName()
        jsonfilepath = os.path.join(srcdir, jsonfilename)
        appversioninfo = {}
        with open(jsonfilepath, 'rb') as fread:
            appversioninfo = json.load(fread)

        modules = []
        unnetdir = getAppPackDir()
        if gIsBeta :
            modules = appversioninfo['BetaModules']
        else :
            modules = appversioninfo['Modules']

        for filename in newfiles :
            if filename not in updatefiles :
                ret, updatefilepath = updatepublishfile(publishfilesdir, filename, srcdir)
                if ret :
                    filename = os.path.basename(updatefilepath)
                    index = filename.rfind('.gz')
                    subname = filename[:index]
                    index = subname.rfind('.')
                    extension = subname[index:]
                    shortname = subname[:index]
                    index = shortname.rfind('-')
                    fileversion = '0.0.0.0'
                    module = {}
                    if extension.find('.exe') >= 0 or extension.find('.dll') >= 0:
                        name = shortname[:index] + extension
                        unnetfilepath = os.path.join(unnetdir, name)
                        fileversion = getFileVersion(unnetfilepath)

                    module['version'] = fileversion
                    module['MD5'] = shortname[index + 1:]
                    module['hasgzfile'] = 'true'
                    module['name'] = subname
                    module['registerdll'] = 'false'
                    module['bytes'] = os.path.getsize(updatefilepath)
                    if fileversion == '0.0.0.0':
                        module['mustupdate'] = 'true'
                    modules.append(module)

        writejsonfile(jsonfilepath, appversioninfo)

    return True, 'ok'

def dogitremoveaction(gitdir, rmfilename) :
    filename = 'updategit' + gAppName + '.bat'
    filepath = os.path.join('D:/wamp/www/pyscript', filename)

    filecontent = '@echo off\r\n\r\n cd /d ' + gitdir + ' \r\n git rm -r ' + rmfilename
    fwrite = codecs.open(filepath, 'wb')
    fwrite.write(filecontent)
    fwrite.close()
    os.system(filepath)

def updategitfiles(gitdir, srcdir, newfilenames) :
    for rootpath, dirs, files in os.walk(gitdir) :
        for filename in files :
            index = filename.rfind('-')
            name = filename[:index]
            if name in newfilenames :
                dogitremoveaction(gitdir, filename)

    for rootpath, dirs, files in os.walk(srcdir) :
        for filename in files :
            shutil.move(os.path.join(srcdir, filename), os.path.join(gitdir,filename))

def checkunusedir(srcdir) :
    for rootpath, dirs, files in os.walk(srcdir) :
        for dir in dirs :
            cleardir(dir)
            os.rmdir(dir)

def updateunupdatefileinfo(newfilenames, appversioninfo) :
    if len(newfilenames) < 1:
        return False
    
    modules = []
    if gAppName == 'EasyClient' :
        updatebetamodules = False
        if gIsBeta and 'BetaModules' in appversioninfo :
            updatebetamodules = True

        if updatebetamodules :
            modules = appversioninfo['BetaModules']
        else :
            modules = appversioninfo['Modules']
    else :
        modules = appversioninfo['Modules']

    if len(modules) < 1 :
        return False

    for i in range(0, len(modules)) :
        modulename = modules[i]['name']
        index = modulename.rfind('-')
        subname = modulename[:index]
        if subname not in newfilenames and modules[i].has_key('mustupdate'):
            modules[i]['mustupdate'] = 'false'

    return True

def makepackfile(srcfilepath) :
    index = srcfilepath.rfind('.')
    if index < 0 :
        return False, '文件上传失败'
    basedir = srcfilepath[0:index]
    if os.path.exists(basedir):
        cleardir(basedir)

    try :
        dir = os.path.dirname(srcfilepath)
        myzip = ZFile(srcfilepath)
        myzip.extract_to(dir)
        myzip.close()
    except Exception as error:
        return False, str(error)

    if not os.path.exists(basedir):
        return False, '上传文件解压缩失败'

    version = basedir[len(dir) + 1:]
    packfiledir = getAppPackDir()
    newfiles = []
    newfilenames = []
    for filename in os.listdir(basedir):
        if filename == '.' or filename == '..' :
            continue
        filepath = os.path.join(basedir, filename)
        newfilepath = os.path.join(packfiledir, filename)
        if os.path.isfile(filepath):
            newfiles.append(filepath)
            (shotname, extension) = os.path.splitext(filename)
            newfilenames.append(shotname)
            if (filename.rfind('.exe') > 0 or filename.rfind('.dll') > 0):
                os.system('D:/DigiSign/sign-with-pwd.bat ' + filepath)
            shutil.copy(filepath, newfilepath)
        elif not os.path.exists(filepath):
            os.mkdir(filepath)

    ret , packfilepath = updateETClientNsisScript(version)
    if not ret :
        return False, '更新离线包脚本失败'

    os.system('D:/DigiSign/sign-with-pwd.bat ' + packfilepath)
    newfilepath = os.path.join(basedir, os.path.basename(packfilepath));
    shutil.move(packfilepath, newfilepath)
    index = newfilepath.rfind('.')
    zipfilepath = newfilepath[:index] + '.zip'
    try :
        myzip = ZFile(zipfilepath, 'w')
        myzip.addfile(newfilepath)
        myzip.close()
    except Exception as error:
        return False, str(error)

    ret, appversioninfo = getAppVersionInfo()
    if not ret :
        return False, appversioninfo

    if not updateversionModulesinfo(newfiles, appversioninfo) :
        return False, '更新版本信息模块失败'
    updateversioninfo(version, appversioninfo)
    updateunupdatefileinfo(newfilenames, appversioninfo)
    ret, error = makeupdateinfojsonfile(basedir, newfilepath, appversioninfo)
    if not ret :
        return False, u'更新版本信息文件失败'

    gitdir = getAppGitDir()
    newgitdir = os.path.join(gitdir, version)
    bupdate = False
    if os.path.exists(newgitdir) :
        bupdate = True

    ret, error = checkpublishfiles(basedir, bupdate, newfilenames)
    if not ret :
        return False, error

    checkunusedir(basedir)

    if os.path.exists(newgitdir) :
        updategitfiles(newgitdir, basedir, newfilenames)
    else :
        shutil.move(basedir, gitdir)
    makeuploadgitscriptfile(version)

    if os.path.exists(basedir) :
        os.rmdir(basedir)
    
    return True, '操作成功'

def getupdateinfo() :
    global gupdateinfo
    try :
        filename = gAppName + 'updateinfo.txt'
        fp = codecs.open(os.path.join('D:/wamp/www', filename), 'rb')
        filecontent = fp.read()
        fp.close()
        gupdateinfo = filecontent
    except Exception as error:
        gupdateinfo = ''

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print('not enough args')
        quit()
    if len(sys.argv) == 5:
        if sys.argv[2] == 'packfile' :
            try :
                global gIsBeta
                gIsBeta = False
                if sys.argv[3] == '1' :
                    gIsBeta = True
                global gAppName
                gAppName = sys.argv[4]
                getupdateinfo()
                clearappgitdir()
                ret, info = makepackfile(sys.argv[1])
                os.remove(sys.argv[1])
                print (info)
            except Exception as error:
                os.remove(sys.argv[1])
                print (str(error))


