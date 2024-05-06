#!/usr/bin/python3
"""Takes in a URL and an email address, sends a POST request to the URL"""

import sys
import requests

if __name__ == "__main__":
    # Get the URL and email arguments from the command line
    url = sys.argv[1]
    email = sys.argv[2]

    # Send a POST request to the URL with the email as a parameter
    response = requests.post(url, data={"email": email})

    # Get the body of the response as a string
    body = response.text

    # Display the body
    print(body)
