#!/usr/bin/python3


import requests


def main():
    """Fetches the status of https://alx-intranet.hbtn.io/status and displays it."""

    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)

    if response.status_code == 200:
        print("Body response:")
        for key, value in response.json().items():
            print(f"\t- type: <class '{type(value)}'>")
            print(f"\t- content: {value}")
    else:
        print(f"Error: {response.status_code}")


if __name__ == "__main__":
    main()
