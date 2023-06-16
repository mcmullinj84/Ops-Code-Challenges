# Script Name:                  ops301d8-day13
# Author:                       Jonathan McMullin
# Date of latest revision:      06/15/2023
# Purpose:                      Powershell Active Directory

# Resources - Microsoft Documentation and ChatGPT used to help with syntax

# Import the Active Directory module
# Suggestion from Chat-GPT
Import-Module ActiveDirectory

# Set the user details - this makes the code modular
$firstName = "Franz"
$lastName = "Ferdinand"
$jobTitle = "TPS Reporting Lead"
$company = "GlobeX USA"
$office = "Springfield, OR"
$department = "TPS"
$email = "ferdi@GlobeXpower.com"

# Set the distinguished name (DN) for the user
$userDN = "CN=$firstName $lastName,OU=Users,DC=corp,DC=globex,DC=com"

# Create the new user 
New-ADUser -SamAccountName $firstName[0].ToString().ToLower() + $lastName.ToLower() -UserPrincipalName ($firstName[0].ToString().ToLower() + $lastName.ToLower() + "@corp.globex.com") -Name "$firstName $lastName" -GivenName $firstName -Surname $lastName -Enabled $true -EmailAddress $email -Title $jobTitle -Company $company -Office $office -Department $department -PassThru | Set-ADUser -ChangePasswordAtLogon $true

# Display the user details
Get-ADUser -Identity $userDN -Properties *

# Output a success message
Write-Host "User $firstName $lastName has been created in Active Directory."