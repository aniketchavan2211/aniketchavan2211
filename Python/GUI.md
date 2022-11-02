## Tkinter - Python GUI Module

On termux, Install tkinter module
```
apt-get install python python-tkinter
```

## Desktop Environment
[Termux Wiki - Desktop Environment](https://wiki.termux.com/wiki/Graphical_Environment)
```
pkg install x11-repo
```

```
pkg install tigervnc
```

```
vncserver -localhost
# set password
```

Set DISPLAY ENVIRONMENT Variable
```
export DISPLAY="1"
```

Clients - VNC Viewer
| Address |
| ------- |
| localhost:1 |
| localhost:5901 |
| 127.0.0.1:5901 |
