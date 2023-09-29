#!/usr/bin/python3
"""
This script sends a POST request to a URL with an email as
a parameter, and displays the body of the response.
"""

import urllib.parse
import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    request = urllib.request.Request(url, data)

    with urllib.request.urlopen(request) as response:
        content = response.read().decode('utf-8')

    print(content)
