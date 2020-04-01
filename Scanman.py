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



print (" $$$$$$$$$$$$$$$$$$   PLEASE WAIT UNTIL SCAN FINISH :)    $$$$$$$$$$$$$$$$$$$  ")



subprocess.run(f'tshark -T fields -e ip.src -r {a}>>SM1.txt ', shell=True)
subprocess.run(f'cat -n SM1.txt | sort -uk2 | sort -nk1 | cut -f2->>HOSTip.txt', shell=True)
subprocess.run('nmap -T4  -O -iL HOSTip.txt >> HOSTos.txt', shell=True)
subprocess.run('nmap -T4  -p- --open  -iL HOSTip.txt >> HOSTopenports.txt', shell=True)
subprocess.run('nmap -T4  -sO -iL HOSTip.txt >> HOSTidenproto.txt', shell=True)

print ("for result search for HOSTip.txt ,HOSTos.txt ,HOSTopenports.txt ,HOSTidenproto.txt" )
