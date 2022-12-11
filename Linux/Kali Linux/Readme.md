![Kali Linux logo](https://github.com/aniketchavan2211/Journey-start-from-here/blob/master/Images/images.png)

## Introduction, Downloading, Installing of the Kali Linux

## Kali Linux 
  Kali Linux is a Debian- derived Linux distributions
  that is maintained by **offensive security**.
  It was developed by Mati Aharoni and Devon Dearns.
  Kali Linux is a specially designed OS for network
  Analyst, Penetration testers, or in simple words
  It is for those who work under umbrella of 
  Cybersecurity and analysis. The official
  website of Kali Linux is [kali.org](kali.org)

### Advantages:
  - It has 600+ Penetration testing and network
    security tools pre-installed.
  - It is completely free and open-source. 
  - So you can use it for free and even contribute
    for its development.
  - It supports many languages.
  - Great for these who are intermediate in Linux
    and have their hands on Linux commands.
 
### Disadvantages:
  - It is not recommended for those who are new 
    to linux and want to learn Linux.
  - It is a bit slower.
  - It is Quite unfamiliar.

## Terminologies
  `Kernel` : The kernel is a computer program
    that is the core of a computer's operating
    systems with complete controls over 
    everything in the system,It manages 
    following resources of the Linux like file
    management, Process management, I/O 
    mangement , Memory management, Device 
    mangement.
  
  `Shell` : A shell is special user program
    which provide in interface to user to use
    operating system services.Shell accepts 
    human readable commands from user and convert
    them into something which kernel can 
    understand. It is can command language
    interpreter that execute commands read 
    from input devices such as keyboard 
    from files. Shell gets started when the 
    user logs in or start the terminal.

   `Terminal` : We can say the terminal is a
     dumb thing so it does not know what to
     do with the inputs, so it needs another
     program to process it. The terminal is 
     a program that provides the user with
     a simple command-line interface.

   `Console` : In the case of window OS, the 
     "console" performs the same operation performed
     by the terminal so we can say for Windows
     OS, the console is the alias name for 
     the terminal.

   `Shell Scripting` : As shell can also take 
     commands as input form file we can write 
     these command in a file and can execute 
     them in shell to avoid this respective work.
     These files are called shell scripts or 
     Shell Programs. Shell script are similar
     to the batch file in MS-DOS, Each shell script
     is saved with `.sh` file extension eg: `myscript.sh`

## Downloading & Installing Kali Linux
  First Download ISO file from below link 
 
  This is Official Kali Linux Page

  Download ISO file from here 
  [ Offical Kali Linux  ](kali.org) 

  Choose your Platform
  - Bare Metals 
  - Virtual Machines
  - ARM
  - Mobile
  - Cloud 
  - Containers
  - Live Boot
  - WSL (Windows Subsystem for Linux)


  Every platform has different Installation 
  mostly used as Virtual Machine 
  
  It basically run as virtual OS.
  This will not affect your Host OS Which has your Personal Data, etc
  And Kali is mostly used for Penetration testing, Network uses
  so it perfered to install and run as virtual OS rather than Host OS.
  
  Watch Videos on Youtube for installation.

### Kali NetHunter | Mobile 

 Kali Nethunter is a Free & Open Source Mobile
 Penetration testing platform for Android devices
 based on Kali Linux

 ***Kali Linux Rootless***
 
 Install Kali NetHunter on any stock, 
 unrooted Android device without voiding the 
 warranty.

 Installation :     
 Open termux and type :      
 Allow Termux app Storage Permission :
 ```
 termux-setup-storage  
 ``` 
 Installing wget Package for Downloading Kali :
 ```
 pkg install wget
 ``` 
 Downloading Kali from Kali Database :
 ```
 wget -O install-nethunter-termux https://offs.ec/2MceZWr 
 ```
 Change Permission to execute the install-nethunter-termux :
 ```
 chmod +x install-nethunter-termux
 ```
 Install Shell Script to Install Kali NetHunter :
 ```
 ./install-nethunter-termux  
 ```
 ***Usage:***        
 Commands - To        
 - `nethunter` - To start Kali Linux Command Line Interface.          
 - `nethunter kex passwd` - configure the KeX password (only needed before 1st use).     
 - `nethunter kex &` - start Kali NetHunter Desktop Experience user sessions.  
 - `nethunter kex stop` -   stop Kali NetHunter Desktop Experience.   
 - `nethunter <command>` - run in NetHunter environment.  
 - `nethunter -r` - start Kali NetHunter cli as root.  
 - `nethunter -r kex passwd` - configure the KeX password for root.   
 - `nethunter -r kex &` - start Kali NetHunter Desktop Experience as root.   
 - `nethunter -r kex stop` - stop Kali NetHunter Desktop Experience root sessions. 
 - `nethunter -r kex kill` - Kill all KeX sessions. 
 - `nethunter -r <command>` - run <command> in NetHunter environment as root.  

 `Note:` The command nethunter can be abbreviated 
 to nh. Tip: If you run kex in the background 
 (&) without having set a password, bring 
 it back to the foreground first when prompted
 to enter the password, i.e. via fg <job id> 
 - you can later send it to the background 
 again via Ctrl + z and bg <job id>
 
 Run `sudo apt update && sudo apt full-upgrade -y`
 first thing after installation to update Kali. 
 If you have plenty of storage space available
 you might want to run `sudo apt install -y 
 kali-linux-default` as well.

# Basic Operations & Commands

 `who` - display user.   
 
 `whoami` - prints login user.    
 
 `users` - display all users on machine.  
 
 `groups` - display groups in machine

 `uname` - display type of machine.             
 
 `uname -r` - (recursive) prints version of OS.  
 
 `uname -a` - (all) prints all info.   
 
 `ls` - listing directories and Files.   
 
 `ls -l` - (long listing) display directories.    
  and files with permissions, users, owner, 
  date and much more.     
  
 `ls -R` - display Directories with 
 sub-directories and files inside them.    
 
 `ls -a` - display hidden Directories and Files.  
 
 `cd` - change directory [cd (path/location/directory)].   
 `cd ..` - Back one directory.    
 
 `cd ../../` - this will take you 2 back or 
 top directories from file system tree.    
 
 `cd /` - take you to root directory.    
 
 `cd ~` - change directory home directory.  
 
 `cd $HOME` - change directory home directory.  
 
 `clear` - clear the terminal screen.   
 
 `man` - manual [man (command)].   
 
 `pwd` - print working directory, display where are you
  in file system, which directory are in.    
  
 `whereis` - locate or find the directories or files.   
 
 ### Shell Operators
 
 `&` - This will execute Command in background.
 
 `&&` - This will execute multiple commands one by one in sequencial manner. [ls && pwd].    
 
 `>` - **Redirector operator** Takes output from a command.( overwrite/replace ). 
 
 `>>` - same as `>` operator, appends the outputs rather than replacing (nothing is overwritten).
 
 `<` - takes file as input in command.
 
 
 `apt update -y && apt upgrade -y` - update list and upgrades and install packages -y means yes and -n means no.   
 
 `pkg update -y && pkg upgrade -y` - update & upgrades packages.            
 
 `su` - superuser/Administrator/poweruser/rootuser has full access to machine, by you will login as superuser.     
 `sudo` - superuser do command or operation will done by super user privileges.    
 
 `touch` - To create any type of blank file [touch (file1.txt)].   
 
 `cat` - display the file content on terminal screen [cat files.txt].   
 
 ### Operations 
 
 `touch` - To create file(s).     
 
 `mkdir` -  To Make Directories.     
 
 `cp` - To copy files and directories.     
 
 `mv` - To move files and directories.      
 `rm` - To delete files.  
 
 `rmdir` - To delete empty directory.   
 
 `rm -rf` - To delete directory with recursive and forcefully.   
 
## Important Operations & Commands | Understanding Environment 

`date` - to display date.      

`sudo date --set 10 Jan 2000 00:00` - setting date with superuser permission.       

`cal` - calender.         

`figlet` - to display highlights text [figlet <text>].        
`yes` - looping text [yes <text>] to stop use ctrl + c.       
`factor` - factorize number [factor <number>].      

`ps` - process, PID process ID.         

`ps aux` - display all process.        

`top` - display task.         

`kill` - to kill or stop process or task[kill /pid <number>].        

`dpkg --list` - listing package [dpkg Debian package]
use for Installing, Removing,etc for package.          

`sudo apt install vlc` - installing vlc media player.      

`vlc` - media player use to olay audio and video files.
[vlc <path>].          

`sudo apt install imagemagick` - installing imagemagick use for photo viewer.             

`display` - command use to display photos/images [display <path>].        

`sudo shutdown now` - shutdown command -r (restart) -c (cancel).        

## Text Logs Related Commands | Text Processing Operations in Kali

`touch` - to create a blank file[touch (filename).        

`type` - to create a blank file [type > filename].     

`echo` - [ text > filename ] text will store in file also work with command output will in the file.       

`cat` - display the content of the file.[cat filename].         

`head` - display top or upper or first lines of code or text [head filename].          

`tail` - display down or lower or last lines of code or text [ tail filenmae].           

`tail -2` - -2 is a parameter display two line of text file from last line of text.         

`more` - display text on same terminal Windows [more file name]. 

`less` - display text on separate terminal windows.press ESC to exit.            

`nano` - nano is a text editor.          

`vim` - vim is text editor.          


## Getting System info in Linux | Gathering Specifications in Kali

`df` - disk info.          

`free` - memory and swap information.         

`du` - disk usage.            

`du -sh` - -s stands for size -h means human readable (bytes/KB/MB/GB).               
  
`cat /proc/cpuinfo)` - cpu info.        

`cat /proc/cpuinfo | grep (modelname)` - show mode name `|` pipeline, grep will filter and display.           
  
`ls cpu` - list cpu info.          

`lsblk` - partition.         

`lsusb` - listing usb devices connected to machines.          
`lspci` - graphics card, network card, etc.          

`sudo dmidecode -t system` - system info.         

`sudo dmidecode -t memory ` - RAM info.        

`sudo dmidecode -t bios` - bios info.          

`sudo dmidecode -t processor` - processor info.       

`cat /etc/*release*` - *(asterisk), Os Release info version.         

`lsb_release -a` - OS version release info.         

`sudo apt install hardinfo` - installing hardinfo package.         

`harinfo` - open hardinfo, all info related computers, display, devices, etc.       

## Users & Groups in Kali Linux 

Users and Groups are used on GNU/Linux for access control - that is, to control access to the system's files, directories, and peripherals. linux offers relatively simple/coarse access control mechanisms by default.

Types of Users.

1. Standard User
2. Poweruser/ Adminstrator/ Rootuser/ Superuser 
3. Guest

`users` - lists users on machines.         

`sudo adduser` - Add user [ suod adduser (username)].        
`sudo useradd` - same as adduser.          

`sudo useradd -d [/home/username] -s[/bin/bash] -p [passwd] username` - `-d`directory `-s` shell `-p` passwd.            

`passwd` - change passwd login user.          

`sudo userdel` - delete existing user.          

`sudo groupadd` - to add group.            

`groups` - to see user in which groups.          

`sudo groupdel` - to delete group.          

`sudo usermod -g (groupname) (username)` - to add user to groups.             

`cat /etc/passwd` - directory contains user and passwd.       
`cat /etc/shadow` - passwd in encrypted form.          

`cat /etc/group` - show groups,name,ID.         

`cat /etc/gshadow` - group info, passwd.        

`passwd` - to change login user passwd.           

`sudo passwd root` - to set new passwd for root user.     
## File Permission in Kali Linux 
On a linux system, each file and directory is assigned access rights for the owner of file, the members of a groups of related users, and everybody else.Rights can be assigned to read a file, to write a file, and to execute a file(i.e., run file as a program).

**r** :- read, only see not have permission to write and execute.             
**w** :- write, have read and write access, but not to execute file.            
**x** :- execute, file can be run, you have access to run the program.               

| users | groups | others |
| ----- | ------ | ------ |
| rwx | rwx | rwx |

| Octal | Binary | File mode | Description |
| ----- | ------ | --------- | ----------- |
| 0 | 000 | --- | No access |
| 1 | 001 | --x | execution |
| 2 | 010 | -w- | write |
| 3 | 011 | -wx | write & execute |
| 4 | 100 | r-- | read only |
| 5 | 101 | r-w | read & execute only |
| 6 | 110 | rw- | read & write only |
| 7 | 111 | rwx | read, write & execute |

`sudo chmod 777 filename` :- change permission 
`+` `-` [adding, removing permission, giving access]     

**Example:**
`sudo chmod +777 file` - giving full access.       
`sudo chmod -777 file` - giving no access.         
`sudo chmod +rwx file` - gives the user read, write & execute permission.      

## Networking Commands in Linux | Network Management in Kali Linux

`sudo` :- root user.      
`ifconfig` - ip, mac, boradcast, etc info.      
`ifconfig [interface/adapter] [ip] netmask [netmask]`-  to change ip and netmask, netmask - subnetmask.         
`ping` - to check connection between you and other machine or website.              
`nslookup` :- server address [nslookup (website/ipaddress)].        
`host (website)` :- host address.     
`arp -e` :- address, mac address, hardware type.      
`hostname` :- name of machine in network.      
`netstat -r` :- ip address, gateway, etc network card info         

## Package in Linux | Tool Packages in Kali Linux

`sudo apt install cmatrix` :- cmatrix is a matrix screen to start type cmatrix on terminal, to exit press ctrl + c.         

`sudo apt install libreoffice` :- libreoffice pkg for Documents viewing, editing, etc alternative of MS office but on Linux.      

`sudo apt install sl` :- train animation . 

`sudo apt install espeak` :- speaking pkg espeak (text-to-speech).  

`sudo apt install gimp` :- gimp pkg for photo editing. 

`dpkg --list` :- listing package.           
`sudo apt remove cmatrix` :- to remove cmatrix from machine.        
`sudo apt remove [package name]` :- to remove any package installed on machine.       

## SSH Server in Kali Linux 

SSH Secure Shell, The Secure Shell Protocol is a cryptographic network protocol for operating network services securely over an unsecured network.It's most notable application are remote login and command-line execution.

`apt install ssh server` :- installing ssh server.       
`service ssh start` :- ssh service start.                 
`username@ipaddress` :- username and ipaddress/hostname.       
```
apt list
apt list openssh-server
```  

`sudo service ssh start` :- start ssh server.      
`sudo service ssh status` :- to check ssh status.      
`ifconfig` :- check ip address.           
`ping` :- check connection between two machines.      

### Commands
```
apt list openssh-server
sudo apt upgrade && apt upgrade openssh-server
sudo service ssh start
sudo service ssh status
ssh username@ipaddress
```