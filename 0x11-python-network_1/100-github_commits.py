#!/usr/bin/python3
"""Takes in a repository name and an owner name, and uses the GitHub API."""

import sys
import requests

if __name__ == "__main__":
    # Get the repository name and owner name arguments from the command line
    # If no arguments are given, set them to empty strings
    repo = sys.argv[1] if len(sys.argv) > 1 else ""
    owner = sys.argv[2] if len(sys.argv) > 2 else ""

    # Send a GET request to the GitHub API endpoint with the query parameters
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    response = requests.get(url, params={"per_page": 10})

    # Get the body of the response as a JSON object
    json_obj = response.json()

    # If the JSON object is a list, iterate over it and display the sha and
    # author name of each commit
    if isinstance(json_obj, list):
        for commit in json_obj:
            sha = commit.get("sha")
            author = commit.get("commit").get("author").get("name")
            print("{}: {}".format(sha, author))
