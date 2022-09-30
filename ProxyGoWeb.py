import webbrowser
import os
import psutil
from colorama import init
init()
from colorama import Fore, Back, Style 
from time import sleep


def Checkrbrowser(Path):
	l = [p.info for p in psutil.process_iter(attrs=['pid', 'name']) if Path in p.info['name']]
	if(len(l)>0):
	    return True
	else:
	    return False



def PROXYGOWEB():
	os.system('cls')
	print(Fore.LIGHTRED_EX+'Proxy Go Web >> Server 198.128.164.197 '+Style.RESET_ALL)
	sleep(2)
	print('Connecting To 198.265.124.128 ....'+Fore.RED+' Failed'+Style.RESET_ALL)
	sleep(2)
	print('Connecting To Sec_PR_01X4 Using Proxy 196.164.214.203'+'\n'+Fore.LIGHTGREEN_EX+'You Are Connected To >> '+Fore.LIGHTYELLOW_EX+'Sec_PR_01X4'+Style.RESET_ALL)
	print()
	print('--------------------------')
	print(Fore.LIGHTCYAN_EX+'CodeName: AB:0x1 '+Style.RESET_ALL)
	print(Fore.LIGHTCYAN_EX+'Github: https://github.com/HackCode0x1'+Style.RESET_ALL)
	print(Fore.LIGHTCYAN_EX+'Proxy Server >> 0x1 Code open Tor Website '+Style.RESET_ALL)
	print(Fore.LIGHTCYAN_EX+'0x1 010101 Proxy Server 196.164.214.203'+Style.RESET_ALL)
	print(Fore.LIGHTCYAN_EX+'[+] Status >>> Connected'+Style.RESET_ALL)
	print()

	chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
	mozilla_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"
	
	url = input('Website->> ')
	os.system('cls')
	print('[1] Open {} >> Firefox'.format(url))
	print('[2] Open {} >> Chrome'.format(url))
	print()
	ch = input(">>>  ")
	if ch=="1":
		if os.path.exists(mozilla_path):
			if Checkrbrowser('firefox')==True:
				webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(mozilla_path))
				webbrowser.get('firefox').open_new_tab('http://googleweblight.com/i?u='+url)
			else:
				webbrowser.register('firefox',
				None,
				webbrowser.BackgroundBrowser(mozilla_path))
				webbrowser.get('firefox').open('http://googleweblight.com/i?u='+url)

		else:
			print('Firefox Not Installed on your System!')

	elif ch=="2":
		if os.path.exists(chrome_path):
			if Checkrbrowser('chrome')==True:
				webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
				webbrowser.get('chrome').open_new_tab('http://googleweblight.com/i?u='+url)
			else:
				webbrowser.register('chrome',
				None,
				webbrowser.BackgroundBrowser(chrome_path))
				webbrowser.get('chrome').open('http://googleweblight.com/i?u='+url)
		else:
			print('chrome Not Installed on your System!')


	else:
		print('[x] invalid option!')
		input('[x] Press Enter To Continue! ')
		os.system('cls')
		PROXYGOWEB()











PROXYGOWEB()


