## Tkinter - Python GUI Module

On termux, Install tkinter module
```bash
apt-get install python python-tkinter
```

## Desktop Environment
[Termux Wiki - Desktop Environment](https://wiki.termux.com/wiki/Graphical_Environment)
```bash
pkg install x11-repo
```

```bash
pkg install tigervnc
```

```bash
vncserver -localhost
# set password
```

Set DISPLAY ENVIRONMENT Variable
```bash
export DISPLAY="1"
```


```bash
# List Display
vncserver -list
```

```bash
# Kill Display
vncserver -kill upda:1
```

Clients - VNC Viewer
| Address |
| ------- |
| localhost:1 |
| localhost:5901 |
| 127.0.0.1:5901 |



Simple Window
```python
import tkinter

# print(dir(tkinter.Tk))

win = tkinter.Tk(screenName=None, baseName=None, className='Tk', useTk=1)

win.mainloop()
```
