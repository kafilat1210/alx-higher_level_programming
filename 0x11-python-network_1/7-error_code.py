#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the body """

import sys
import requests

if __name__ == "__main__":
    # Get the URL argument from the command line
    url = sys.argv[1]

    # Send a GET request to the URL and get a Response object
    response = requests.get(url)

    # Get the HTTP status code as an integer
    status_code = response.status_code

    # If the status code is less than 400, display the body of the response
    if status_code < 400:
        print(response.text)
    # Otherwise, print the error code
    else:
        print("Error code: {}".format(status_code))
