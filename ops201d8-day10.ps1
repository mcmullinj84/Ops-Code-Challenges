# Script Name:                  ops201d8-day10
# Author:                       Jonathan McMullin
# Date of latest revision:      05/05/2023
# Purpose:                      Powershell Sys Process Commands

# Declaration of variables

# Declaration of functions

# Main

#1
#Format-Table limits the output to Just the name and the CPU usage
Get-Process | Sort-Object -Descending CPU | Format-Table Name, CPU -AutoSize

#2

Get-Process | Sort-Object -Descending Id | Format-Table Name, Id -AutoSize
#3

Get-Process | Sort-Object -Descending WorkingSet | Select-Object -First 5 Name, WorkingSet | Format-Table -AutoSize

#4

Start-Process microsoft-edge https://owasp.org/www-project-top-ten/.

#5
#ChatGPT suggested I set up a loop using a 'counter'. This counts
#everytime the function completes the process and continues to run it
# until the counter hits 10
for ($i = 1; $i -le 10; $i++) {
    Start-Process notepad
}

#6
Get-Process notepad | Stop-Process

#7
#ChatGPT recommends running the "-ErrorAction Silently Continue" to stop error messages
$edgeProcesses = Get-Process msedge -ErrorAction SilentlyContinue

#This condiditonal script will take the PIDs and stop them
if ($edgeProcesses) {
    $edgePID = $edgeProcesses.Id
    Write-Host "Found Microsoft Edge process with ID $edgePID"
    
    Stop-Process -Id $edgePID -Force
    Write-Host "Microsoft Edge process with ID $edgePID stopped."
}
else {
    Write-Host "No Microsoft Edge processes found."
}


# End