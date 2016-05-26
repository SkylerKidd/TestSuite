dim fso: set fso = CreateObject("Scripting.FileSystemObject")
    dim CurrentDirectory
    CurrentDirectory = fso.GetAbsolutePathName(".")
    
Set oShell = WScript.CreateObject("WScript.shell")
oShell.run "%comspec% /k java -jar " & CurrentDirectory & "\collegeAffordability.jar -R", 1, True