import requests

url = "https://api.etherscan.io/api"

payload='apikey=WHTN1JMFV7SKDTAUTPA91WVDPP6FY6ZJHX&module=account&address=0x00000000219ab540356cBB839Cbe05303d7705Fa&tag=latest&action=balance'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

