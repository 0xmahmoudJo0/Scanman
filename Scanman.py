#!/usr/bin/env python3
print ("  /      \                               /  \     /  |                      ")
print (" /$$$$$$  |  _______   ______   _______  $$  \   /$$ |  ______   _______    ")
print (" $$ \__$$/  /       | /      \ /       \ $$$  \ /$$$ | /      \ /       \   ")
print (" $$      \ /$$$$$$$/  $$$$$$  |$$$$$$$  |$$$$  /$$$$ | $$$$$$  |$$$$$$$  |  ")
print ("  $$$$$$  |$$ |       /    $$ |$$ |  $$ |$$ $$ $$/$$ | /    $$ |$$ |  $$ |  ")
print (" /  \__$$ |$$ \_____ /$$$$$$$ |$$ |  $$ |$$ |$$$/ $$ |/$$$$$$$ |$$ |  $$ |  ")
print (" $$    $$/ $$       |$$    $$ |$$ |  $$ |$$ | $/  $$ |$$    $$ |$$ |  $$ |  ")
print ("  $$$$$$/   $$$$$$$/  $$$$$$$/ $$/   $$/ $$/      $$/  $$$$$$$/ $$/   $$/   ")
print ("BY:MahmoudJOO")

import os,sys
import subprocess


a = input ("Enter The Pcap File Path:  " '\n')

print ("$$$$$$$$$$$$$$$$$$   PLEASE WAIT UNTIL SCAN FINISH :)    $$$$$$$$$$$$$$$$$$$" '\n')  

subprocess.run(f'tshark -T fields -e ip.src -r {a}>SM1.txt ', shell=True ,text=False)
subprocess.run('cat -n SM1.txt | sort -uk2 | sort -nk1 | cut -f2->HOSTip.txt', shell=True)

subprocess.run('nmap  -T5 -sO -iL HOSTip.txt -oG - | grep -Ev "Nmap|Status" > RESULTS.txt ' , shell=True )
print ("SCAN Identified protocol DONE :    " '\n')

subprocess.run('echo -------------------------------------------------------------------------------------------------------- >> RESULTS.txt ' , shell=True)

subprocess.run('nmap -O -T5 --open -iL HOSTip.txt | grep -Ev "shown|Warning|detection|hops|done|Starting|Host|closed" >> RESULTS.txt ' , shell=True)
print ("SCAN OS & Open Ports DONE :        " '\n')

print ("the ip hosts in HOSTip.txt   ")
print ("the output is in RESULTS.txt ")
