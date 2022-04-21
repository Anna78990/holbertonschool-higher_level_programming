#!/bin/bash
#displays the body of the response if the status is 200
if [ "$(curl -sI "$1" | head -1 | awk '{print $2}')" -eq 200 ]; then  curl -L "$1";fi
