#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the body"""

import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    # Get the URL argument from the command line
    url = sys.argv[1]

    # Try to open the URL and get the response object
    try:
        with urllib.request.urlopen(url) as response:
            # Get the body of the response
            body = response.read()
            # Decode the body in utf-8
            body = body.decode("utf-8")
            # Display the body
            print(body)
    # Catch the HTTPError exceptions and print the error code
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
