import requests #Module that identifies and handles requests to and from TOR browser

session = requests.session()
session.proxies = {
    "http": "socks5h://127.0.0.1:9050", #connects via socks5 proxy protocol with 'h' to local port 9050
    "https": "socks5h://127.0.0.1:9050" #ssl encryption variation of above code
}

url = "http://example.com" #To allow only traffic from ssl encrypted URLs, chang to HTTPS

response = session.get(url, verify=True) #SSL certificate verification it True by default, setting it to false is not reccomended

print(response.content)


#change URL to https:// and add the URL of a .onion site to access SSL traffic from darkweb