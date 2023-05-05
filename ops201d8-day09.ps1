# Script Name:                  ops201d9-day09
# Author:                       Jonathan McMullin
# Date of latest revision:      05/04/2023
# Purpose:                      Powershell Management

# Declaration of variables

# Declaration of functions

# Main

#1
$Begin = (Get-Date).AddDays(-1)
$End = Get-Date
$DesktopPath = "C:\Users\VM-JMC\Desktop"
Get-EventLog -LogName System -After $Begin -Before $End > $DesktopPath\last_24.txt

#2

$DesktopPath = "C:\Users\VM-JMC\Desktop"
Get-EventLog -LogName System -EntryType Error > $DesktopPath\errors.txt

#3

Get-EventLog -LogName System -InstanceId 16

#4

Get-EventLog -LogName System -Newest 20

#5

Get-EventLog -LogName System -Newest 500 | Format-Table -Wrap




# End