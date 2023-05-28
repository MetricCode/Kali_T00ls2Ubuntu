#!/usr/bin/env python3
# @Author  : M3tr1c_ r00t
# A tool to help everyone setting up their ubuntu operating system's for cyber security purposes... :)
# For this script to work, you must be root.
# You must also have installed all kali repositories.
# You can use the katoolin script to install the kali repository plus the kali menu.(Find the katoolin script on github)


import os
import fade
import time
import sys, traceback
import subprocess
from termcolor import colored

banner = """
┬┌─┌─┐┬  ┬┌┬┐┌─┐┌─┐┬  ┌─┐    ┬ ┬┌┐ ┬ ┬┌┐┌┌┬┐┬ ┬
├┴┐├─┤│  │ │ │ ││ ││  └─┐ -- │ │├┴┐│ ││││ │ │ │
┴ ┴┴ ┴┴─┘┴ ┴ └─┘└─┘┴─┘└─┘    └─┘└─┘└─┘┘└┘ ┴ └─┘
"""

# categorizing the tools according to thier specific installers...

all_tools = ['plocate','vim', 'python2','hashcat','john', 'hydra', 'wireshark', 'nmap', 'gobuster', 'dirsearch', 'ffuf', 'steghide', 'fcrackzip', 'sqlmap', 'binwalk','whois', 'ruby-full', 'wafw00f', 'python2', 'gdb', 'openvpn', 'p7zip', 'pdfcrack',  'rdesktop', 'sqlitebrowser', 'tcpdump','hashid','stegseek','gimp','exiftool','nfs-common','autopsy','mysql-client','redis-cli']
snap_tools = ['searchsploit','metasploit-framework', 'crackmapexec', 'enum4linux','ghidra']
checked_tools = ['net-tools', 'python3-impacket', 'freerdp2-dev', 'libapache2-mod-php', 'default-libmysqlclient-dev', 'openssh-client']
awaiting_install = []
gem_tools = ['wpscan']


def check_root():
    if os.getuid() != 0:
        print("Sorry. You need to run this script as root :)")
        sys.exit()

def check_tools(all_tools):
    installed = "Installed :)"
    not_installed = "Not Installed!"
    print(fade.brazil("Checking your tools..."))
    # checking if the tools in the all_tools category are installed...
    for i in all_tools:
        new_var = str(i)
        output = subprocess.check_output(f"if [ $(which {i}) ]; then echo '{installed}';else echo '{not_installed}';fi",shell=True)
        newout = bytes.decode(output)
        finout = newout.replace("\n","")
        strout = str(finout)
        if strout == not_installed:
            awaiting_install.append(new_var)

    print(fade.brazil("The following tools will be installed: "))
    c = 0
    print(fade.purplepink("Via apt..."))
    for i in awaiting_install:
        c += 1
        print(f"{c}). {i}")
        time.sleep(0.5)

    c = 0
    print(fade.purplepink("Via snap..."))
    for i in snap_tools:
        c += 1
        print(f"{c}). {i}")
        time.sleep(0.5)

    c = 0
    print(fade.purplepink("Via gem..."))
    for i in gem_tools:
        c += 1
        print(f"{c}). {i}")
        time.sleep(0.5)
    c = 0
    print(fade.purplepink("Extras..."))
    for i in checked_tools:
        c += 1
        print(f"{c}). {i}")
        time.sleep(0.5)




def install_tools():

    # installing tools from the all_tools which arent installed...
    for i in awaiting_install:
        print(fade.fire(f"Installing {i}"))
        os.system(f"sudo apt install {i} -y")

    # installing snap tools...
    for i in snap_tools:
        print(fade.fire(f"Installing {i}"))
        os.system(f"sudo snap install {i}")

    # installing this tools without checking if they are installed...
    for i in checked_tools:
        print(fade.fire(f"Installing {i}"))
        os.system(f"sudo apt install {i} -y")
        time.sleep(1)

    # installing gem tools...
    for i in gem_tools:
        print(fade.fire(f"Installing {i}"))
        os.system(f"sudo gem install {i}")

    print(fade.brazil("Finishing up the installation process..."))
    time.sleep(1)
    

def create_banner(banner):
    colored_banner = fade.pinkred(banner)
    print(f"{colored_banner}\n" + fade.purpleblue("Created by M3tr1c_r00t...\n\nFollow on Twitter: m3tr1c_r00t\nThank you!"))

   
def upgrade_tools():
    want_up = input(fade.brazil("Would you like to upgrade your system's tools? (y/n)"))
    if want_up == "y":
        time.sleep(2)
        print(fade.fire("Updating..."))
        os.system("sudo apt upgrade -y")
    else:
        print(fade.fire("Exiting the tool installer..."))
        time.sleep(1)
        exit()

def set_wordlists():
    print(fade.fire("\nSetting up your wordlists..."))
    os.system("git clone https://github.com/3ndG4me/KaliLists")
    os.system("mkdir /usr/share/wordlists/")
    os.system("mv KaliLists/* /usr/share/wordlists/")
    print(fade.fire("\nDone!"))

def main():
    create_banner(banner)
    check_root()
    my_sys_updater = input(print(fade.brazil("Is your system updated? (y/n)")))
    if my_sys_updater == "y":
        pass
    elif my_sys_updater == "n":
        print(fade.fire("Updating the system ..."))
        time.sleep(1)
        os.system("sudo apt-get update -y")
        print(fade.fire("Updating complete!"))
    else:
        print(fade.fire("Invalid choice"))
        exit()
    

    checking_snap_installation = input(fade.brazil("Do you have snap installed? (y/n)"))
    if checking_snap_installation == "y":
        pass
    elif checking_snap_installation == "n":
        print(fade.fire("Installing snap ..."))
        time.sleep(1)
        os.system("sudo apt install snapd -y")
        print(fade.fire("Snap installed!",))
    else:
        print(fade.fire("Invalid choice"))
        exit()


    choice = input(fade.brazil("Would you like to check your tools and install missing ones? (y/n)"))

    if choice == "y":
        check_tools(all_tools)
        install_choice = input(fade.brazil("Would you like to install the missing tools? (y/n)"))

        if install_choice == "y":
            install_tools()
            upgrade_tools()
            get_wordlists = print(fade.brazil("Would you like to set up your wordlists? (y/n)"))
            if get_wordlists =="y":
                set_wordlists()
                time.sleep(1)
                print(fade.fire("Full setup complete!"+ "\nExiting the tool installer..."))
                time.sleep(1)
                exit()
                
        else:
            print(fade.fire("Exiting the tool installer..."))
            time.sleep(1)
            exit()
            
    else:
        print(fade.fire("Exiting the tool installer..."))
        time.sleep(1)
        exit()


# Error Handling....
try:
    main()
except KeyboardInterrupt:
    print(fade.fire("Exiting the tool installer..."))
