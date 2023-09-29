#!/bin/bash
# This script makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing "You got me!"
curl -sX PUT -Ld "user_id=98" -H "Origin: HolbertonSchool" -H "User-Agent: HolbertonSchool" 0.0.0.0:5000/catch_me
