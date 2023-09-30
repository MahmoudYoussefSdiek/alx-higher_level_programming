#!/usr/bin/python3
"""
This script sends a POST request to http://0.0.0.0:5000/search_user with
a letter as a parameter, and displays the response.
"""

import requests
import sys

url = 'http://0.0.0.0:5000/search_user'

if __name__ == '__main__':
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    data = {'q': q}
    response = requests.post(url, data=data)

    try:
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
