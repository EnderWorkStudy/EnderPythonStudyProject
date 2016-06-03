# -*- coding: cp1251 -*-
import shutil, _winreg
key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'SOFTWARE', 0, winreg.KEY_ALL_ACCESS)
key2 = winreg.OpenKey(key, 'NORDCURRENT', 0, winreg.KEY_ALL_ACCESS)

try:
    winreg.DeleteKey(key2, 'Sky Crew')
except Exception:
    print("Sky Crew already deleted!")
try:
    winreg.DeleteKey(key2, 'Sky Crew: Collector\'s Edition')
except Exception:
    print("Sky Crew: Collector's Edition already deleted!")

try:
    shutil.rmtree("C:\\Users\\user\\AppData\\LocalLow\\Nordcurrent")
except Exception:
    print("Local nordcurrent already dead!")

try:
    shutil.rmtree("C:\\Users\\user\\AppData\\Roaming\\Nordcurrent")
except Exception:
    print("Roaming nordcurrent already dead!")

print("Done!")

# -*- coding: cp1251 -*-
import shutil
import  _winreg

key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, 'SOFTWARE', 0, _winreg.KEY_ALL_ACCESS)
key2 = _winreg.OpenKey(key, 'DefaultCompany', 0, _winreg.KEY_ALL_ACCESS)

try:
    _winreg.DeleteKey(key2, 'Happy Clinic')
except Exception:
    print("Sky Crew already deleted!")
try:
    _winreg.DeleteKey(key2, 'Happy Clinic: Collector\'s Edition')
except Exception:
    print("Sky Crew: Collector's Edition already deleted!")

try:
    shutil.rmtree("C:\\Users\\user\\AppData\\LocalLow\\Nordcurrent")
except Exception:
    print("Local nordcurrent already dead!")

try:
    shutil.rmtree("C:\\Users\\user\\AppData\\Roaming\\Nordcurrent")
except Exception:
    print("Roaming nordcurrent already dead!")

print("Done!")

