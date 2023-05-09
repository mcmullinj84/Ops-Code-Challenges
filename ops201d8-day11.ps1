# Script Name:                  ops201d9-day11
# Author:                       Jonathan McMullin
# Date of latest revision:      05/04/2023
# Purpose:                      Powershell Management

# most scripts derived from https://github.com/superswan/Powershell-SysAdmin 
# Declaration of variables

# Declaration of functions

# Main

#1
# Enable File and Printer Sharing
Set-NetFirewallRule -DisplayGroup "File And Printer Sharing" -Enabled True

#2
# Enable ICMP
netsh advfirewall firewall add rule name="Allow incoming ping requests IPv4" dir=in action=allow protocol=icmpv4

#3
Firewall Rule
Enable-NetFirewallRule -DisplayGroup “Remote Desktop”

#4
#RDP
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
Enable-PSRemoting -SkipNetworkProfileCheck -Force
#5

#Bloatware Remover
iex ((New-Object System.Net.WebClient).DownloadString('https://git.io/debloat'))


#Enable Hyper-V
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All

#Toggle SMBv1
Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force

# End