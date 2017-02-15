import os
import sys
os.system("apt-get install python-pip")
import pip
import time
#import
if not os.geteuid() == 0:
    sys.exit("\033[1;31mPlease run this script as root!\033[0m")

####### COLORS #######
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan
NG = '\033[1;35;32m' # Neon Green
####### MAIN CODE #######

banner = O + """
               ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO\
       ::::::;       ;          OOOOO\
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#
""" + W
print banner 
while True:
	main = raw_input(NG + "SandBox> " + W)

	if main == "help":
		print G + "help " + W + "- You're looking at it"
		print G + "modules " + W + "- Install pentesting modules"
		print G + "tools " + W + "- Install pentesting tools"
		print G + "other " + W + "- Install third-party tools"
	elif main == "modules":
		print O + "Which modules would you like to install?"
		print """
1) Scapy
2) SpoofMac
3) Netifaces
4) Pythonwhois
5) Mechanize
6) Google
7) Impacket
8) Requests

0) Install all modules
"""		
		module = raw_input(NG + "SandBox-Modules> " + W)
		if module == "1":
			pip.main(["install", "scapy"])
			print G + "SUCCESSFULLY INSTALLED!"
		if module == "2":
			pip.main(["install", "SpoofMAC"])
			print G + "SUCCESSFULLY INSTALLED!"
		if module == "3":
			pip.main(["install", "netifaces"])
			print G + "SUCCESSFULLY INSTALLED!"
		if module == "4":
			pip.main(["install", "pythonwhois"])
			print G + "SUCCESSFULLY INSTALLED!"
		if module == "5":
			pip.main(["install", "mechanize"])
			print G + "SUCCESSFULLY INSTALLED!"
		if module == "6":
			pip.main(["install", "google"])
			print G + "SUCCESSFULLY INSTALLED!"
		if module == "7":
			pip.main(["install", "impacket"])
			print G + "SUCCESSFULLY INSTALLED!"
		if module == "8":
			pip.main(["install", "requests"])
			print G + "SUCCESSFULLY INSTALLED!"
		if module == "0":
			pip.main(["install", "netifaces", "scapy", "SpoofMAC", "pythonwhois", "mechanize", "google", "impacket", "requests"])
			print G + "SUCCESSFULLY INSTALLED!"
	elif main == "tools":
		print O + "Which tools would you like to install?"
		print """
1) Trity - @_t0x1c
2) B4ckd00r - @_t0x1c
3) Quack - @_t0x1c
4) Animation - @_t0x1c
5) DeadAir - @the.red.team
6) AnnoyingPack - @the.red.team
7) BlackSand - @the.red.team
8) PersistentEye - @the.red.team
9) Paralysis - @the.red.team
10) onTHEgo - @_0dayz_

0) Install all modules
"""		
		module = raw_input(NG + "SandBox-Tools> " + W)
		if module == "1":
			os.system("git clone https://github.com/toxic-ig/Trity")
			print G + "SUCCESSFULLY INSTALLED!"
		if module == "2":
			os.system("git clone https://github.com/toxic-ig/B4ckd00r")
			print G + "SUCCESSFULLY INSTALLED!"
		if module == "3":
			os.system("git clone https://github.com/toxic-ig/Quack")
			print G + "SUCCESSFULLY INSTALLED!"
		if module == "4":
			os.system("git clone https://github.com/toxic-ig/Animation")
			print G + "SUCCESSFULLY INSTALLED!"
		if module == "5":
			os.system("git clone https://github.com/the-red-team/Deadair")
			print G + "SUCCESSFULLY INSTALLED!"
		if module == "6":
			os.system("git clone https://github.com/the-red-team/AnnoyingPack")
			print G + "SUCCESSFULLY INSTALLED!"
		if module == "7":
			os.system("git clone https://github.com/the-red-team/BlackSand")
			print G + "SUCCESSFULLY INSTALLED!"
		if module == "8":
			os.system("git clone https://github.com/the-red-team/PersistentEye")
			print G + "SUCCESSFULLY INSTALLED!"
		if module == "9":
			os.system("git clone https://github.com/the-red-team/Paralysis")
			print G + "SUCCESSFULLY INSTALLED!"
		if module == "10":
			os.system("git clone https://github.com/R3c0nx00/onTHEgo")
			print G + "SUCCESSFULLY INSTALLED!"
		if module == "0":
			print G + "SUCCESSFULLY INSTALLED!"
	elif main == "other":
		print ""
	else:
		print R + "That is not an option :/" + W



