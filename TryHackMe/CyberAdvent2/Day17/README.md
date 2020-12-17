# Day 17 challenge

## ReverseELFneering 

This challenge help you to understand basics of reverse engineering and how to use radre2 to reverse engineer an executable.

Lets deploy the machine and connect via ssh 

Now we do it using rdare2

`r2 -d ./challenge1`

> aaa
let it disassemble

> pdf @main
gives us:

0x00400a30]> pdf @main
            ;-- main:
/ (fcn) sym.main 35
|   sym.main ();
|           ; var int local_ch @ rbp-0xc
|           ; var int local_8h @ rbp-0x8
|           ; var int local_4h @ rbp-0x4
|              ; DATA XREF from 0x00400a4d (entry0)
|           0x00400b4d      55             push rbp
|           0x00400b4e      4889e5         mov rbp, rsp 
|           0x00400b51      c745f4010000.  mov dword [local_ch], 1 <- (local_ch value)
|           0x00400b58      c745f8060000.  mov dword [local_8h], 6 <- (local_8h value)
|           0x00400b5f      8b45f4         mov eax, dword [local_ch]
|           0x00400b62      0faf45f8       imul eax, dword [local_8h] <- (Value of eax when imul is called)
|           0x00400b66      8945fc         mov dword [local_4h], eax <- (Value of local_4h is vlaue of eax that is 6, So value of local_4h before eax set to 0 is 6)
|           0x00400b69      b800000000     mov eax, 0
|           0x00400b6e      5d             pop rbp
\           0x00400b6f      c3             ret

...

	1. What is the value of local_ch when its corresponding movl instruction is called (first if multiple)?
		- Ans: 1 
	2. What is the value of eax when the imull instruction is called?
		- Ans: 6
	3. What is the value of local_4h before eax is set to 0?
		- Ans: 6
...

Thank you <3