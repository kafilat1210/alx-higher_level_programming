#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the value"""

import sys
import requests

if __name__ == "__main__":
    # Get the URL argument from the command line
    url = sys.argv[1]

    # Send a GET request to the URL and get a Response object
    response = requests.get(url)

    # Get a dictionary of the response headers
    headers = response.headers

    # Get the value of the X-Request-Id variable and display it
    print(headers.get("X-Request-Id"))
