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


a = input ("Enter The Pcap file:  ")

print ("$$$$$$$$$$$$$$$$$$   PLEASE WAIT UNTIL SCAN FINISH :)    $$$$$$$$$$$$$$$$$$$")  

subprocess.run(f'tshark -T fields -e ip.src -r {a}>>SM1.txt ', shell=True)
subprocess.run('cat -n SM1.txt | sort -uk2 | sort -nk1 | cut -f2->>HOSTip.txt', shell=True)
subprocess.run('nmap  -T5 -sO -iL HOSTip.txt -oG -> RESULTS.txt && nmap -T5 -O -iL HOSTip.txt >> RESULTS.txt' , shell=True )
print ("the ip hosts in HOSTip.txt   ")
print ("the output is in RESULTS.txt ")
