#requests module to send request to the web browser.
import requests
import os
import time
#termcolor module to print colored text.
from termcolor import colored
name = 'figlet -f mono9 "Login-Find" | lolcat'
os.system(name)
print(" "*50,colored("Developer - Shivnath Tathe","red",attrs=['blink']))
print(colored("=============================================================================","yellow"))

#Status code for better understanding.
sts_ok = "Status code - "
sts_other = "Status code - "

#Taking user input as domain mame / URL.
#path1 = input(colored("Enter your main domain name / URL : ","yellow"))
try:
    path1 = input(colored("Enter your main domain name / URL : ","yellow"))

    #Checking if main domain working or not.
    maind = requests.get(path1,timeout=5)
    maind_sts = maind.status_code
    if maind_sts == 200:
        print(colored("\nGood job main domain working, ready to go!!\n","green"))
    else:
        pass

    #Checking if main domain contain / at the end , if true remove it.
    if path1[len(path1)-1]=="/":
        path = path1.rstrip(path1[len(path1)-1])
    else:
        path = path1
        pass
except:
    raise Exception(colored("Main domain not responding","red"))

#Opening a file and readin possible paths.
sub_paths = open("path.txt","r")
for i in sub_paths:
    url = sub_paths.readline()
    find = f"{path}{url}"

    #Requsting with get method with time out of 5.
    res = requests.get(find,timeout=5)

    #Checking for response status_code.
    status= res.status_code
    if status == 200:
        print(sts_ok,status)
        print("[+]",colored(find,"green"))
    else:
        print(sts_other,status)
        print("[-]",colored(find,"red"))
sub_paths.close()

