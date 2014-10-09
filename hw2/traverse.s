BITS 32
    popa ; edi --> ret addr, esi --> 1st param
    push edi
start:
    mov DWORD esi, [esi]
    cmp WORD [esi+4], 0xa700
    jne start
end:
    lea eax, [esi+8]
    ret

; another interesting answer I found
;    pop ebx
;    pop eax
;    mov edx, "FLAG"
;start:
;    inc eax
;    cmp DWORD [eax], edx
;    jne start
;end:
;    jmp ebx
;    nop
;    nop
