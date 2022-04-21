#!/bin/bash
# displays all HTTP methods the server will accept.
curl -X OPTIONS -s "$1" -i | sed -n 2P | cut -d " " -f2- 
