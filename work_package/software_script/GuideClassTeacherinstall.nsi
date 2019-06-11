; �ýű���jiamule���,NSIS��

!include "WinVer.nsh" 
	
; ��װ�����ʼ���峣��
!define PRODUCT_NAME "������ʦ��ϵͳ - ѧ��ʦ"
!define PRODUCT_VERSION "1.0.2.1810"
!define PRODUCT_PUBLISHER "�򵥿Ƽ�"
!define PRODUCT_WEB_SITE "http://www.jd100.com/"
!define PRODUCT_DIR_REGKEY "Software\Microsoft\Windows\CurrentVersion\App Paths\GuideClassTeacherInstaller.exe"
!define INSTALLSIZE 85893
SetCompressor /SOLID lzma

; ------ MUI �ִ����涨�� (1.67 �汾���ϼ���) ------
!include "MUI.nsh"

; MUI Ԥ���峣��
!define MUI_ABORTWARNING
!define MUI_ICON "etsetup.ico"

; ��ӭҳ��
!insertmacro MUI_PAGE_WELCOME
; ���Э��ҳ��
;!insertmacro MUI_PAGE_LICENSE "..\..\..\..\..\path\to\licence\YourSoftwareLicence.txt"
; ��װ����ҳ��
!insertmacro MUI_PAGE_INSTFILES
; ��װ���ҳ��
!define MUI_FINISHPAGE_RUN "$LOCALAPPDATA\Easytech\GuideClassTeacher\GuideClassTeacher.exe"

!insertmacro MUI_PAGE_FINISH

; ��װ�����������������
!insertmacro MUI_LANGUAGE "SimpChinese"
; ------ Exe �ļ���Ӱ汾��Ϣ������ŵ� MUI_LANGUAGE���棬�������������룩 ------
;���漸������ʾ��װ�����Ե�һЩ��Ϣ
VIProductVersion "1.0.2.1810"
;��Ʒ����
VIAddVersionKey /LANG=${LANG_SimpChinese} "ProductName" "������ʦ��ϵͳ"
;��˾
VIAddVersionKey /LANG=${LANG_SimpChinese} "CompanyName" "�����򵥿Ƽ����޹�˾"
;��Ȩ
VIAddVersionKey /LANG=${LANG_SimpChinese} "LegalCopyright" ""
;����
VIAddVersionKey /LANG=${LANG_SimpChinese} "FileDescription" "������ʦ��ϵͳ - ѧ��ʦ"
;�ļ��汾��
VIAddVersionKey /LANG=${LANG_SimpChinese} "FileVersion" "1.0.2.1810"
; ��װԤ�ͷ��ļ�
!insertmacro MUI_RESERVEFILE_INSTALLOPTIONS
; ------ MUI �ִ����涨����� ------


;��ʾ����=������+�汾��
Name "${PRODUCT_NAME} ${PRODUCT_VERSION}"
;����ļ���
OutFile "GuideClassTeacherSetup1.0.2.1810.exe"
;��װĿ¼
InstallDir "$LOCALAPPDATA\Easytech\GuideClassTeacher"
;��װĿ¼д��ע���
;InstallDirRegKey HKLM "${PRODUCT_UNINST_KEY}" "UninstallString"
;��ʾ��װ��ϸ����
ShowInstDetails show
;���½Ǳ�ʶ
BrandingText "������ʦ�ΰ�װ����"

RequestExecutionLevel user
Section "������ʦ��" SEC01
;
  SetOutPath "$LOCALAPPDATA\Easytech\GuideClassTeacher"
  SetOverwrite on
  ;ж��֮ǰ�汾����
   ;ExecShell open "$INSTDIR\ETClientInstaller.exe" "-u"
    ;MessageBox MB_OK "��װǰ������ж��֮ǰ��װ�İ汾�����֮ǰ�а�װ�����Զ�������ж�س�����ж�ص��ٰ�[ȷ��]�������ΰ�װ"
  ;MessageBox MB_OK "��ȷ���ر�������������ٰ�[ȷ��]�������ΰ�װ"

 ;��������
  KillProcDLL::KillProc "GuideClassTeacher.exe"
  ;KillProcDLL::KillProc "EasyClient.exe"
  
  ;ɾ��֮ǰ������ܸ��Ƶ��ļ�
  ;Delete "$INSTDIR\EasyUI.swf"
  ;UnRegDLL "$INSTDIR\ETClientHelper.dll"
  ;��װ�����ļ�

  File /r "GuideClassTeacherPack\*"
	
  ;ע��dll���
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
  
  
  ;WriteRegStr HKLM "SOFTWARE\MozillaPlugins\@jd100.com/ETCClientHelper" "Description" "��ѧϰ��"
  ;WriteRegStr HKLM "SOFTWARE\MozillaPlugins\@jd100.com/ETCClientHelper" "Path" "$INSTDIR\npETClientHelper.dll"
  ;WriteRegStr HKLM "SOFTWARE\MozillaPlugins\@jd100.com/ETCClientHelper" "ProductName" "�򵥿���"
  ;WriteRegStr HKLM "SOFTWARE\MozillaPlugins\@jd100.com/ETCClientHelper" "Vendor" "��ѧϰ��"
  ;WriteRegStr HKLM "SOFTWARE\MozillaPlugins\@jd100.com/ETCClientHelper" "Version" "${PRODUCT_WEBKIT_VERSION}"
  ;WriteRegStr HKLM "SOFTWARE\MozillaPlugins\@jd100.com/ETCClientHelper\MimeTypes\application/x-easytech-clienthelper" "Description" "��ѧϰ��"
  ;WriteRegStr HKLM "SOFTWARE\MozillaPlugins\@jd100.com/ETCClientHelper\MimeTypes\application/x-easytech-clienthelper" "Suffixes" "*"
	
  ;WriteRegStr HKCR "etx" "" "URL:etx Protocol"
  ;WriteRegStr HKCR "etx" "URL Protocol" ""
  ;WriteRegStr HKCR "etx\\DefaultIcon" "" "$INSTDIR\EasyClient.exe, 0"
  ;WriteRegStr HKCR "etx\\shell\\open\\command" "" "$INSTDIR\EasyClient.exe %1"
  
  
  ;������ʼ�˵���ݷ�ʽ
  CreateDirectory "$SMPROGRAMS\��ѧϰ��\������ʦ��(ѧ��ʦ)"
  CreateShortCut "$SMPROGRAMS\��ѧϰ��\������ʦ��(ѧ��ʦ)\������ʦ��(ѧ��ʦ).lnk" "$INSTDIR\GuideClassTeacher.exe"
  CreateShortCut "$SMPROGRAMS\��ѧϰ��\������ʦ��(ѧ��ʦ)\ж�ض�����ʦ��(ѧ��ʦ).lnk" "$INSTDIR\GuideClassTeacherInstaller.exe" uninstall
  
  ;���������ݷ�ʽ
  CreateShortCut "$DESKTOP\������ʦ��(ѧ��ʦ).lnk" "$INSTDIR\GuideClassTeacher.exe"
  ;CreateShortCut "$DESKTOP\��ѧϰ��.lnk" "http://www.jiandan100.cn/user/clientstudy/" " " "$INSTDIR\EasyClient.exe" "2"



  
SectionEnd
