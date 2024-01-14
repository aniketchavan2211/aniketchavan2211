
## Introduction to Command Prompt 
 
 In CLI (**Command Line Interface**) also known 
 as CUI (**Command User Interface**) or 
 Terminal (**shell**), The user has to type all the commands 
 using the keyword to interact with the 
 computer. There is only text in CLI.


## Basic Commands and Operations Regarding Files, Folders & Locations 

 `dir` - directory to list directory & Files.
 
 `cd [location/directory/path]` - change directory used to change 
   the directory.
 
 
  - `cd ..`: Back. 
  - `cd /` : to change directory to /root or return to home.

 `mkdir [Foldername/directory name]` - make directory 
 
 `ren [directoryname/foldername]` - rename rename/label a 
                                   folder/directory.      

 `type nul> [filename]` - to create new files.

 `copy [filename] [location/directory/path]` - copy used to copy
                                             folder/directory.     

 `del [filename]` - delete delete/remove a files. 
 
 `move [filename] [directory]` - used to move files to folders. 

 `rmdir [foldername/directory]` - to delete a folder . 

## Start & Stop Tasks and Services using CMD
 
  Task - Apps
  Service - System process
 
 `tasklist` - listing tasks running. 

 `taskkill /pid [pid number]`- to stop tasks. 

 `cls` - clearing the terminal. 

 `netstart` - listing running services. 

 `netstop [pid]` - stop service. 

 `driverquery` - opening list of installed drivers. 


## Getting Information about system and Programs using CMD

  `wmic > /output:[path]` - to get name, version,... 

  `wmic > cpu` - detailed description

  vol D: 

 `dispart` > 
 `list disk` > 
 `select disk [1]` > 
 `detail disk`
 `chkdsk`
 `getmac` - used to show mac address.
 `systeminfo`

## Managing User Account

  `net user` - To check/list accounts. 

  `net user [username] /add `- to add accounts. 

  `net user [username] /add [password]` - to add password.

  `net user [username] /del` - to delete account. 

  `net user [Administrator/Guest] /active:yes`

  `net user [Administrator/Guest] /active:no`

  `net user "username"*` -  for password. 
 
## Hide & Encrypt files

  `attrib +h +r +s` - for hiding files. 

  `attrib -h -r -s` - for unhiding files.

  `cipher /e` - for encryting files.

  `cipher /d` -  for decryting files. 

  `cipher /c` - for seeing the files in directory. 

  `cipher /rekey` - for update efs key. 

  `assoc.[extension]` - to know the about installed extension. 

## Creating & Exporting files using CMD (Admin Privileges needed)
 
  `tasklist > [filename.extension]` - to save in file. 

  `echo [type_text] > [filename.extension] `- to save text in file. 

  `copy con [filename.extension]`
    => write here {to exit press ctrl+z}
  `type [filename.ext]` - to create new files.

  `type nul > [filename.extension]`
 
## USB disk format,boot & label(rename) (Admin privileges needed)
 
  ```batch

  diskpart 

  list disk

  select disk [number]

  clean

  create partition primary

  select partition [number]

  format fs=ntfs quick

  active

  assign

  exit
  ```


  format and creating partition in disk drive.
  `label [drive letter:] [rename]` - rename a disk drive.


## Wireless Commands (Admin privileges)
 
  `netsh wlan show profile` - showing wifi connected.

  `netsh wlan show all` - all info in detailed.

  `netsh wlan show profile name="network"  key=clear` - to show passwd.

  `netsh wlan set hostednetwork mode=allow ssid=LINE key=[password]`
   =>`netsh wlan start hostednetwork` - creating hotspot in laptop.
 
## Networking Commands (Admin privileges)
 
  `hostname` - to know the device name.    

  `ipconig` - to show ip address.     

  `getmac` - to show mac address.    

  `ping` - to check connection b/w two system.      

  `tracert` - to tract the network route.    

  `netstat` - to check network statistics.    

  `nslookup` - to get ip address of any domain.
   
## Customization CMD Prompt Window Color changing,Resizing & Title Commands (Admin Privileges needed)
 
  Change properties by Right click on Title Bar and Properties 
  will appear.     

  `color [number]` - {Text color}.  

  `color help` - Display the color and their numbers.  

  `mode [number]` - Resize Window.   

  `title` - Title Bar          

  `prompt [text]`.   
 
## Best Utility Commands (Admin Privileges needed)
 
  `tree` - {Listing the directories and Shb-directories}.     

  `date` - {to change date}.   

  `time` - {to change time}.   

  `doskey/history` - {history of commands}.  

  `shutdown -s -t [000 in seconds]` - {shutdown}.  

  `shutdown -r -t [000 in seconds]` - {restart}.   
 
## Stars Wars Impressive Commands (Admin Privileges)

 ```batch
  enable telnet client by opening contol panel > 
  Programs >
  Windows Features on and off > 
  enable telnet client >
  telnet towel.blinkenlights.nl.
 ```

