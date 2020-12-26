from os import rename

import requests

r = requests.get("https://coreyms.com")
print(r.status_code)

name = input("Your Name? \n")
print("Hello, ", name)