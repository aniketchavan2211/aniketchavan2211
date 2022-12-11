## Dirb 

### Objectives

- Content & vulnerability scanner
- how dirb works
- basic syntax
- save output
- handle different wordlists
- verbosity scan
- enumerate files specific extension [.PHP]
- scan delay
- proxy
- modify agent, cookie
- add custom header

### content & vulnerability scanner

content scanner scans for content, files for example robots.txt if exist or not, but
vulnerability scanner scan and show vulnerability of service.

dirb is a content scanner

### How drib works

drib has wordlists which contains file names, 
dirb will check those files in target machine. if exist or not. 
target machine sends resposne status code 200 ok, 404 Not Found etc. 

```
https://vulnerable.com/robots.txt
```

dirb will request like above and after receving status code,
check for other file, file name store in wordlists.

```bash
drib http://localhostDVWA
```

tool name : `drib`
url : `http://localhostDVWA`

output : files and directory

```bash
drib http://localhostDVWA -o output.txt
```

to save output use `-o` flag
and filename and extension

```bash
cd usr/share/dirb/wordlists
```

wordlists are store in this directory `usr/share/dirb/wordlists`

```bash
dirb http://localhost/Dvwa wordlists.txt
# given full path of wordlists
```

to specify wordlists

### verbosity scan

```
dirb http:localhost/bWAPP -w
```

`-w` : scan all sub-directory 

### specific extension
```bash
dirb http://localhost -X .php
```

all `.php` files

```bash
dirb http://localhost/bWAPP -X .php,.asp,.jsp
```
search for `.php`, `.asp`, `.jsp`

```bash
dirb http://localhost/DVWA -H .php
```

it also show php.ini, phpinfo.php, index.php, etc

### handle status code

```bash
dirb http://localhost/DVWA -N 302
```

ignored 302 status code pages.

### Delayed Scan

```bash
dirb http://loaclhost/dvwa -z 10000
```

wait for `10000` miliseconds then sends another request.

### proxy

```bash
dirb http://localhost/DVWA -p 192.168.1.3:9999
```
request will go through  proxy server `192.168.1.3:9999`

### user-agent

```bash
drib http://localhost/DVWA -p 192.168.0.3:9999 -a "user-agent"
```
`-a` : user-agent manually

```bash
dirb http://localhost/DVWA -p 192.168.0.3:9999 -c "cookies"
```

### custom header

```bash
dirb http://localhost/DVWA -p 192.168.0.3:9999 -H test:test
```
`-H` :for custom header key:value
