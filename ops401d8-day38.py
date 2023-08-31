#!/usr/bin/env python3

# Script Name:                  ops401d8-day38
# Author:                       Jonathan McMullin
# Date of latest revision:      08/30/2023
# Purpose:                      XSS Vulnerability Detection

# Credit: Utilized syntax from Code Fellows Demo and ChatGPT to develop this script

# Import libraries

import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# Declare functions

# This function retrieves all HTML forms from a given URL.
def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

# This function extracts details (action, method, inputs) from an HTML form.
def get_form_details(form):
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

# This function submits a form with a specified value and checks for XSS vulnerability.
def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

# This function scans a URL for XSS vulnerabilities.
def scan_xss(url):
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    # Example of a JavaScript payload that triggers an alert.
    js_script = "<script>alert('XSS')</script>"
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = True
    return is_vulnerable

# Main

# The main function takes a URL as input and scans it for XSS vulnerabilities.
if __name__ == "__main__":
    url = input("Enter a URL to test for XSS:") 
    print(scan_xss(url))

# End

# Outputs on Dojo - 1st = success, 2nd = failure
'''
dojo@dojo-VirtualBox:~/Desktop/class-38$ ./challenge.py
Enter a URL to test for XSS:https://xss-game.appspot.com/level1/frame
[+] Detected 1 forms on https://xss-game.appspot.com/level1/frame.
[+] XSS Detected on https://xss-game.appspot.com/level1/frame
[*] Form details:
{'action': '',
 'inputs': [{'name': 'query',
             'type': 'text',
             'value': "<script>alert('XSS')</script>"},
            {'name': None, 'type': 'submit'}],
 'method': 'get'}
True

dojo@dojo-VirtualBox:~/Desktop/class-38$ ./challenge.py
Enter a URL to test for XSS:http://dvwa.local/login.php
[+] Detected 1 forms on http://dvwa.local/login.php.
False

'''