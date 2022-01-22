import time 
import requests
import json

##colors
W = '\033[0m'
Cyan="\033[1;36m" 
Green="\033[1;32m"
Red="\033[1;31m"
Blue="\033[1;34m"
Yellow="\033[1;33m"

TITLE = """
    
█░█ █▀▀ ▄▀█ █░░ ▀█▀ █░█   █▀▀ █░█ █▀▀ █▀▀ █▄▀ █▀▀ █▀█
█▀█ ██▄ █▀█ █▄▄ ░█░ █▀█   █▄▄ █▀█ ██▄ █▄▄ █░█ ██▄ █▀▄
    """

CREDITS = Blue + "\nCredits: @leantony72" + W
GITHUB = Blue + "\nGithub: https://github.com/leoantony72" + W

print(
    TITLE,
    CREDITS,
    GITHUB
)

def green_box(arg):
    return Green + '\n'+ f"[{arg}] " + W

def red_box(arg):
    return Red + '\n'+ f"[{arg}] " + W

def yellow_box(arg):
    return Yellow + '\n'+ f"[{arg}] " + W



def ping(urls):
    while True:
        time.sleep(3)
        for url in urls:
            try:
                response = requests.get(url)
                # print(f"Pinged {url}")
            except requests.exceptions.MissingSchema :
                print(red_box("!")+"Invalid Url Schema eg: https://google.com ")
                exit(-1)    

            if response.status_code != 200:
                print(Blue +f"{response.url} : Website Down📉")
                time.sleep(10)
                continue
            else:
                print(Blue +f"{response.url} : Website Up📈")

        print("\n")            
                

print(red_box("!")+"Ctr + C to exit")
# Ask For Config FileName
print(yellow_box("*")+Cyan+"Provide Config File If You Have"+W)
config = input(green_box(">")+'Config File(Filename/n): ')

if config.lower() == 'n':
    print(yellow_box("*")+Cyan+"Please use ',' For Multiple Urls"+W)
    urls = [str(x) for x in input(green_box(">")+"Url: ").split(',')]
    ping(urls)

# Open Config File
try:
   with open(config) as data:
     db = json.load(data)
     urls = db["urls"]
except FileNotFoundError:
    print(red_box("!")+"Error: File Not Found")
    exit(-1)
        
## Ping servers
ping(urls)


