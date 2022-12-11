### THC Hydra 

**What is THC Hydra?**

Hydra is a parallelized login cracker which supports numerous protocols
to attack. It is very fast and flexible, and new modules are easy to add.
This tool makes it possible for researchers and security consultants to
show how easy it would be to gain unauthorized access to a system
remotely.

### Installation

```bash
sudo apt-get install hydra
```

```bash
apt-get install hydra
```

### Hydra Syntax

#### New

```bash
hydra (some commands) Protocols://target:Port/module_options
```

#### Old 

```bash
hydra (some commands) [ports] target protocol [module options]
```

**Example:**
New Style Syntax
```
hydra ftp://192.168.0.1:2211 -l admin -P list_of_Password.txt 
```

`hydra` : Name of Tool
`ftp` : Protocol
`192.168.0.1`: IP / Hostname 
`2211` : Port
`-l` : for single user `admin` 
`-P` : lists of password specify `list_of_Password.txt`

Single IP : 192.168.0.1
Network / Subnet : 192.168.0/24

| IP | IP:Ports |
| -- | ------- |
| 192.168.1.1 | 192.168.1.1:22 |
| 192.168.1.34 | 192.168.1.34:80 |
| 192.168.1.67 | 192.168.1.67:53 |
| 192.168.1.85 | 192.168.1.85:443 |

Protocols : http, https, ssh, ftp, telnet ,etc.
Destination Ports : 80, 443, 22, 21, 20, etc.

#### Module Options

1. http-get 
- A : auth-type
- H :  user defined header
- S : check for port in http response.


2 . Options

`-l` : only one username 
`-L` : Lists of username
`-p` : only one password
`-P` : Lists of Passwords
`-V` : --verbose, Show output on screen 
`-t` : tasks
`-o` : output file
`-m` : module options

**Modules :**
LOGIN, PLAIN, CRAM-MD5, CRAM-SHA1, CRAM-SHA256, DIGEST-MD5, NTLM, etc.

```bash
hydra -l username -p password ftp://localhost/PLAIN
```

### SSH BruteForce

```
hydra ssh://192.168.0.0:2211 -L /wordlists.txt -P /wordlists.txt  -V -f
# -f : once password match, stop cracking password.
```

**In case of Firewall**
sends request manually.

```
hydra ssh://192.168.0.0:2211 -L /wordlists.txt -P /wordlists.txt  -V -f -t 2
# -t : sends 2 request at a time.
```

### MySQL BruteForce

```
hydra mysql://127.0.0.1 -l root -P password_lists.txt -o passCrack -V
# -o : save the crack password in passCrack file
```

**Password Options**
Use `-e`
`s` : try the login as password
`n` : try an empty passwd
`r` : reverse the login and try it as passwd

```bash
hydra ftp://127.0.0.1 -l anonymous -e n
# n : try an empty passwd 
```

#### Login Page BruteForce

```bash
hydra 192.168.0.1 http-post-form "userName=^USER^&pcPassword=^PASS^&loginBtn=Submit: tHe useranme or password is incorrect ..."
-L /wordlists.txt -P /wordlists.txt -V -t
# userNamme & pcPassword are variable in index.html login page
# ^USER^ & ^PASS^ will try entering username and password
# submit button mention
# incorrect message after : (semicolon)
```

**IPv6**
IP version 6 
```bash
hydra <.....> -6 <protocol....>
# default ipv4 
# for ipv6 give -6 switch
```