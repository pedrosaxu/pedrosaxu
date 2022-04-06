from datetime import datetime
from time import sleep, strftime
import ctypes
from ctypes import CDLL
from pushsafer import Client

longrest = 1
cycle = 1
os = 'mac' #acceptable os: mac, win
current_time=strftime("%H:%M")
push_safer_private_key='' #https://www.pushsafer.com/en/python

def locks_creen(os):
    if os == 'mac':
        login = CDLL('/System/Library/PrivateFrameworks/login.framework/Versions/Current/login')
        result = login.SACLockScreenImmediate()
    elif os == 'win':
        ctypes.windll.user32.LockWorkStation()

def notify_iphone():
    client = Client(push_safer_private_key)
    request = client.send_message("Your rest shift has ended!","⭐️ Head back to work!","a","1","","2","www.pushsafer.com","Open Pushsafer","0","2","60","600","1","","","")

print(f'\n{"="*80}\n\nYour 2 shifts\' pomodore system has started...')
 
while longrest != 3:
    print(f'\n{"*"*80}')

    while cycle<=4:
        print(f'{current_time} Focus cycle {cycle}/4 started...')
        sleep(1/2)

        print('Time to work!!!')
        sleep(2)

        sleep(60*25) #25 minutes of focus 

        if cycle != 4:
            print(f'\n{current_time} Focus cycle {cycle}/4 ended...')
            sleep(1/2)

            print('Walk around!!! Go out and see the day!!!')
            sleep(2)

            locks_creen(os)

            sleep(60*5) #5 minutes of rest
            notify_iphone()

        cycle+=1
        print(f'{"*"*80}')

    print(f'\n{"*"*80}\n{current_time} 5\' rest shift {longrest}/2 ended...')
    sleep(1/2)

    print(f'15\' rest shift has started...\nDon\'t just check your social media !!!!\n{"*"*80}\n')
    sleep(2)

    locks_creen(os)
    
    sleep(60*15) #15 minutes of rest
    notify_iphone()

    longrest+=1
 
print(f'\n{current_time} Your 2 shifts\' pomodore system has ended...\n{"="*80}\n')