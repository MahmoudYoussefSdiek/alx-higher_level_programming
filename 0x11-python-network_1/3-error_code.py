#!/usr/bin/python3
"""
This script sends a request to a URL and displays the body of the response.
"""

import urllib.request
import urllib.error
import sys

if __name__ == '__main__':
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            print(content)
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
