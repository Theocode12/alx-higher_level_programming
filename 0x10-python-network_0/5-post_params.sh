#!/bin/bash
# A Bash script that takes in a URL and displays the body of the response
curl -ds "email=test@gmail%2Ecom&subject=I2Bwill2Balways2Bbe2Bhere2Bfor2BPLD" -X POST $1
