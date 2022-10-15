import requests


url = "https://api.exmo.me/v1/ticker"

payload='pair=BTC_ETH'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)
response.encoding = 'utf-8' 
print(response.text)