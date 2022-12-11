## Crunch 

### Basic Structure

```bash
crunch <min> <max> <charset> -t <pattern> -o <filename>
# name of tool
# minimum length
# maximum length
# optional others
```

```bash
crunch 3 4 | more
# 3-4 length of passwd
# 123
# 1234
```
`| more` : show less output on screen

### save Output
```
crunch 3 5 -o filename.txt
# -o, --output : save output in file
```

### Charset

Types

- a..b
- A..B
- 0..9
- #..$
- a..b + 0..9, and more

```bash
crunch 3 5
# default character set: a...z
crunch 3 5 AB1

# crunch charset
# /usr/share/crunch/charset.txt
# -f, --file 
# mixalpha is one of charset name
crunch 3 5 -f /usr/share/crunch/charset.txt mixalpha | more
```


### Pattern specific wordlist

@ : lowercase
, : uppercase
% : numbers
^ : symbols

```bash
to specify pattern use '-t'
crunch 4 4 -f ... -t //%% #AA00 AA01
```

```bash
crunch 10 10 -f ... -t %%%%%%%%%% # 10 times numbers
```

```bash
crunch 7 8 0123456789 -t AMAN@%%%% -l aaaa@aaa
# Aman@111
```

```bash
crunch 10 10 -t %%%%%%%%%% | more
```

```bash
crunch 4 4 -t ,,,, | more
```

```bash
crunch 8 8 0123456789 -t AMAN@%%% -l aaaa@aaa | more
```

### permutation

```bash
crunch 4 6 -P AMAN SHARMA MAY
```

```bash
crunch 4 6 -q text.txt | more
```

### Break wordlist into chunks

```bash
crunch 4 5 abcde -c 10 -o START
```

```bash
crunch 4 4 -t %%%% -b 1kb -o START
```

### wordlist compression

Types of zip

-  gzip
- bzip2
- lzma
- 7z

```bash
crunch 4 4 -t %%%% -z gzip -o file.txt
# 4 length passwd
# -t : pattern 4 numbers
# -z : specify zip type
# -o save output in file.txt
# file will then compress
```

### Handle frequency of characters

```bash
crunch 9 9 SumitPa -d 2@
# -d : frequency/duplicate, 2times (ss)
# @ : lowercase
# SumitPass...
```

### Inversion of output

```bash
crunch 8 8 -t Pass@%%% -l aaaa@aaa -i | more
# -i : invert
```
