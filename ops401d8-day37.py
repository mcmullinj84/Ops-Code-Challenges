#!/usr/bin/env python3

# Script Name:                  ops401d8-day37
# Author:                       Jonathan McMullin
# Date of latest revision:      08/29/2023
# Purpose:                      Cookie Capture Tool

# Credit: Utilized syntax from Code Fellows Demo and ChatGPT to develop this script

# Note: You will need to have Firefox and the Geckodriver

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

targetsite = input("Enter target site url: ")
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster(): # Because why not!
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')

def save_html_response(response_text):
    with open('response.html', 'w', encoding='utf-8') as f:
        f.write(response_text)

def open_html_with_firefox():
    options = Options()
    options.headless = True  # Set to False if you want to run Firefox in GUI mode
    driver = webdriver.Firefox(options=options)
    driver.get('file://' + 'response.html')

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

# Send the cookie back to the site and receive an HTTP response
response_with_cookie = requests.get(targetsite, cookies=cookie)

# Generate a .html file to capture the contents of the HTTP response
save_html_response(response_with_cookie.text)

# Open it with Firefox
open_html_with_firefox()

# End