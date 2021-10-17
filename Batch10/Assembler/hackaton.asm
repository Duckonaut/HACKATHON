global    _start

        section   .text
_start: mov       rax, 1
        mov       rdi, 1
        mov       rsi, hackaton
        mov       rdx, len
        syscall

        mov       rax, 60
        mov		  rdi, 0
        syscall

        section   .data
hackaton:  db     "HACKATON", 10
len :     equ	    $-hackaton