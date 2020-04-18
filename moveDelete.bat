@echo off
set DFMachine="F:\Windows7\Windows 7 x64.vmx"
C:
cd C:\Program Files (x86)\VMware\VMware Workstation


vmrun -T ws -gu admin -gp pass copyFileFromHostToGuest %DFMachine% "F:\Commands\Images\%1" "C:\Users\admin\Documents\%1"

vmrun -T ws -gu admin -gp pass deleteFileinGuest %DFMachine% "C:\Users\admin\Documents\%1"
