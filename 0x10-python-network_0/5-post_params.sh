#!/bin/bash
# A Bash script that takes in a URL and displays the body of the response
curl -s -d "email=test@gmail%2Ecom&subject=I%2Bwill%2Balways%2Bbe%2Bhere%2Bfor%2BPLD" -X POST $1
