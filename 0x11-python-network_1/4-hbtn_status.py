#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""

import requests

if __name__ == "__main__":
    # Send a GET request to the URL and get a Response object
    response = requests.get("https://alx-intranet.hbtn.io/status")
    # Get the body of the response as a string
    body = response.text
    # Display the type and content of the response body
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
