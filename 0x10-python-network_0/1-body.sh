#!/bin/bash
#displays the body of the response if the status is 200
# display if success
curl -X GET -s -L "$1"
