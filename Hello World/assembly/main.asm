.global _start

.section .data
    hello:    .asciz "Hello, World!\n"

.section .text
_start:
    // write Hello, World! to stdout
    mov x8, 64                // syscall number for write
    mov x0, 1                 // file descriptor for stdout
    ldr x1, =hello            // pointer to the message
    ldr x2, =13                // message length
    mov x16, 64               // syscall
    svc 0

    // exit the program
    mov x8, 93                // syscall number for exit
    mov x0, 0                 // exit status
    mov x16, 64               // syscall
    svc 0
