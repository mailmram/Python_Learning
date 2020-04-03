import time
from datetime import datetime as dt

hostpath = "/etc/hosts"
redirect = "127.0.0.1"
block_list = ["www.facebook.com", "www.youtube.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working hours...")
        with open(hostpath,'r+') as file:
            content=file.read()
            for website in block_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
    else:
        with open(hostpath,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in block_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")