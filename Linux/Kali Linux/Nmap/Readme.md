## Nmap

### Objectives
- Nmap commands structure
- host discovery
- how nmap scanning works
- target
- ports
- scan type
- scan status
- scan timings
- output formats
- nmap script engine
- service detection
- os detection
- timeout & host delay

### Basics

**Requriements**:

1. ip 
2. port \[default\]
3. scan type [default]
4. scan timings [default]
5. output types [default]

subnet(CIDR): if you want to scan whole network.
you give subnet.

### host discovery

to check system is alive or shutdown.

```
nmap <ip address or subnet (192.168.1.1/24) #scan all host machine is in network>
nmap -sN 192.169.1.1 # -sN is by default if you don'r give then also it starting doing host discovery
nmap 192.168.1.1 # default
```

#### how does it work

-  root user
 - ICMP echo request
 - TCP SYN - port 443
 - TCP ACK - port 80
 - ICMP T.S request

- local user
 - SYN - port 443
 - ACk - port 80

if you don't want to do host discovery
```bash
nmap -Pn 192.168.1.1
```

### how scanning works

**port open (3-way handshake)**
`Machine A` sends **SYN packet** to Machine B (Machine A wants to connect to Machine B)
`Machine B` then sends **SYN & ACK packet** in return (Machine B accept the connection request)
`Machine A` then sends **ACK packet**  (Machine A will connected successfully to Machine B) 

**port closed**
`Machine A` sends **SYN packet** to `Machine B`
`Machine B` sends **RST & ACK packet** to `Machine A` (RST flag [reset flag]  Machine B port is closed)

RFC: request for commits all response of protocol 
nmap using this rules book.

### Target

1. single ip

```
nmap 192.168.1.1
```

2. subnet range
```
nmap 192.168.0.0/24
# all host machine in network
```

3. ip range
```
nmap 192.168.1.1-5
```

4. specific ips
```
nmap 192.168.1.6 192.168.1.4
```

5. text file
```
nmap -iL hostmachines.txt
```

6. domain
```
nmap domainname.com scanme.nmap.org
```

by default 1000 ports are scan


### ports

```
nmap 192.168.1.1 <port>
```

1. single port
```
nmap 1921.168.1.1 -p 80
```

2. sequence port (range)
```
nmap 192.168.1.1 -p20-80 
```

3. distrubuted port only
```
nmap 192.168.1.1 -p80, 22, 21
```

4. service specific 
```
nmap 192.168.1.1 -p http # <service>
```

5. protocol specific
```
nmap 192.168.1.1 -p T:22, U:53 # T(TCP):<port number> and U(UDP): <port number>
```

6. all ports
```
nmap 192.168.1.1 -p- # total ports: 65535
```

7. top port
```
nmap 192.168.1.1 --top-ports 100
```

### scan techniques
- TCP connect scan `-sT`
- TCP SYN scan `-sS`
- FIN scan `-sF`
- xmas scan `-sX`
- null scan `-sN`
- ping scan `-sP`
- UDP scan `-sU`
- ACK scan `-sA`

1. TCP connect scan: `Machine A` will sends **SYN packet** to `Machine B`
`Machine B` will reply with **SYN & ACK packets** to `Machine A`
`Machine A` will then reply with **ACK & RST packets** to `Machine B` (machine A want to closed the connection with RST(reset) flag)

you need root privilieges

2. TCP SYN scan/ stealth scan: `Machine A`
will sends SYN packet
Machine B will sends **SYN & ACK packets** to Machine A (machine B wants to connect)
Machine A will sends RST flag after receiving **SYN packet**

3. UDP scan: on based of ICMP reply nmap decide the port is open or closed

4. ACK scan: Firewall is blocking the packets if finds suspiuious or finds in rileset to block the request, resulting in 
no reply, so nmap can't be sure port is open/closed/filtered

ACK scan helps to finds the firewall enabled or not and rule set.

### scan status
- open
- close
- filtered
- open filtered
- close filtered
- unfiltered

#### open 

Machine A sends **SYN packet** to Machine B
Machine B reply with **SYN + ACK packets** To Machine A
Nmap detect that port is open, because Machine A receive SYN + ACK packet from Machine B.

