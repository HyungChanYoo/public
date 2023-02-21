"""
윈도우 부팅 시, 파이썬 어플리케이션 자동 실행.
레즈스트리 편집하여 자동 실행하는 코드.
출처 : Python Assets, 2022-02-11, https://pythonassets.com/posts/run-python-application-at-startup-on-windows/

수정 중
"""

# 윈도우 레지스트리를 편집하기 위해서 윈도우 API가 필요하며, pywin32 패키를 설치하여 이용할 수 있다.
# pip install pywin32

from win32api import (GetModuleFileName, RegCloseKey, RegDeleteValue,
                    RegOpenKeyEx, RegSetValueEx, RegEnumValue)
from win32con import (HKEY_LOCAL_MACHINE, HKEY_CURRENT_USER, KEY_WRITE,
                    KEY_QUERY_VALUE, REG_SZ)
from winerror import ERROR_NO_MORE_ITEMS
import pywintypes


# 레지스티리 값을 편집할 키 path이다.
# win+r -> regedit 입력 (레지스트리 편집기)
# HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run or HKEY_LOCAL_MACHINE SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run
# 레지스트리 편집기에서 위의 경로를 찾아 들어가면 현재 등록된 프로그램들을 볼 수 있다.

STARTUP_KEY_PATH = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"


def run_at_startup_set(appname, path=None, user=False):
    """
    Store the entry in the registry for running the application
    at startup.
    """
    # Open the registry key where applications that run
    # at startup are stored.
    key = RegOpenKeyEx(
        HKEY_CURRENT_USER if user else HKEY_LOCAL_MACHINE,
        STARTUP_KEY_PATH,
        0,
        KEY_WRITE | KEY_QUERY_VALUE
    )
    # Make sure our application is not already in the registry.
    i = 0
    while True:
        try:
            name, _, _ = RegEnumValue(key, i)
        except pywintypes.error as e:
            if e.winerror == ERROR_NO_MORE_ITEMS:
                break
            else:
                raise
        if name == appname:
            RegCloseKey(key)
            return
        i += 1
    # Create a new entry or key.
    RegSetValueEx(key, appname, 0, REG_SZ, path or GetModuleFileName(0))
    # Close the key when no longer used.
    RegCloseKey(key)


def run_script_at_startup_set(appname, user=False):
    """
    Like run_at_startup_set(), but for applications released as
    source code files (.py).
    """
    run_at_startup_set(
        appname,
        # Set the interpreter path (returned by GetModuleFileName())
        # followed by the path of the current Python file (__file__).
        '{} "{}"'.format(GetModuleFileName(0), __file__),
        user
    )


def run_at_startup_remove(appname, user=False):
    """
    Remove the registry application passed in the first param.
    """
    key = RegOpenKeyEx(
        HKEY_CURRENT_USER if user else HKEY_LOCAL_MACHINE,
        STARTUP_KEY_PATH,
        0,
        KEY_WRITE
    )
    RegDeleteValue(key, appname)
    RegCloseKey(key)
