#!/bin/bash
# This script sends a GET request to a URL passed as an argument
# and displays the body of the response. A header variable is also sent with the request.

URL=$1
HEADER="X-School-User-Id: 98"

curl -sH "$HEADER" "$URL"
