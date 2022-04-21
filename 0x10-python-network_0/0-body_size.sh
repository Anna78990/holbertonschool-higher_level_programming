#!/usr/bin/env bash
curl -sI $1 | grep Content-Length | awk -F ':' '{print $2}'
