#!/usr/bin/env python3
# @Author  : M3tr1c_ r00t
# A tool to help everyone setting up their ubuntu operating system's for cyber security purposes... :)
# For this script to work, you must be root.
# You must also have installed all kali repositories.
# You can use the katoolin script to install the kali repository plus the kali menu.(Find the katoolin script on github)


import os
import time
import sys, traceback
import subprocess
from termcolor import colored


banner = """
 _______  ______ _________ _______  __    _______   _________ _______  _______  _              __    _        _______ _________ _______  _        _        ______   _______
(       )/ ___  \\__   __/(  ____ )/  \  (  ____ \  \__   __/(  __   )(  __   )( \           /  \  ( (    /|(  ____ \\__   __/(  ___  )( \      ( \      / ___  \ (  ____ )
| () () |\/   \  \  ) (   | (    )|\/) ) | (    \/     ) (   | (  )  || (  )  || (           \/) ) |  \  ( || (    \/   ) (   | (   ) || (      | (      \/   \  \| (    )|
| || || |   ___) /  | |   | (____)|  | | | |           | |   | | /   || | /   || |             | | |   \ | || (_____    | |   | (___) || |      | |         ___) /| (____)|
| |(_)| |  (___ (   | |   |     __)  | | | |           | |   | (/ /) || (/ /) || |             | | | (\ \) |(_____  )   | |   |  ___  || |      | |        (___ ( |     __)
| |   | |      ) \  | |   | (\ (     | | | |           | |   |   / | ||   / | || |             | | | | \   |      ) |   | |   | (   ) || |      | |            ) \| (\ (
| )   ( |/\___/  /  | |   | ) \ \____) (_| (____/\     | |   |  (__) ||  (__) || (____/\     __) (_| )  \  |/\____) |   | |   | )   ( || (____/\| (____/\/\___/  /| ) \ \__
|/     \|\______/   )_(   |/   \__/\____/(_______/_____)_(   (_______)(_______)(_______/_____\____/|/    )_)\_______)   )_(   |/     \|(_______/(_______/\______/ |/   \__/
                                                 (_____)                               (_____)                                                                             """



all_tools = ['python2','wordlists','hashcat','john', 'hydra', 'net-tools', 'wireshark', 'searchsploit', 'metasploit-framework', 'nmap', 'gobuster', 'dirsearch', 'ffuf', 'steghide', 'hash-identifier', 'fcrackzip', 'sqlmap', 'binwalk', 'wpscan', 'whois', 'crackmapexec', 'wafw00f', 'python3-impacket', 'impacket-scripts', 'python2', 'hashid', 'git', 'ghidra', 'gdb', 'freerdp2-dev', 'enum4linux', 'jadx', 'joomscan', 'kerberoast', 'linux-exploit-suggester', 'mongo-tools', 'default-libmysqlclient-dev', 'openssh-client', 'openvpn', 'p7zip', 'pdfcrack', 'libapache2-mod-php', 'python3-pip', 'rdesktop', 'sqlitebrowser', 'tcpdump','hashid']
snap_tools = ['searchsploit']
awaiting_install = []

def check_root():
    if os.getuid() != 0:
        print("Sorry. You need to run this script as root :)")
        sys.exit()


def check_tools(all_tools):
    installed = "Installed :)"
    not_installed = "Not Installed!"
    print("Checking your tools...")
    os.system("sleep 2")
    for i in all_tools:
        new_var = str(i)
        output = subprocess.check_output(f"if [ $(which {i}) ]; then echo '{installed}';else echo '{not_installed}';fi",shell=True)
        newout = bytes.decode(output)
        finout = newout.replace("\n","")
        strout = str(finout)
        if strout == not_installed:
            awaiting_install.append(new_var)
    print("The following tools are not installed: ")
    time.sleep(2)
    print(awaiting_install)

def install_tools():
    uniq_val = [y for y in awaiting_install if y in snap_tools]
    if uniq_val == None:
        pass
    else:
        for p in uniq_val:
            print(f"Installing {p}")
            os.system(f"sudo snap install {p} -y")
            time.sleep(2)

    remaining_tools = [b for b in awaiting_install if b not in uniq_val]

    for i in remaining_tools:
        print(" ")
        print(colored(f"Installing {i} ...","red"))
        print(" ")
        os.system(f"sudo apt install {i} -y")
        time.sleep(2)
        print(" ")
    print(colored("Finishing up the installation process...","green"))
    time.sleep(2)
    print("...")
    print(" ")
    print("And Done! :)")
    

def create_banner(banner):
    colored_banner = colored(banner,"green",attrs=["bold"])
    print(colored_banner)
   
def upgrade_tools():
   want_up = input(colored("Would you like to upgrade your system's tools? (y/n)","red",attrs=["bold"]))
   if want_up == "y":
       time.sleep(2)
       print(" ")
       print(colored("Upating is in progress. This might take a while... :)","green"))
       print(" ")
       os.system("sudo apt upgrade -y")
   else:
       print(colored("Exiting the tool installer...","red",attrs=["bold"]))
       time.sleep(1)
       exit()

