## cURL

- Support many protocols: ftp, ftps, http, https, smtp, scp, telnet, tftp, etc 

```
curl www.google.com
```

`curl` sends GET request to `www.google.com`

```bash
curl -o "output.txt" https://www.google.com
```

`-o` : ia a output flag / switch, output or response will store in output.txt 


```
curl --request GET https://www.google.com
# curl --request POST --data "data" https://www.google.com
# DELETE
# PUT
```
you can manually sends http methods 

```bash
curl -o text1 https://www.google.com \
     -o text2 https://www.duckduckgo.com
```

you send multiple request

```bash
curl -O <url>
```

if you want download data from server,
`-O` : file will have same name which was on server.

```bash
curl -C - -O <url> 
```

if in case download is cancel,
to resume download use `-C` and give value
`-` here it says auto. it will start downloading where it left before.

```bash
curl -I https://www.google.com
```

to see only header, `-I`

```bash
curl -A "header" <url>
```

you can manually add header to request

```bash
curl -L google.com
```

`301`, `302` status code in response or
if page are moved to new url.

```bash
curl --limit-rate 20k -O https://www.google.com
# kilobytes megabytes gigabytes
```

set speed limit `--limit-rate 20k`


```bash
curl -x 192.168.1.1:8888 https://www.google.com
```
Set proxy `-x` `ip-address:port-number`
request go through proxy and then final destionation

```
curl -U username:password -x 192.168.1.1:888 google.com
```

if proxy need to verify, 
`-U` : specify username and password

```bash
curl --cookie "Name=value" https://www.google.com
```
**ftp**
```bash
curl -u username:password ftp://sites.com/text.txt
```

to download file from ftp server

```bash
curl -T upload.txt -u username:password ftp://192.168.0.1/
```
to upload file to ftp server