#### closed

Machine A sends **SYN packet** to Machine B
Machine B reply with **RST + ACK packet**.

Machine B has closed port so sends RST + ACK flag.

```
# root user / superuser
sudo nmap -p 3389,22 scanme.nmap.org
# 22 open ssh
# 3389 closed ms-wbt-server
```
Machine A with root privilieges sends ping request, SYN - 443, ACK - 80, timestamp request and SYN packet to 3389, 22 
Machine B reply with ping reply, timestamp reply, RST + ACK flag on 443, RST flag on 80, and RST + ACK on 3389, SYN + ACK on 22
Machine A sends RST flag on port 22.

```bash
# local user / regular user
nmap -p 3389,22 scanme.nmap.org
# 22 open ssh
# 3389 closed ms-wbt-server
```

**host discovery**
Machine A sends SYN port 80 and SYN port 443
Machine B reply with RST + ACK on port 443 means closed, and SYN + ACK on 80 means open port
Machine A sends ACK, RST + ACK on 80 closed tyhe connection

**request for 3389 and 22 ports**
Machine A sends SYN on port 3389, 22
Machine B reply with SYN + ACK on 22 means open and 
Machine A sends ACk on 22
Machine B reply with RST + ACK on 3389
Machine A sends RST + ACK on 22

#### Filtered

Machine A sends `SYN packet` to Machine B
but Firewall or packet filter will stop the packet will stop packet from reaching Machine B
Firewall or packet filter will only block or drop the packet which is define in ruleset.

#### Unfiltered

Machine A sends SYN packet to Machine B
Machine B reply with ICMP packet

Nmap can't be decide that port is open/closed

**Create rule to block the all packet on port 22**
```bash
sudo iptables -I INPUT -p tcp --dport=22 -j DROP
# iptables: arp tables
# -I : chain (INPUT/OUTPUT)
# -p: protocol (tcp/udp)
# --dport=22: destination port assinged port 22
# -j: ACCEPT/DROP/DENY the packet
```

#### open filtered

firewall set to drop all SYN flag(machine want to connect) and only tansfer data which is already connected

to bypass NULLL scan, XMAS scan FIN scan

NULL scan sends packet which has nothing raw packet.
pass firewall, Machine reply

case1: if port is closed then Machine then response with RST flag

case2: sneds ICMP packet nmap can't decide port is open or not.

case3: when machine A not got response from Machine B
firewall is droping packet or Machine B sends reply but firewall is droping the that reply packet.

```bash
sudo nmap -p 7553 -sN scanme.nmap.org
# -sN: NUll scan
```

no response open or closed

#### close filtered

same open filtered
IDLE scan used

### Scan timings

T0: paranoid slow, in case of IDS 
T1: sneaky less slow, in case of IDS
T2: polite 
T3: normal default
T4: aggressive fast
T5: insane fastest less accurrcy

```
nmap 192.168.1.1 -T4
```

**host timeout**
if service take too long time(specific time)
then leave move to next port.

```bash
nmap --host-timeout 500ms <ip addr>
```

**Scan delay**
delay/wait/stop packet to sends

```
nmap --scan-delay 1s <ip addr>
# 1s: 1 sconds
```

### output types

to save output

1. `-oN`: normal text output 
```
nmap 192.168.1.1 -oN text.txt
```
2. `-oX`:  xml format

```
nmap 192.168.1.1 -oX file.xml
```
3. `-oG`: grepable format
4. `-oS`: script kiddie format [state -> st4t4]

```
nmap 192.168.1.1 -oS file
```

### NSE (Nmap Script Engine)

1. firewall bypass
2. ftp enum
3. dns enum
4. http enu

```
nmap scanme.nmap.org --script http-headers
```

to see scripts
```
cd /usr/share/nmap/scripts
```

### MISC

- service version
```
nmap -sV <ip addr>
```
- os detection
```
nmap -O <ip addr>
```

- verbosity
```
nmap -v <ip>
```

- service version + os detection + scannig + traceroute
```
nmap -A <ip addr>
# aggressive scan
```

- scan ipv6 hots
```
nmap -6 <ipv6 addr>
```
