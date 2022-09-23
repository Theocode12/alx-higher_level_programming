#!/bin/bash
# A Bash script that takes in a URL and displays the body of the response
curl -d "email=test@gmail%2Ecom&subject=I+will+always+be+here+for+PLD" -X POST $1
