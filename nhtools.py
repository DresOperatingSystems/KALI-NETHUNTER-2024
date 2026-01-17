import os
print ("""\033[93m
İNSTALLİNG NETHUNTERS TOOLKIT AND DEPENDENCIES\033[0m""")
os.system("apt install aircrack-ng -y")
os.system("apt install reaver -y")
os.system("apt install set -y")
os.system("apt install maltego -y")
os.system("apt install zaproxy -y")
os.system("apt install nikto -y")
os.system("apt install sherlock -y")
os.system("apt install burpsuite -y")
os.system("wget https://raw.githubusercontent.com/KasRoudra2/MaxPhisher/main/maxphisher.py  && python3 maxphisher.py")
os.system("apt install hydra -y")
os.system("git clone https://github.com/AdliXSec/Shell-Finder")
os.system("git clone https://github.com/golismero/golismero")
os.system("apt install sqlmap -y")
os.system("apt install nmap -y")
os.system("apt install masscan -y")
os.system("apt install hashcat -y")
print ("""\033[93m
ALL DONE YOU SHOULD NOW HAVE A FULL WORKING NETHUNTER DESKTOP ENVIROMENT.
ALSO WE AT DresOS MUST ASK YOU TO USE THIS SOFTWARE RESPONSIBLY AND THAT WE ARE NOT RESPONSIBLE FOR ANY UNETHICAL USE.
FYI YOU DONT HAVE TO INSTALL THE SUGGESTED PACKAGES BUT CAN IF YOU WANT TO \033[0m""")
