#!/bin/bash

sudo rm -r /sys/kernel/config/usb_gadget/upHILkeyboard/configs/c.1/

sudo systemctl disable upHILkeyboard
sudo rm /etc/systemd/system/upHILkeyboard.service

sudo chmod -x /share/usb_emu.sh