#!/usr/bin/env python3
import requests

proxies = {
	'https': 'https://52.183.8.192:3128'
}

response = requests.get("https://ipinfo.io/json", proxies=proxies)
print(response.text)
print(response.json()['country'])
