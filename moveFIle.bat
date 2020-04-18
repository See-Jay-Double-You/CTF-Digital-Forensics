@echo off
set DFMachine="F:\Windows7\Windows 7 x64.vmx"
echo %1

vmrun.lnk -T ws -gu admin -gp pass copyFileFromHostToGuest %DFMachine% "F:\Commands\Images\%1" "C:\Users\admin\Documents\%1"