## Batch scripting 
 
### What's a batch file?

   The definition of a batch file as it used in a Windows/DOS 
   environment is a text file that contains a series of
   commands that executed in sequence for Windows for perform 
   and operation.
 
### Why is it called a batch file?

   It's called a batch file because it "batches" a sequence
   of commands that would normally have to be ran one at times.

### How do you execute a batch file?

   You can run a batch file two ways. Create a shortcut
   the batch file or create your own batch file and save
   it to your desktop or somewhere in the files structure 
   you have access. Then you can either double click the icon 
   for the batch file, or you can execute from the commands 
   line simply by trying the filename and extension,
   e.g. batchfile.bat, and pressing enter.

### Batch File Commands 

  The purpose of batch files in run many DOS Commands at once
  sometimes pausing to allow the administrator to interact 
  with the operation by entering data or starting the process
  if the process is paused. The commands that are used to 
  "program" the batch file are similar to DOS commands. Here 
  is a list of the important commands that are used and their 
  definition.

### Commands

  `echo` - Display text on the screen.    

  `@echo off` - hides the text that is normally output.    

  `start` - run a file with its default application.    

  `rem` - inserts a comments line in the progarm.    

  `mkdir`/`rmdir` - Make / Remove Directory.    

  `del` - delete a files or file.   

  `copy` - copy a file or files.   

  `copy con` - allows to type in.    

  `for`/`in`/`do` - This commands lets you specify files.    

  `title` - edit the title of the window.    
 
### Batch Files: Creating and Executing
 
#### Using Notepad and Wordpad
 
   Notepad or Wordpad is what used to create batch files.These
   text editors are used to type out your batch file because 
   it is easiest way to type out the commands and to edit 
   your batch file after it has been created.
 
#### Creating the batch file in Windows

   Once either Notepad or Wordpad is open you can start typing
   your batch file. Here is an example of a batch file typed
   out in a text editor. Type the Following.

 ```batch
 @echo off
 echo Hello this is a text batch file
 pause
 dir c:\windows
 pause
 ```
 
   Click file and then Save, and then navigate to where you
   want to save the file. For the filename, type "test.bat"
   , and if your version of Windows has a "Save as type"
   option, choose "All files". otherwise it saves as a text
   file. Once you have completed these steps, click the Save
   button and exit notepad.
 
   To run the batch file, double-click it like any other
   program. Once the batch file has completed running it 
   closes automatically.
 
   **Creating the batch file from the Command line**

 1. Open an  MS-DOS commands window or load MS-DOS.

 2. In the MS-DOS prompt, type edit test bat and press enter.

 3. if typed correctly, you should now see a blue edit screen. Within the screen, type:


 ```batch
 @echo off
 echo Hello this a text batch file
 pause 
 dir c:\windows
 pause 
 ```

 4. Once these three lines are entered, click file and choose
   exit, when prompted to save, click Yes. Users who do not 
   have a mouse cursor can accomplish this same task by 
   pressing ALT+F to access the file menu, and then X     o exit. Press Enter to save changes. 

 5. Once you are back at the MS-DOS prompt, type:test
   press Enter to execute the test.bat file.Because the
   first line is a pause, you will be prompted to press
   a key. Upon doing so, the batch file runs line by - line
   , in this case, listing the files in the Windows and 
   Windows / system directories.
 
 
  Here is a batch files for creating and delete user account 

###   ADD USER

 1. In the notepad type Command NET USER [USER1] [123] /ADD, 
   where USER1 is the username a that you want to create an 
   123 is a password for the user want to create an 123 is a 
   password for the user account. If you want to create 50
   user at a time you can simply copy the entire command 
   and can paste it 50 times on the same notepad and change
   the username as per your requirement like, USER, USER2, 
   and so on.

 2. Once you are done with commands you can save the notepad 
   file with BAT extension. For example CREATEUSER.BAT, Make
   sure you specify the filename and extension between"".
 
###   DELETE USER
 1. In the notepad type command NET [USER1] [123] /ADD,where 
 USER1 is the user name that you want to create and 123 
 is the password for the user account.
 If you want to create 50 users at a time you can simply 
 copy the entire command and can paste it 50 times on the
 same notepad and change the username as per your 
 requirement like, USER1, USER2 ....so on.
 2. Once you are done with commands you can save the notepad 
 file with.BAT extension. For example CREATE USER.BAT.
 Make sure you specify the filename and extension between.
 
###   Commands 
 1. `echo` - to display text in terminal.
 2. `@echo off` - {to hide unwanted text in terminal, adding @ will also hide path
 3. `goto` - for executing a loop in terminal.
 4. `color` - to change color of text in terminal.
 5. `set /p` - to declare variable with user input.
 6. `if else` - decision making statements.
 7. `pause` - to hold output on screen.
 8. `cls` - clear previous commands.
 9. `exit /b` - for exiting the terminal.
