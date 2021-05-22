#!/bin/bash

INSTALL_DIR="/usr/local/bin"

#json=$(curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest)
#url=$(echo "$json" | jq -r '.assets[].browser_download_url | select(contains("linux64"))')
#url==$(echo "$json" | jq -r '.assets[].browser_download_url | select(contains("linux64"))')
#curl -s -L "$url" | tar -xz
wget https://www.mozilla.org/en-US/firefox/download/thanks/
#curl -s https://www.mozilla.org/en-US/firefox/download/thanks/
#curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest 
#chmod +x firefox
#chmod +x geckodriver
#sudo mv firefox "$INSTALL_DIR"
#sudo mv geckodriver "$INSTALL_DIR"
#echo "installed geckodriver binary in $INSTALL_DIR"
echo "gecko.sh run"
