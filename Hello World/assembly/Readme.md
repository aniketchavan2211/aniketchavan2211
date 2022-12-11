## Assenbly Language

1. assemble the code
install assembler
```
apt install nasm
```

2. convert into object file
```
nasm -f elf64 file.asm -o objectfile.o
```

3. linked file to neccesary files
```
ld objectfile.o -o output
```
4. Run the output file
 
```
./output
```

to check file type
file is package to see details of files and formats.
```
file filename
```

## Assembly arm aarch64

installing binary utils package
```bash
apt install binutils
```

```bash
# assemble converting into object file
as hello.asm -o hello.o

# linking neccessary files
ld hello.o -o hello 

# runnning
./hello
```
