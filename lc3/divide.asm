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
	LD R0, DIVIDENT

; Load the divisor into R3
	LD R3, DIVISOR	

; Check if divisor is larger than the dividend
	NOT R3, R3
	ADD R5, R0, R3 
	BRn INVALID

; Clear R2 (used for quotient)
	AND R2, R2, #0


; Loop as long as the dividend (R0) is greater than the divisor (R3)
 	LOOP 	
		LD R3, DIVISOR		    ; Load the divisor into R3 
    		NOT R3, R3		    ; Negate the divisor for 1s complement
		ADD R3, R3, #1		    ; Add 1 for 2s complement
    		ADD R0, R0, R3              ; Subtract the divisor (R3) from the dividend (R0)
		BRn DISPLAY		    ; Branch to display without incrementing counter if negative
		ADD R2, R2, #1		    ; Increment the quotient counter
		ADD R0, R0, #0		    ; This is to ensure that the positive branch is due to the value in R0 and not the counter
		
	
 	BRp LOOP     				; If R0 is positive, continue the loop

; At this point, R0 contains the remainder, and R2 contains the quotient

; Display the remainder and qotient
	DISPLAY	LD R5, ASCII
		ADD R0, R0, R5
		Out
		ADD R0, R2, R5
		OUT
	
	INVALID ;We branch to here if divisor was larger than dividend


	; Halt the program
	HALT
;
DIVIDENT .FILL	8
DIVISOR  .FILL	4
ASCII .FILL   	48
;
	.END

	
	