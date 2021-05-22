#!/bin/bash

INSTALL_DIR="/usr/local/bin"
wget https://download.mozilla.org/?product=firefox-stub&os=win&lang=en-US&attribution_code=c291cmNlPXN1cHBvcnQubW96aWxsYS5vcmcmbWVkaXVtPXJlZmVycmFsJmNhbXBhaWduPShub3Qgc2V0KSZjb250ZW50PShub3Qgc2V0KSZleHBlcmltZW50PShub3Qgc2V0KSZ2YXJpYXRpb249KG5vdCBzZXQpJnVhPWVkZ2UmdmlzaXRfaWQ9MTY2NjMyMzEwNi4xNjIxNjk3NDU0&attribution_sig=adb49d216df299c4f451d07e7698f3ed14f83d4927e9fc3ea41fe9d026ce7aad

#json=$(curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest)
#url=$(echo "$json" | jq -r '.assets[].browser_download_url | select(contains("linux64"))')
#url==$(echo "$json" | jq -r '.assets[].browser_download_url | select(contains("linux64"))')
#curl -s -L "$url" | tar -xz

#wget https://www.mozilla.org/en-US/firefox/download/thanks/
#curl -s https://www.mozilla.org/en-US/firefox/download/thanks/
#curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest 
#chmod +x firefox
#chmod +x geckodriver
#sudo mv firefox "$INSTALL_DIR"
#sudo mv geckodriver "$INSTALL_DIR"
#echo "installed geckodriver binary in $INSTALL_DIR"
echo "gecko.sh run"
