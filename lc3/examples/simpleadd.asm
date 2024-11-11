; This simple program reads two characters from 
; standard input (i.e. the keyboard). The program 
; then adds their ASCII values together and outputs 
; the character corresponding to the new ASCII value 
; to standard output (i.e. the console). ; 
.ORIG x3000 
IN 
ADD R1,R0,#0 
IN 
ADD R0,R0,R1 
OUT 
HALT 
.END