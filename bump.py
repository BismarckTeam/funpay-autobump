import requests
import time

def f():
    link="https://funpay.com/lots/raise"
    
    headers = {
        "Accept" : "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding" : "gzip, deflate, br",
        "Accept-Language" : "ru-RU,ru;q=0.9",
        "Content-Length" : "64",
        "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie" : "-",
        "Origin" : "https://funpay.com",
        "Referer" : "https://funpay.com/lots/1453/trade",
        "Sec-Ch-Ua" : '''"Google Chrome";v="110", "Chromium";v="110", "Not=A?Brand";v="24"''',
        "Sec-Ch-Ua-Mobile" : "?0",
        "Sec-Ch-Ua-Platform" : '''"Windows"''',
        "Sec-Fetch-Dest" : "empty",
        "Sec-Fetch-Mode" : "cors",
        "Sec-Fetch-Site" : "same-origin",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "X-Requested-With" : "XMLHttpRequest"
    }
    
    data = {
        "game_id" : "354",
        "node_id" : "1453",
        "node_ids[]" : "1453",
    }
    
    r = requests.post(link, data=data, headers=headers)
    
    print(r.status_code)
    print(r.text)

while(True):
    f()
    time.sleep(1800)