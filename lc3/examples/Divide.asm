;
; Write a program (div.asm) to perform positive integer division algorithm.
;  Your program will have two inputs: the dividend and divisor 
; and have two outputs: the quotient and remainder.
; 
;
; Initialization
;

	.ORIG x3000

; Load the dividend into R0
LD R0, DIVIDEND
; Load the divisor into R3
LD R3, DIVISOR

; Clear R1 (used for quotient) and R2 (used for remainder)
AND R1, R1, #0
AND R2, R2, #0

; Loop as long as the dividend (R0) is greater than the divisor (R3)
DIV_LOOP
    ADD R2, R2, #1          ; Increment the quotitient (R2)
    NOT R3, R3
    ADD R0, R0, R3          ; Subtract the divisor (R3) from the dividend (R0)
    BRp DIV_LOOP            ; If R0 is positive, continue the loop

; At this point, R0 contains the remainder, and R2 contains the quotient
; Store the results
ST R2, QUOTIENT
ST R0, REMAINDER

; Display the remainder and qotient
Out
LEA R0, QUOTIENT
OUT

; Halt the program
HALT

; Data section
DIVIDEND    .FILL   42      ; Example dividend (change as needed)
DIVISOR     .FILL   7       ; Example divisor (change as needed)
QUOTIENT    .BLKW   1       ; Space for quotient
REMAINDER   .BLKW   1       ; Space for remainder

.END

	
	