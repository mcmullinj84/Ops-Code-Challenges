#!/usr/bin/env python3

# Script Name:                  ops301d8-day11
# Author:                       Jonathan McMullin
# Date of latest revision:      06/14/2023
# Purpose:                      Practice python psutil

# Note: to install psutil package run the following commands in the terminal:
# <sudo apt-get update -y>
# <sudo apt-get install -y python3-psutil>
# Source: https://zoomadmin.com/HowToInstall/UbuntuPackage/python3-psutil 

# Declaration of variables

# Declaration of functions

# Main 

import psutil

# credit to ChatGPT for explaining the syntax of psutil

# Get CPU times
cpu_times = psutil.cpu_times()

# Time spent by normal processes executing in user mode
user_time = cpu_times.user

# Time spent by processes executing in kernel mode
system_time = cpu_times.system

# Time when system was idle
idle_time = cpu_times.idle

# Time spent by priority processes executing in user mode
priority_user_time = cpu_times.nice

# Time spent waiting for I/O to complete
io_wait_time = cpu_times.iowait

# Time spent for servicing hardware interrupts
hardware_interrupt_time = cpu_times.irq

# Time spent for servicing software interrupts
software_interrupt_time = cpu_times.softirq

# Time spent by other operating systems running in a virtualized environment
virtual_os_time = cpu_times.steal

# Time spent running a virtual CPU for guest operating systems
guest_time = cpu_times.guest

# Print the fetched information
print("Time spent by normal processes executing in user mode:", user_time)
print("Time spent by processes executing in kernel mode:", system_time)
print("Time when system was idle:", idle_time)
print("Time spent by priority processes executing in user mode:", priority_user_time)
print("Time spent waiting for I/O to complete:", io_wait_time)
print("Time spent for servicing hardware interrupts:", hardware_interrupt_time)
print("Time spent for servicing software interrupts:", software_interrupt_time)
print("Time spent by other operating systems running in a virtualized environment:", virtual_os_time)
print("Time spent running a virtual CPU for guest operating systems:", guest_time)

# End