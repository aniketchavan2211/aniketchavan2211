## How to Change BASH Prompt Color

Default Bash Prompt

```bash
# RED
PS1='\033[1;99m┌──(\e[1;31m\u@\h\e[0m\033[1;99m)—[\[\e[1;34m\]\w\[\e[0m\]\033[1;99m] \n\033[1;99m└─\[\e[0;97m\]\$\[\e[0m\]  '
```

```
# BLUE
PS1='\033[1;99m┌──(\e[1;34m\u@\h\e[0m\033[1;99m)—[\[\e[1;32m\]\w\[\e[0m\]\033[1;99m] \n\033[1;99m└─\[\e[0;97m\]\$\[\e[0m\] '
```

 You can change the text color of your BASH prompt. For example,
 to temporarily change the text of your BASH prompt to green, 
 enter the following:

 ```sh
 export PS1="\e[0;32m[\u@\h \W]\$ \e[0m"
 ```

 Your prompt should have the same text as normal but be colored
 green.

- `\e[` – Begin color changes
- `0;32m` – Specify the color code
- `[\u@\h \W]\$` – This is the code for your normal BASH prompt (username@hostname Workingdirectory $)
- `\e[0m` – Exit color-change mode

 The first number in the color code specifies the typeface:

- `0` – Normal
- `1` – Bold (bright)
- `2` – Dim
- `4` – Underlined

 The second number indicates the color you want:

- `30` – Black
- `31` – Red
- `32` – Green
- `33` – Brown
- `34` – Blue
- `35` – Purple
- `36` – Cyan
- `37` – Light gray

 Additionally, if you combine the bright option with a color
 code, you get a lighter version of that color. For example,
 if you use color code 1;32, you would get light green instead
 of the normal green. If you use 1;33, you get yellow instead
 of brown.

 ```bash
# Set colors to variables
BLACK="\[\033[0;30m\]"
BLACKB="\[\033[1;30m\]"
RED="\[\033[0;31m\]"
REDB="\[\033[1;31m\]"
GREEN="\[\033[0;32m\]"
GREENB="\[\033[1;32m\]"
YELLOW="\[\033[0;33m\]"
YELLOWB="\[\033[1;33m\]"
BLUE="\[\033[0;34m\]"
BLUEB="\[\033[1;34m\]"
PURPLE="\[\033[0;35m\]"
PURPLEB="\[\033[1;35m\]"
CYAN="\[\033[0;36m\]"
CYANB="\[\033[1;36m\]"
WHITE="\[\033[0;37m\]"
WHITEB="\[\033[1;37m\]"
RESET="\[\033[0;0m\]"
 ```

## Reference
- [bash prompt customization](https://wiki.archlinux.org/title/Bash/Prompt_customization#:~:text=Bash%20has%20four%20prompt%20strings,a%20multi%2Dline%20command)
- [Change Color of Bash prompt](https://phoenixnap.com/kb/change-bash-prompt-linux)
