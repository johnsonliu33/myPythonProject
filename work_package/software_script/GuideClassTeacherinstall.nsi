; 该脚本由jiamule添加,NSIS用

!include "WinVer.nsh" 
	
; 安装程序初始定义常量
!define PRODUCT_NAME "定制名师课系统 - 学管师"
!define PRODUCT_VERSION "1.0.2.1810"
!define PRODUCT_PUBLISHER "简单科技"
!define PRODUCT_WEB_SITE "http://www.jd100.com/"
!define PRODUCT_DIR_REGKEY "Software\Microsoft\Windows\CurrentVersion\App Paths\GuideClassTeacherInstaller.exe"
!define INSTALLSIZE 85893
SetCompressor /SOLID lzma

; ------ MUI 现代界面定义 (1.67 版本以上兼容) ------
!include "MUI.nsh"

; MUI 预定义常量
!define MUI_ABORTWARNING
!define MUI_ICON "etsetup.ico"

; 欢迎页面
!insertmacro MUI_PAGE_WELCOME
; 许可协议页面
;!insertmacro MUI_PAGE_LICENSE "..\..\..\..\..\path\to\licence\YourSoftwareLicence.txt"
; 安装过程页面
!insertmacro MUI_PAGE_INSTFILES
; 安装完成页面
!define MUI_FINISHPAGE_RUN "$LOCALAPPDATA\Easytech\GuideClassTeacher\GuideClassTeacher.exe"

!insertmacro MUI_PAGE_FINISH

; 安装界面包含的语言设置
!insertmacro MUI_LANGUAGE "SimpChinese"
; ------ Exe 文件添加版本信息（这个放到 MUI_LANGUAGE后面，否则中文是乱码） ------
;下面几行是显示安装包属性的一些信息
VIProductVersion "1.0.2.1810"
;产品名称
VIAddVersionKey /LANG=${LANG_SimpChinese} "ProductName" "定制名师课系统"
;公司
VIAddVersionKey /LANG=${LANG_SimpChinese} "CompanyName" "北京简单科技有限公司"
;版权
VIAddVersionKey /LANG=${LANG_SimpChinese} "LegalCopyright" ""
;描述
VIAddVersionKey /LANG=${LANG_SimpChinese} "FileDescription" "定制名师课系统 - 学管师"
;文件版本号
VIAddVersionKey /LANG=${LANG_SimpChinese} "FileVersion" "1.0.2.1810"
; 安装预释放文件
!insertmacro MUI_RESERVEFILE_INSTALLOPTIONS
; ------ MUI 现代界面定义结束 ------


;显示名称=程序名+版本号
Name "${PRODUCT_NAME} ${PRODUCT_VERSION}"
;输出文件名
OutFile "GuideClassTeacherSetup1.0.2.1810.exe"
;安装目录
InstallDir "$LOCALAPPDATA\Easytech\GuideClassTeacher"
;安装目录写入注册表
;InstallDirRegKey HKLM "${PRODUCT_UNINST_KEY}" "UninstallString"
;显示安装详细进度
ShowInstDetails show
;左下角标识
BrandingText "定制名师课安装程序"

