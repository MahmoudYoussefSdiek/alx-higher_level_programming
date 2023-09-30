#!/usr/bin/python3
"""
This script uses the GitHub API to list the 10 most recent commits of a
repository, and displays the commit sha and author name.
"""

import requests
import sys

if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    response = requests.get(url)

    json_data = response.json()

    for commit in json_data[:10]:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print("{}: {}".format(sha, author_name))
