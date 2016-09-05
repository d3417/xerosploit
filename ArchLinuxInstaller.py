#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys

#---------------------------------------------------------------------------#
# This file is part of Xerosploit.                                          #
# Xerosploit is free software: you can redistribute it and/or modify        #
# it under the terms of the GNU General Public License as published by      #
# the Free Software Foundation, either version 3 of the License, or         #
# (at your option) any later version.                                       #
#                                                                           #
# Xerosploit is distributed in the hope that it will be useful,             #
# but WITHOUT ANY WARRANTY; without even the implied warranty of            #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
# GNU General Public License for more details.                              #
#                                                                           #
# You should have received a copy of the GNU General Public License         #
# along with Xerosploit.  If not, see <http://www.gnu.org/licenses/>.       #
#                                                                           #
#---------------------------------------------------------------------------#
#                                                                           #
#        Copyright © 2016 LionSec (www.lionsec.net)                         #
#                                                                           #
#---------------------------------------------------------------------------#
#This is the installer ported for ArchLinux distro's by d3417_, for Debian Distro's please use the original installer. THX

if not os.geteuid() == 0:
    sys.exit("""\033[1;91m\n[!] Xerosploit installer must be run as root. ¯\_(ツ)_/¯\n\033[1;m""")
print(""" \033[1;36m
┌══════════════════════════════════════════════════════════════┐
█                                                              █
█                     Xerosploit Installer                     █
█ Ported for ArchLinux by d3417_ (BETA                         █
█ Usage: python2.7 install.py                                  █
█ [DON'T USE OTHER VERSION OF PYTOHN]                          █
└══════════════════════════════════════════════════════════════┘     \033[1;m""")

def main():

	print("\033[1;34m\n[++] Please choose your operating system.\033[1;m")

	print("""
1) ArchLinux
""")
	system0 = raw_input(">>> ")
	if system0 == "1":
		print("\033[1;34m\n[++] Installing Xerosploit ... \033[1;m")

		bet_un = os.system("pacman -R --noconfirm bettercap") # Remove bettercap to avoid some problems . Installed by default with apt-get .
		bet_re_ins = os.system("gem install bettercap") # Reinstall bettercap with gem.

		install = os.system("echo 'Adding BlackArch Repo...' && curl -O https://blackarch.org/strap.sh && chmod +x strap.sh && bash strap.sh && pacman -Sy && pacman -S --noconfirm nmap ruby git libpcap gmp python-pip && pip install terminaltables tabulates && yaourt -S --noconfirm --force hping")

		install1 = os.system("""cd tools/bettercap/ && gem build bettercap.* && sudo gem install xettercap-* && rm xettercap-* && cd ../../ && mkdir -p /usr/share/xerosploit && cp -R tools/ /usr/share/xerosploit/ && cp xerosploit.py /usr/share/xerosploit/xerosploit.py && cp banner.py /usr/share/xerosploit/banner.py && echo 'python2.7 /usr/share/xerosploit/xerosploit.py' > run.sh && cp run.sh /usr/bin/xerosploit && chmod +x /usr/bin/xerosploit && echo 'Fixing XeroSploit Script for Arch' && wget https://gist.githubusercontent.com/d3417/920ebce418188c067ba8b45ea28e6e8a/raw/fe1ec6acbd19e26a4e7f06b89d20145ec372c688/fix.sh && chmod +x fix.sh && bash fix.sh && tput setaf 34; echo "Xerosploit has been sucessfuly installed. Execute 'xerosploit' in your terminal." """)


	else:
		print("Please select the option 1")
		main()
main()
