## John The Ripper

**What is John The Ripper?**

John the Ripper is a tool designed to help systems administrators to
 find weak (easy to guess or crack through brute force) passwords, and
 even automatically mail users warning them about it, if it is desired.

**What is Hash?**

Paassword are store in hash value. using hash function passwords can simply seen, it's unreadable.

Hashing Algorithm

- MD5
- SHA256
- SHA512
- more,..

```bash
john --list=formats
```

**Encrypting vs Hashing**

### How to install John The Ripper Pen Testing Tool

```bash
sudo apt-get install john
```
ask for admin / root privileges.

or

```bash
apt-get install john
```

In Kali Linux, Parrot Security OS and other pentesting OS
has pre-install.

```bash
john file1.txt --format=RAW-MD5
```
**Muliple files**
```
john file1.txt file2.txt file3.txt file.txt --format=RAW-SHA256
```

### Types Of Mode

####  Single Mode

```bash
john --single file1.txt --format=MD5
```

`--single` is for using single mode,
adding hash contain `file.txt`

file.txt:
```
ysmBgjsaSwPlAGFxlOY.TevQqc0hybbAmTXFqG3D.1C
```

#### Wordlist Mode

```bash
john --wordlist=wordlist.txt file1.txt --format=RAW-MD5
```

wordlist.txt:
```
admin
Admin
Admin
password
passwd
pass123
```

we can used wordlist for username and password.

#### Rules

Combinations of password.
```
john --rules=<...>
```

```
john --rules=ShiftToggle --wordlist=wordlist.txt --stdout | more
```

```
admin
Admin
aDmin
adMin

so on...
```

see conf of john rules, etc.
```bash
cd /etc/john
nano /etc/john/john.conf
```

#### Incremental Mode 

```bash
john --incremental:alpha file1.txt --format=RAW-SHA256
 ```
 
 see more details
 ```
 nano /etc/john/john.conf
 ```
 
 configuration file of john.
 
 ### Shadow File 
 
 ```bash
 sudo unshadow /etc/passwd /etc/shadow
 ```

/etc/shadow:
```
username:$hashtype$SALTEDValue$HashPassword:LastPaaswordChange(Epoch):MinimumPasswordAge:MaximumPasswordAge:WaringPeriod:Inactivity Period:Expiration Date:Reserved
```

MinimumPasswordAge -> default value 0 means you can change any time, instantly. setting 2, you can change password after 2 days.

MaximumPasswordAge -> you must change password before the mention date.

WarningPeriod -> it will alert you before password gets expirired. 2 this will alert you before 2 days that Expiration is 2 days ahead change password.

Inactivity ->  after expirired password you don't change password this period you account get disable.

Expriration Period -> account get disable on following day.

Reserved -> upcoming updates

from Last password to Expriration date is all about password in Epoch value.

EPOCH Time System
(in seconds)
```
expr $(date +%s)
```
 
 **Example:**
 ```
 17777 -> Monday 03 September 2018 12:00:00 AM IST
 18000 -> Sunday 14 April 2019 12:00:00 AM IST
 ```
 /etc/passwd:
 ```
 username:passwd denoted here as x:UserID:GroupID:FULL NAME:<Room number:Phone number/Personal Details>:/home/user1<home directory>:/bin/bash<here login shell>
 ```
 
 ```bash
 john file2.txt --wordlist=/usr/share/wordlist/rockyou.txt
john --show file2.txt
 ```
 
 ### Crack Zip file
 ```
 zip2john hash.zip > extract_hash_from_zip.txt
 john extract_hash_from_zip.txt --wordlist=/wordlists.txt
 ```