#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status."""
import requests


import requests

if __name__ == "__main__":
    response = requests.get("https://intranet.hbtn.io/status")
    print(response.text)
