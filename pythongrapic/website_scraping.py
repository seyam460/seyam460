import requests

url = "https://www.facebook.com/"

response = requests.get(url)

output = response.text 
print (output)


