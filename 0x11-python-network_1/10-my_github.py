#!/usr/bin/python3
"""Takes your GitHub credentials and uses the GitHub API to display your id."""

import sys
import requests

if __name__ == "__main__":
    # If no arguments are given, set them to empty strings
    username = sys.argv[1] if len(sys.argv) > 1 else ""
    password = sys.argv[2] if len(sys.argv) > 2 else ""

    # Send a GET request to the GitHub API endpoint with Basic Authentication
    response = requests.get(
            "https://api.github.com/user",
            auth=(username, password))

    # Get the body of the response as a JSON object
    json_obj = response.json()

    if isinstance(json_obj, dict) and "id" in json_obj:
        print(json_obj["id"])
    # Otherwise, display None
    else:
        print(None)
