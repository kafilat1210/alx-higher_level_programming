#!/usr/bin/python3
"""Takes in a letter and sends a POST request to http://0.0.0.0:500"""

import sys
import requests

if __name__ == "__main__":
    # Get the letter argument from the command line
    # If no argument is given, set the letter to an empty string
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    # Send a POST request to the URL with the letter as a parameter
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data={"q": letter})

    # Try to get the body of the response as a JSON object
    try:
        json_obj = response.json()
        if isinstance(json_obj, dict) and json_obj:
            print("[{}] {}".format(json_obj.get("id"), json_obj.get("name")))
        # Otherwise, display No result
        else:
            print("No result")
    # If the JSON object is invalid, display Not a valid JSON
    except ValueError:
        print("Not a valid JSON")
