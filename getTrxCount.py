import requests

url = "https://api.etherscan.io/api"

payload='apikey=WHTN1JMFV7SKDTAUTPA91WVDPP6FY6ZJHX&module=proxy&action=eth_getTransactionCount&tag=latest&address=0x4bd5900Cb274ef15b153066D736bf3e83A9ba44e'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
