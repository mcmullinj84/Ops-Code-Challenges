# Script Name:                  ops201d8-day12
# Author:                       Jonathan McMullin
# Date of latest revision:      05/09/2023
# Purpose:                      Powershell Select string

# Declaration of variables

# Declaration of functions
function Search-IPv4Address {
    # output ipconfig to network_report.txt file
    ipconfig > C:\Users\VM-JMC\Desktop\network_report.txt

    # Search .txt file for IPv4 address and output that line into Powershell
    $ipv4Addresses = Select-String -Path C:\Users\VM-JMC\Desktop\network_report.txt -Pattern "IPv4 Address" | Select-Object -ExpandProperty Line

    # Remove network_report.txt file
    Remove-Item C:\Users\VM-JMC\Desktop\network_report.txt

    # Return the IPv4 addresses as output from the function
    return $ipv4Addresses

# Main
# Define a function to create and search the network report

# Call the function and store the result in a variable
$ipv4Addresses = Search-IPv4Address

# Print the IPv4 addresses to the console
Write-Host "IPv4 Addresses: $ipv4Addresses"


# End