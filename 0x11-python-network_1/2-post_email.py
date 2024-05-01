#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request to the URL with the email
as a parameter, and displays the body of the response."""

import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    # Get the URL and email arguments from the command line
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email parameter into a query string
    data = urllib.parse.urlencode({"email": email}).encode("ascii")

    # Create a Request object with the URL and the data
    req = urllib.request.Request(url, data)

    # Open the URL and get the response object
    with urllib.request.urlopen(req) as response:
        # Get the body of the response and decode it in utf-8
        body = response.read().decode("utf-8")

    # Display the body
    print(body)
