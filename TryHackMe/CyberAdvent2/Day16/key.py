#!/usr/bin/env python3

import requests

#Loop

for i in range(1, 100, 2) :

	url = requests.get(f'http://10.10.159.88:8000/api/{i}')

	print(url.text)