#!/bin/bash
# A Bash script that sends a JSON POST and displays the body of the response
curl -X POST $1 -H 'Content-type: application/json' -d @$2
