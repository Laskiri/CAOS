.ORIG x3000
	AND R4, R4, #0 ; Quotitent 
 	AND R1, R1, #0
	ADD R1, R1, #3 ; Number to divide with
   	LD R2, NUMBER ; Operand
	ADD R5, R2, #0 ; Copy the number into R5
	NOT R3, R1 	; Convert 3 -3 in 2s compl
	ADD R3, R3, #1
LOOP	ADD R5, R2, R3 ; Remainder
	BRn NEGATIVE
	BRz INC_QUOT
	ADD R4, R4, #1
	BRnzp LOOP
	
NEGATIVE NOT R5, R5	; Get the positvie value of the remainder
	 ADD R5, R5, #1 
	 BRnzp END

INC_QUOT ADD R4, R4, #1 
END 	 HALT

NUMBER	.FILL 8
QUOTIENT .BLKW 1
REMAINDER .BLKW 1 
	
	












	