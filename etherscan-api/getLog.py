import requests

url = "https://api.etherscan.io/api"

payload='apikey=WHTN1JMFV7SKDTAUTPA91WVDPP6FY6ZJHX&module=logs&action=getLogs&fromBlock=100&toBlock=latest&address=0xe83cccfabd4ed148903bf36d4283ee7c8b3494d1'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