def set_wordlists():
    dirbuster_wordlists = ['apache-user-enum-1.0.txt','apache-user-enum-2.0.txt','directory-list-1.0.txt','directory-list-2.3-big.txt','directory-list-2.3-medium.txt','directory-list-2.3-small.txt','directory-list-lowercase-2.3-big.txt','directory-list-lowercase-2.3-medium.txt','directory-list-lowercase-2.3-small.txt']
    dns_wordlists = ['bitquark-subdomains-top100000.txt', 'combined_subdomains.txt', 'deepmagic.com-prefixes-top500.txt', 'deepmagic.com-prefixes-top50000.txt', 'dns-Jhaddix.txt', 'fierce-hostlist.txt', 'italian-subdomains.txt', 'namelist.txt', 'shubs-stackoverflow.txt', 'shubs-subdomains.txt', 'sortedcombined-knock-dnsrecon-fierce-reconng.txt', 'subdomains-top1million-110000.txt', 'subdomains-top1million-20000.txt', 'subdomains-top1million-5000.txt', 'tlds.txt']
    print(colored("Setting up your wordlists...","red",attrs=['bold']))

    os.system("mkdir /usr/share/wordlists")
    os.system("git clone https://github.com/v0re/dirb /usr/share/wordlists/set1")
    os.system("mv /usr/share/wordlists/set1/wordlists /usr/share/wordlists/dirb")
    os.system("rm -r /usr/share/wordlists/set1")

    os.system("mkdir /usr/share/wordlists/dirbuster")
    for i in dirbuster_wordlists:
        os.system(f"wget https://hackbbs.org/wordlists/dirbuster/{i} -O /usr/share/wordlists/dirbuster/{i}")
    
    print(colored("Now setting sub-domain wordlists :)","red",attrs['bold']))
    os.system("mkdir /usr/share/wordlists/dns")
    for i in dns_wordlists:
        os.system(f"wget https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/DNS/{i} -O /usr/share/wordlists/dns/{i}")

    print(colored("Setting up rockyou wordlists...","red",attrs=['bold']))
    os.system("wget https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Leaked-Databases/rockyou.txt.tar.gz -O /usr/share/wordlists/rockyou.txt.tar.gz")
    os.system("tar -xvf /usr/share/wordlists/rockyou.txt.tar.gz")
    time.sleep(1)
    print(colored("Done!","green",attrs=['bold'])) 


def main():
    create_banner(banner)
    check_root()
    print(" ")
    print(colored("Welcome to the M3tr1c_T00l installer for ubuntu users!","red",attrs=["bold"]))
    print(" ")
    print(colored("Hope you enjoy the experience! :)","green",attrs=["bold"]))
    time.sleep(1)
    print(" ")
    my_sys_updater = input(colored("Is your system updated? (y/n)","red",attrs=["bold"]))
    if my_sys_updater == "y":
        print(" ")
        pass
    else:
        print(" ")
        print(colored("Updating the system ...","green",attrs=["bold"]))
        time.sleep(2)
        os.system("sudo apt-get update -y")
        print(colored("Updating complete!","green",attrs=["bold"]))

    checking_snap_installation = input(colored("Do you have snap installed? (y/n)","green",attrs= ["bold"]))
    if checking_snap_installation == "y":
        print(" ")
        pass
    else:
        print(" ")
        print(colored("Installing snap ...","red",attrs=["bold"]))
        print(" ")
        time.sleep(2)
        os.system("sudo apt install snapd -y")
        print(colored("Snap has been installed :)","green",attrs=["bold"]))


    choice = input(colored("Would you like to check your tools and install missing ones? (y/n)","red",attrs=["bold"]))
    if choice == "y":
        check_tools(all_tools)
        install_choice = input(colored("Would you like to install the missing tools? (y/n)","green",attrs=["bold"]))
        if install_choice == "y":
            install_tools()
            upgrade_tools()
            get_wordlists = print(colored("Would you like to set up your wordlists? (y/n)","green",attrs=['bold']))
            if get_wordlists =="y":
                set_wordlists()
                time.sleep(1)
                print(colored("Full setup complete! Thank you for your time!(Feel free to give the creator credit by starring this repository ;))","yellow",attrs=['bold']))
                print(colored("Thank you for your time!(Feel free to give the creator credit by starring this repository ;))\nExiting the tool installer...","red",attrs=["bold"]))
                time.sleep(2)
                os.system("exit")
                
        else:
            print(colored("Thank you for your time!(Feel free to give the creator credit by starring this repository ;))\nExiting the tool installer...","red",attrs=["bold"]))
            time.sleep(2)
            os.system("exit")
            
    else:
        print(colored("Thank you for your time!(Feel free to give the creator credit by starring this repository ;))\nExiting the tool installer...","red",attrs=["bold"]))
        time.sleep(2)
        os.system("exit")


# Error Handling....
try:
    main()
except KeyboardInterrupt:
    print(" ")
    print(colored("\nLeaving program. Goodbye :)","blue"))
