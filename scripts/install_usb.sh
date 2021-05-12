#!/bin/bash

# In order to run this script, make install_usb.sh runnable with "sudo chmod +x /share/install_usb.sh"
# then run "sudo /share/install_usb.sh"

if cat /boot/config.txt | grep dtoverlay=dwc2; then
echo exists "dtoverlay=dwc2"
else
echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt
echo "dwc2" | sudo tee -a /etc/modules
fi

sudo chmod +x /share/usb_emu.sh
sudo chmod +x /share/uninstall_usb.sh

if systemctl | grep upHILkeyboard; then
echo exists "upHILkeyboard"
else
sudo cp /share/upHILkeyboard.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start upHILkeyboard
sudo systemctl enable upHILkeyboard
fi

if systemctl | grep rf-kserver; then
echo exists "upHILkeyboard"
else
sudo cp /share/rf-kserver.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start rf-kserver
sudo systemctl enable rf-kserver
fi

