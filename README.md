# basic_usbkeyboard
Had to do USB Keyboard emulation for Pi 4B at work, thought I'd share the code if anyone needs it

Put everything into /share on your Pi

MAKE SURE in /etc/modules you have dwc2 and libcomposite!

```
sudo mkdir -m 1777 /share
cd /share
./install_usb.sh
sudo reboot
```
