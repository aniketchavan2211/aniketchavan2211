global _start

section .text

_start:
  mov rax,1 ; write syscall, see more /usr/include/x86_64-linux-gnu/asm/unistd_64.h
  mov rdi,1 ; write arg fd: 1(output)
  mov rsi,hello ; buf(fer) hello -> 'hello world'
  mov rdx,11 ; length of buffer(variable) of hello
  syscall

  ;exit
  mov rax,60 ; exit syscall
  mov rdi,22 ; status code
  syscall

section .data

  hello: db 'hello world'