RequestExecutionLevel user
Section "定制名师课" SEC01
;
  SetOutPath "$LOCALAPPDATA\Easytech\GuideClassTeacher"
  SetOverwrite on
  ;卸载之前版本部分
   ;ExecShell open "$INSTDIR\ETClientInstaller.exe" "-u"
    ;MessageBox MB_OK "安装前建议先卸载之前安装的版本，如果之前有安装，会自动弹出来卸载程序，先卸载掉再按[确定]继续本次安装"
  ;MessageBox MB_OK "请确保关闭所有浏览器，再按[确定]继续本次安装"

 ;结束进程
  KillProcDLL::KillProc "GuideClassTeacher.exe"
  ;KillProcDLL::KillProc "EasyClient.exe"
  
  ;删除之前最常见不能复制的文件
  ;Delete "$INSTDIR\EasyUI.swf"
  ;UnRegDLL "$INSTDIR\ETClientHelper.dll"
  ;安装复制文件

  File /r "GuideClassTeacherPack\*"
	
  ;注册dll组件
  ;RegDLL "$INSTDIR\ETClientHelper.dll"
  ;RegDLL "$INSTDIR\PlayCore.dll"
  
  
  WriteRegStr HKLM "SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\GuideClassTeacher" "DisplayIcon" "$INSTDIR\GuideClassTeacher.exe"
  WriteRegStr HKLM "SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\GuideClassTeacher" "DisplayName" "${PRODUCT_NAME}"
  WriteRegStr HKLM "SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\GuideClassTeacher" "DisplayVersion" "${PRODUCT_VERSION}"
  WriteRegStr HKLM "SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\GuideClassTeacher" "Publisher" "${PRODUCT_PUBLISHER}"
  WriteRegStr HKLM "SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\GuideClassTeacher" "UninstallString" "$INSTDIR\GuideClassTeacherInstaller.exe uninstall"
  WriteRegDWORD HKLM "SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\GuideClassTeacher" "EstimatedSize" ${INSTALLSIZE}

  ;WriteRegStr HKLM "SOFTWARE\Easytech\EasyClient" "Install" "success"
  ;WriteRegStr HKLM "SOFTWARE\Easytech\EasyClient" "Install_Dir" "$INSTDIR"
  ;WriteRegStr HKLM "SOFTWARE\Easytech\EasyClient" "Regist_Dll" "ETClientHelper.dll|"
  ;WriteRegStr HKLM "SOFTWARE\Easytech\EasyClient" "Version" "${PRODUCT_VERSION}"
  ;WriteRegStr HKLM "SOFTWARE\Easytech\EasyClient" "FFmpegVersion" "${PRODUCT_FFMPEGPLAYCORE_VERSION}"
  
  
  ;WriteRegStr HKLM "SOFTWARE\MozillaPlugins\@jd100.com/ETCClientHelper" "Description" "简单学习网"
  ;WriteRegStr HKLM "SOFTWARE\MozillaPlugins\@jd100.com/ETCClientHelper" "Path" "$INSTDIR\npETClientHelper.dll"
  ;WriteRegStr HKLM "SOFTWARE\MozillaPlugins\@jd100.com/ETCClientHelper" "ProductName" "简单课堂"
  ;WriteRegStr HKLM "SOFTWARE\MozillaPlugins\@jd100.com/ETCClientHelper" "Vendor" "简单学习网"
  ;WriteRegStr HKLM "SOFTWARE\MozillaPlugins\@jd100.com/ETCClientHelper" "Version" "${PRODUCT_WEBKIT_VERSION}"
  ;WriteRegStr HKLM "SOFTWARE\MozillaPlugins\@jd100.com/ETCClientHelper\MimeTypes\application/x-easytech-clienthelper" "Description" "简单学习网"
  ;WriteRegStr HKLM "SOFTWARE\MozillaPlugins\@jd100.com/ETCClientHelper\MimeTypes\application/x-easytech-clienthelper" "Suffixes" "*"
	
  ;WriteRegStr HKCR "etx" "" "URL:etx Protocol"
  ;WriteRegStr HKCR "etx" "URL Protocol" ""
  ;WriteRegStr HKCR "etx\\DefaultIcon" "" "$INSTDIR\EasyClient.exe, 0"
  ;WriteRegStr HKCR "etx\\shell\\open\\command" "" "$INSTDIR\EasyClient.exe %1"
  
  
  ;创建开始菜单快捷方式
  CreateDirectory "$SMPROGRAMS\简单学习网\定制名师课(学管师)"
  CreateShortCut "$SMPROGRAMS\简单学习网\定制名师课(学管师)\定制名师课(学管师).lnk" "$INSTDIR\GuideClassTeacher.exe"
  CreateShortCut "$SMPROGRAMS\简单学习网\定制名师课(学管师)\卸载定制名师课(学管师).lnk" "$INSTDIR\GuideClassTeacherInstaller.exe" uninstall
  
  ;创建桌面快捷方式
  CreateShortCut "$DESKTOP\定制名师课(学管师).lnk" "$INSTDIR\GuideClassTeacher.exe"
  ;CreateShortCut "$DESKTOP\简单学习网.lnk" "http://www.jiandan100.cn/user/clientstudy/" " " "$INSTDIR\EasyClient.exe" "2"



  
SectionEnd
