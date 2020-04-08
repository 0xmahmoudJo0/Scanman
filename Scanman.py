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


a = input ("Enter The Pcap File Path:  ")

print ("$$$$$$$$$$$$$$$$$$   PLEASE WAIT UNTIL SCAN FINISH :)    $$$$$$$$$$$$$$$$$$$")  

subprocess.run(f'tshark -T fields -e ip.src -r {a}>SM1.txt ', shell=True ,text=False)
subprocess.run('cat -n SM1.txt | sort -uk2 | sort -nk1 | cut -f2->HOSTip.txt', shell=True)
subprocess.run('nmap -T5  -p- -iL HOSTip.txt -oG - | grep "open"  > RESULTS.txt && nmap  -T5 -sO -iL HOSTip.txt -oG - | grep -v "Nmap\|Status" >> RESULTS.txt && nmap -T5  -O -iL HOSTip.txt | grep "Aggressive OS guesses" | grep -v "gnored" >> RESULTS.txt' , shell=True)

print ("the ip hosts in HOSTip.txt   ")
print ("the output is in RESULTS.txt ")
