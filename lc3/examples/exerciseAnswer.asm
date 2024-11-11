	.ORIG	x3000

	LEA R0,MESG1 ;load the address of the message string
	PUTS ;outputs a string

	LEA R0,MESG2 ;load the address of the message string
	PUTS ;outputs a string

	GETC ;Number will be stored in R0
	ADD R2, R0, #0 ;Store number you entered in R2
	
	LD R1, Zero ;Load R1 with '0' in ascii
	
LOOP
	ADD R0, R1, #0

	OUT	

	LEA R0,MESG4 ;load the address of the message string
	PUTS ;outputs a string

	ADD R1, R1, #1
	
	ADD R3, R1, #0

	NOT R3, R3

	ADD R3, R3, #1

	ADD R3, R2, R3
	
	BRzp LOOP

	HALT

;It's where you store strings and variables
MESG1 .STRINGZ "hello\n"
MESG2 .STRINGZ "Please input a number from 0 to 9\n"
MESG3 .STRINGZ "Have a good day!\n"
MESG4 .STRINGZ ", "
Zero   .FILL   48           ; Ascii value of '0'
.END