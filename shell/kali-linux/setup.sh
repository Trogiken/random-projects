#!/bin/bash

# Update kali
echo
echo "****Updating Kali****"
echo
sleep 2s
sudo apt update
sudo apt full-upgrade -y

# Install Default Tools
echo
echo "****Installing Default Tools****"
echo
sleep 2s
sudo apt install -y kali-linux-default

# Install More Tools
echo
echo "****Installing More Tools****"
echo
sleep 2s
list_tools=("kali-tools-hardware" "kali-tools-crypto-stego" "kali-tools-fuzzing" "kali-tools-802-11" "kali-tools-bluetooth" "kali-tools-voip" "kali-linux-labs")
for i in "${list_tools[@]}"; do
    sudo apt install -y $i
done

# Install Menu Items
echo
echo "****Installing Menu Items****"
echo
sleep 2s
list_menu=("kali-tools-information-gathering" "kali-tools-vulnerability" "kali-tools-web" "kali-tools-database" "kali-tools-passwords" "kali-tools-wireless" "kali-tools-reverse-engineering" "kali-tools-exploitation" "kali-tools-social-engineering" "kali-tools-sniffing-spoofing" "kali-tools-post-exploitation" "kali-tools-forensics" "kali-tools-reporting")
for i in "${list_menu[@]}"; do
    sudo apt install -y $i
done

# Install Tor Browser
echo
echo "****Installing Tor Browser****"
echo
sleep 2s
sudo apt install -y tor

# Update again
echo
echo "****Checking for Updates****"
echo
sleep 2s
sudo apt update
sudo apt full-upgrade -y

# Install Git
echo
echo "****Installing Git****"
echo
sleep 2s
sudo apt install -y git

echo
read -p "Enter your name for Git: " name
read -p "Enter your email for Git: " email
read -p "Enter your Personal Access Token for Git: " token

# Configure Git
echo
echo "****Configuring Git****"
echo
sleep 2s
git config --global credential.helper store
git config --global user.name $name
git config --global user.email $email
git config --global user.token $token

# Install Misc Tools
echo
echo "****Installing Misc Tools****"
echo
sleep 2s
sudo apt install -y gobuster
git clone https://github.com/danielmiessler/SecLists.git
git clone https://github.com/lgandx/Responder.git


# Fix Installs
echo
echo "****Fixing Installs****"
echo
sleep 2s
sudo apt --fix-broken install -y

# Cleanup
echo
echo "****Cleaning Up****"
echo
sleep 2s
sudo apt autoremove -y
sudo apt autoclean -y

# Ask to Reboot
echo
read -p "Would you like to reboot now? (y/n): " reboot
if [ $reboot == "y" ]; then
    sudo reboot
else
    echo
    echo "****Setup Complete****"
    echo
fi
