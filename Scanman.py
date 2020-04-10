#!/usr/bin/env python3

import os,sys
import subprocess
from colorama import Fore
from colorama import Style

print(f'{Fore.RED}    ______                                                                  {Style.RESET_ALL}')
print(f'{Fore.RED}   /      \                                                                 {Style.RESET_ALL}')
print(f'{Fore.RED}  /$$$$$$  |  _______   ______   _______   _____  ____    ______   _______  {Style.RESET_ALL}')
print(f'{Fore.RED}  $$ \__$$/  /       | /      \ /       \ /     \/    \  /      \ /       \ {Style.RESET_ALL}')
print(f'{Fore.RED}  $$      \ /$$$$$$$/  $$$$$$  |$$$$$$$  |$$$$$$ $$$$  | $$$$$$  |$$$$$$$  |{Style.RESET_ALL}')
print(f'{Fore.WHITE}   $$$$$$  |$$ |       /    $$ |$$ |  $$ |$$ | $$ | $$ | /    $$ |$$ |  $$ |{Style.RESET_ALL}')
print(f'{Fore.WHITE}  /  \__$$ |$$ \_____ /$$$$$$$ |$$ |  $$ |$$ | $$ | $$ |/$$$$$$$ |$$ |  $$ |{Style.RESET_ALL}')
print(f'{Fore.RED}  $$    $$/ $$       |$$    $$ |$$ |  $$ |$$ | $$ | $$ |$$    $$ |$$ |  $$ |{Style.RESET_ALL}')
print(f'{Fore.RED}   $$$$$$/   $$$$$$$/  $$$$$$$/ $$/   $$/ $$/  $$/  $$/  $$$$$$$/ $$/   $$/ {Style.RESET_ALL}')                                                                       
print(f'{Fore.BLUE} BY: MahmoudJOO{Style.RESET_ALL}') 
print ("       ")

a = input ("Enter The Pcap File Path:  ")
print ("       ")
print (f'{Fore.GREEN}                    ^--------------------------------^  {Style.RESET_ALL}')     
print(f'{Fore.GREEN}____________________| PLEASE WAIT UNTIL SCAN FINISH  |_____________________{Style.RESET_ALL}')
print (f'{Fore.GREEN}                    O--------------------------------O  {Style.RESET_ALL}')
print ("       ")
subprocess.run(f'tshark -T fields -e ip.src -r {a}>SM1.txt ', shell=True )
subprocess.run('cat -n SM1.txt | sort -uk2 | sort -nk1 | cut -f2->HOSTip.txt', shell=True)

subprocess.run('echo  "\033[1;91m----------------------------------\033[m" > RESULTS.txt ' , shell=True)
subprocess.run('echo "\033[1;93mIdentified Protocol For Each HOST\033[m" >>RESULTS.txt' , shell=True)
subprocess.run('echo "\033[1;91m-----------------------------------\033[m" >> RESULTS.txt ' , shell=True)
subprocess.run('echo   >> RESULTS.txt' , shell=True)

subprocess.run('nmap  -T5 -sO --open -iL HOSTip.txt -oG - | grep -Ev "Nmap|Status" >> RESULTS.txt ' , shell=True )

subprocess.run('echo   >> RESULTS.txt' , shell=True)

subprocess.run('echo  "\033[1;32m==============================================================================================\033[m" >> RESULTS.txt ' , shell=True)

subprocess.run('echo   >> RESULTS.txt' , shell=True)

print ("SCAN Identified protocol DONE :    " '\n')

subprocess.run('echo  "\033[1;91m---------------------------------\033[m " >> RESULTS.txt ' , shell=True)
subprocess.run('echo "\033[1;93mOS And Open Ports For Each HOST \033[m"  >>RESULTS.txt' , shell=True)
subprocess.run('echo "\033[1;91m---------------------------------\033[m" >> RESULTS.txt ' , shell=True)
subprocess.run('echo   >> RESULTS.txt' , shell=True)

subprocess.run('nmap -O -T4 --open -iL HOSTip.txt | grep -Ev "shown|Warning|detection|hops|done|Starting|Host|closed|Runing|CPE" | cut -c 1-60 >> RESULTS.txt ' , shell=True)    


print ("SCAN OS & Open Ports DONE :        " '\n')

print(f'{Fore.GREEN}       __..._   _...__{Style.RESET_ALL}'  )
print(f'{Fore.GREEN}  _..-"      `Y`      "-._{Style.RESET_ALL}'  )
print(f'{Fore.GREEN}  \           |           /{Style.RESET_ALL}'  )
print(f'{Fore.GREEN}  \\     THE RESULTS      //{Style.RESET_ALL}'  )
print(f'{Fore.GREEN}  \\\          |         ///{Style.RESET_ALL}')
print(f'{Fore.GREEN}   \\\ _..---. |.---.._ ///{Style.RESET_ALL}')
print(f'{Fore.GREEN}    \\`_..--- .Y.---.._`//{Style.RESET_ALL}')
print ("         ")
subprocess.run('cat RESULTS.txt' , shell=True)
