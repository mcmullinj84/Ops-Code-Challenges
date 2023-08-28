
local nmap = require "nmap"

-- Define the script's arguments and description
description = [[
Custom NSE script to check the status of predefined ports (FTP, SSH, Telnet, SMTP, POP3, and HTTP/HTTPS).
]]
license = "Same as Nmap--See https://nmap.org/book/man-legal.html"

-- Define the port rule for this script
portrule = function(host, port)
  local predefined_ports = {21, 22, 23, 25, 110, 443}
  return nmap.match(port.number, predefined_ports)
end

-- The action function to run when the script is called
action = function(host, port)
  local result = {}
  
  -- Display the port status and service name
  if port.state == "open" then
    local service = nmap.service_protocols[port.number] or "unknown"
    local version = port.version or "unknown"
    local output = string.format("Port %d (%s) is open.", port.number, service)
    
    if version then
      output = output .. " Version: " .. version
    end
    
    table.insert(result, output)
  elseif port.state == "closed" then
    table.insert(result, string.format("Port %d is closed", port.number))
  elseif port.state == "filtered" then
    table.insert(result, string.format("Port %d is filtered", port.number))
  else
    table.insert(result, string.format("Port %d has an unknown state", port.number))
  end

  return result
end