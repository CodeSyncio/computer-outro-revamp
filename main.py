#---<imports>---
from ctypes import windll , c_int , c_uint , c_ulong , POINTER , byref
from subprocess import check_call,DEVNULL,STDOUT
from sys import executable
from os import path,mkdir,getcwd,system
try:
    from requests import get
except:
    print('The requests package has not yet been installed. Pressing enter will automatically install it.')
    gh = input()
    print('Installing...')
    check_call([executable, '-m', 'pip', 'install','requests'],stdout=DEVNULL,stderr=STDOUT)
    from requests import get
    print('Done!')
from winsound import PlaySound,SND_ASYNC
from time import sleep
import json
#---<payloads>---
def LoadConfig():
    if path.exists('config.json'):
            pass
    else:
        with open('config.json', 'w') as outfile:
            template = {"AutoInitiate": "","HowToUse":"For shutting down, set AutoInitiate to 's', for fake BSOD, 'fb', and for real BSOD 'b'"}
            json.dump(template, outfile)
            outfile.close()
            print("Config has been created! u can use it to skip the select menu! (not needed, but usefull)")
            sleep(2)
            system('cls')
    
    with open('config.json','r') as cf:
            AutoInit = []
            AutoInit.append(json.load(cf))
    if len(AutoInit[0]['AutoInitiate']) ==0:
        return None
    else:
        return (1 if AutoInit[0]['AutoInitiate'] == 's'else (2 if AutoInit[0]['AutoInitiate'] =='b'else 3)) 
def getfile():
    audio = get('https://github.com/CodeSyncio/computer-outro-downloadables/blob/main/outro.wav?raw=true')
    fake = get('https://github.com/CodeSyncio/computer-outro-downloadables/blob/main/fakebsod.hta?raw=true')
    if path.exists('outro-revamped'): pass
    else: mkdir('outro-revamped')
    open(f'{getcwd()}\\outro-revamped\\outro.wav', 'wb').write(audio.content)
    open(f'{getcwd()}\\outro-revamped\\fakebsod.hta', 'wb').write(fake.content)
    system('cls')
def bsod():
    nullptr = POINTER(c_int)()
    windll.ntdll.RtlAdjustPrivilege(c_uint(19) , c_uint(1) , c_uint(0) , byref(c_int()))
    windll.ntdll.NtRaiseHardError(c_ulong(0xC000007B) , c_ulong(0) , nullptr , nullptr , c_uint(6) , byref(c_uint()))

def sd():
    system('shutdown /s /t 1 -c " "')
    sleep(10)

def fbsod():
    system(f'start {getcwd()}/outro-revamped/fakebsod.hta')
    sleep(15)
    
def play():
    PlaySound(f'{getcwd()}/outro-revamped/outro.wav', SND_ASYNC)
     
#---<start>---
if __name__ == '__main__':
    getfile()
    con = LoadConfig()
    
    if con == None:
        print('Please choose an option.\n[1] Shutdown\n[2] BSOD\n[3] Fake BSOD')
        c = int(input())
    else:
        c = con
    play()
    for i in range(10):
        system('cls')
        print(('BSOD 'if c ==2 else ('Shutting down 'if c ==1 else'FBSOD ')) +'in '+str(10-i) +' seconds...')
        sleep(1)
    if c == 1:
        sd()
    elif c == 2:
        sleep(0.5)
        bsod()
    else:
        fbsod()